from django.contrib import admin

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategori','date')

admin.site.register(Artikel, ArtikelAdmin)

class InfoAdmin(admin.ModelAdmin):
    list_display = ('author','title','link','isodate','description','image','content')

admin.site.register(Info, InfoAdmin)
# Register your models here.
