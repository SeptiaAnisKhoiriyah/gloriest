from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import Profil, Kategori, Bahan, Slide,Testimoni, Custumer
from cart.models import Transaksi



class KategoriForm(ModelForm):
    class Meta:
        model = Kategori
        fields=['nama','aktif']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control','placeholder':'Kategori'}),


           

        }

class BahanForm(forms.ModelForm):
    
    class Meta:
        model = Bahan
        fields = ['kategori', 'nama_bahan', 'gambar', 'gambar_satu', 'gambar_dua', 'gambar_tiga',
                  'gambar_empat', 'gambar_lima', 'keterangan', 'harga', 'no_whatsup', 'diskon','stock']
        widgets = {
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'nama_bahan': forms.TextInput(attrs={'class': 'form-control'}),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gambar_satu': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gambar_dua': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gambar_tiga': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gambar_empat': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gambar_lima': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_whatsup': forms.TextInput(attrs={'class': 'form-control'}),
            'diskon': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['judul', 'gambar_slide', 'aktif']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'gambar_slide': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'aktif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


        }

class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ('nama', 'pekerjaan', 'gambar_testimoni', 'deskripsi', 'aktif')
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan': forms.TextInput(attrs={'class': 'form-control'}),
            'gambar_testimoni': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 30}),
            'aktif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



