from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Kategori, Bahan, Slide, Testimoni, Kontak, Profil, Custumer

class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nama',)} 
    
class KontakAdmin(admin.ModelAdmin):
    list_display = ['nama','no_whatsup','subject','email']
class SlideAdmin(admin.ModelAdmin):
    list_display = ['judul']   
class BahanAdmin(admin.ModelAdmin):
    list_display = ['nama_bahan','kategori','no_whatsup']
    prepopulated_fields = {'slug': ('nama_bahan',)} 
    readonly_fields = ["dibeli"]
    formfield_overrides = {
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size':'20'})},
        models.PositiveBigIntegerField: {'widget': TextInput(attrs={'size':'25','placeholder':'628##########'})},
        models.CharField: {'widget': TextInput(attrs={'size':'70' })},
    }

class StatisAdmin(admin.ModelAdmin):
    pass
class ProfilAdmin(admin.ModelAdmin):
   
    pass

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Bahan, BahanAdmin)
admin.site.register(Kontak,KontakAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Slide,SlideAdmin)
admin.site.register(Testimoni)
admin.site.register(Custumer)

