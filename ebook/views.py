from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .decorators import *
# Login page.


@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        usernameu=request.POST.get('username')
        passwordu=request.POST.get('password')
        user=authenticate(request, username=usernameu, password=passwordu)
        context={'eror':''}
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context={'eror':'Ошибка логина или пароля'}
            return render(request, 'login.html', context)
        
    return render(request, 'login.html')
# Logout
def logoutPage(request):
    logout(request)
    return redirect('login')


# Register page
@unauthenticated_user
def registerPage(request):
    form=CreateUser()
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='user')
            user.groups.add(group)
            reader=Reader.objects.create(
                user=user,
                firstname=user.first_name,
                lastname=user.last_name,
                email=user.email
            )
            reader.save()   
            return redirect('login')

    context={'form':form}
    return render(request, 'register.html', context)
#I am
@login_required(login_url='login')
def im(request):
    user=request.user
    reader=Reader.objects.get(id=user.id)
    form=CreateReader(instance=reader)
    userimg=reader.user_img
    if request.method=='POST':
        form=CreateReader(request.POST, request.FILES, instance=reader )
        post = request.POST.copy()
        post['user']=user
        form=CreateReader(post, request.FILES, instance=reader)
        if form.is_valid():
            print(userimg)
            if userimg!=form.instance.user_img:
                    a="static/"+str(userimg)
                    if os.path.exists(a):
                        if(a!='static/'):
                            os.remove(a)
            form.save()
            user.email=post['email']
            user.first_name=post['firstname']
            user.last_name=post['lastname']
            user.save()
            return redirect('home')
    context={'form':form, 'img':str(reader.user_img)}
    return render(request, 'myself.html', context)

# Hoem view
def homev(request):
    janr=Janr.objects.all()
    context={'janrs':janr}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def booksv(request):
    return render(request, 'books.html')
# Books 
def books(request):
    book=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if str(q)!="": 
            bookn=Books.objects.filter(name__icontains=q)
            bookt=Books.objects.filter(title__icontains=q)
            booka=Books.objects.filter(aftor__icontains=q)
            bookj=Books.objects.filter(janr__janr__icontains=q)
            book.extend(bookn)
            book.extend(bookj)
            book.extend(bookt)
            book.extend(booka)
            if len(book)>0:
                eror=False
            else:
                eror=True
        else:
            book=Books.objects.all()
            eror=False


    else:   
        book=Books.objects.all()
        q=False
        eror=False
    pagination=Paginator(book,8)
    page=request.GET.get('page')
    book=pagination.get_page(page)
    context={'books':book, 'q':q, 'search':eror}
    return render(request, 'books.html', context)
@login_required(login_url='login')
def onebook(request, pk):
    book=Books.objects.get(id=pk)
    user=Reader.objects.get(id=book.user_id)

    context={'books':book, 'user':user}
    return render(request, 'onebook.html', context)
#Download
@login_required(login_url='login')
def download(request, path):
    print("AAAA")
    file_path=os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
        raise Http404
#add Book
def addbook(request):
    form=addbookForm
    if request.method=='POST':
        form=addbookForm(request.POST, request.FILES)
        post = request.POST.copy()
        post['user_id']=request.user.id
        form=addbookForm(post, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('books')       
    if request.method=='GET':
        janr=list(Janr.objects.values())
        if request.is_ajax():
            return JsonResponse({'janres':janr, 'jid':0, 'jn':'Выбери жанр', 'img_book':'Введите изображение книги !!!', 'file_book':'Введите файл книги !!!'}, status=200)
    context={'form':form}
    return render(request, 'addbooks.html', context)
def updatebook(request, pk):
    book=Books.objects.get(id=pk)
    if book.user_id==request.user.id:
        form=updateForm(instance=book)
        oldnamebook=book.book_img
        oldnamefile=book.bookfile
        if request.method=='POST':
            form=updateForm(request.POST, request.FILES, instance=book)
            post = request.POST.copy()
            post['user_id']=request.user.id
            form=updateForm(post, request.FILES,  instance=book)
            if form.is_valid():
                if oldnamebook!=form.instance.book_img:
                    a="static/"+str(oldnamebook)
                    if os.path.exists(a):
                        if(a!='static/'):
                            os.remove(a)
                if  oldnamefile!=form.instance.bookfile:
                    a="static/"+str(oldnamefile)
                    if os.path.exists(a):
                        if(a!='static/'):
                            os.remove(a)
                form.save()
                return redirect('books') 
        context={'form':form}
        if request.method=='GET':
            janr=list(Janr.objects.values())
            if request.is_ajax():
                return JsonResponse({'janres':janr, 'jid':book.janr.id, 'jn':book.janr.janr, 'img_book':str(book.book_img), 'file_book':str(book.bookfile)}, status=200)
        return render(request, 'update.html', context)
    else:
        return redirect('books')


@login_required(login_url='login')
def users(request):
    userb=Reader.objects.all()
    context={'users':userb}
    return render(request, 'users.html', context)


@login_required(login_url='login')
def delete(request, pk_test):
    book=Books.objects.get(id=pk_test)
    if str(request.user.id)==book.userid:
        if request.method=='POST':
            book.delete()
            return redirect('/')
        context={'book':book}
    else:
        return redirect('books')
    return render(request, 'delete.html', context)
    

def janr(request):
    form=JanrForm()
    janr=Janr.objects.all()
    if request.method=='POST':
        form=JanrForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('janr')

    context={'form':form, 'janrs':janr}
    return render(request, 'janr.html', context)
