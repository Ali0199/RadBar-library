var a=document.querySelectorAll('.input-text p');
var buttons=document.querySelectorAll('.input-text');
var c=document.querySelectorAll('.input-text input');
var i=0,j=0;
$(document).ready(function()
{
    $('#login').click(function(){
        if(i!=1 && i!=3){
            a[0].classList.toggle('d-b');
            c[0].placeholder="";
            i=1;
        }
    });
    $('#parol').click(function(){
        if(j!=1 && j!=3){
            a[1].classList.toggle('d-b');
            c[1].placeholder="";
            j=1;
        }
    });
    $('.login').keyup(function(){ buttons[0].style.border="0.5px solid #fff";});
    $('.parol').keyup(function(){ buttons[1].style.border="0.5px solid #fff";})
    $('.login').focusout(function(){
        if(c[0].value=="" && i==1){a[0].classList.remove('d-b'); c[0].placeholder="Login"; i=2;}
        if(c[0].value!="" && i==2 ){ a[0].classList.toggle('d-b');   i=1;}
    });
    $('.parol').focusout(function(){
        if(c[1].value=="" && j==1){a[1].classList.remove('d-b'); c[1].placeholder="Parol"; j=2;}
        if(c[1].value!="" && j==2 ){ a[1].classList.toggle('d-b');   j=1;}
    });
    $('.submit-button').click(function(){
        var i=0;
        if(c[0].value!=""){i++;} else{buttons[0].style.border="0.5px solid red";}
        if(c[1].value!=""){i++;} else{buttons[1].style.border="0.5px solid red";}
        if(i==2){$('.kirish form').submit();}
        console.log(i);
    })
});