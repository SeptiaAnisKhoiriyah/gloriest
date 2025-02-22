from django.urls import path
from . import views



urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),

    path('kategori-admin/', views.kategori_admin, name='kategori_admin'),
     path('form-kategori/', views.formkategori_admin, name='formkategori_admin'),
    path('edit-kategori/<str:slug>', views.editkategori_admin, name='editkategori_admin'),
    path('delete-kategori/<str:pk>', views.deletekategori_admin, name='deletekategori_admin'),

    
    path('bahan-admin/', views.bahan_admin, name='bahan_admin'),
    path('form-bahan/', views.formbahan_admin, name='formbahan_admin'),
    path('edit-bahan/<str:slug>', views.editbahan_admin, name='editbahan_admin'),
    path('delete-bahan/<str:pk>', views.deletebahan_admin, name='deletebahan_admin'),


    path('slide-admin/', views.slide_admin, name='slide_admin'),
     path('form-slide/', views.formslide_admin, name='formslide_admin'),
    path('edit-slide/<str:pk>', views.editslide_admin, name='editslide_admin'),
    path('delete-slide/<str:pk>', views.deleteslide_admin, name='deleteslide_admin'),

    path('testimoni/', views.testimoni_admin, name='testimoni_admin'),
    path('form-testimoni/', views.formtestimoni_admin, name='formtestimoni_admin'),
    path('edit-testimoni/<str:pk>', views.edittestimoni_admin, name='edittestimoni_admin'),
    path('delete-testimoni/<str:pk>', views.deletetestimoni_admin, name='deletetestimoni_admin'),

     path('kontak/', views.kontak_admin, name='kontak_admin'),

 
    path('laporan/', views.laporan, name='laporan'),
    path('transaksi/', views.transaksi_list, name='transaksi_list'),
     path('transaksi/detail/<str:notransaksi>/', views.detail_transaksi, name='detail_transaksi'),


    path('custumer-admin/', views.custumer_admin, name='custumer_admin'),
    path('delete-custumer/<str:pk>', views.deletecustumer_admin, name='deletecustumer_admin'),
]
  
