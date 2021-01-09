from django.contrib import admin

# Register your models here.
from .models  import *

admin.site.register(Reader)
admin.site.register(Books)
admin.site.register(Janr)