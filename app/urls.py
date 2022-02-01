from django.urls import path

from app.views import index, pinjaman, pegawai, anggota, bnn

urlpatterns = [
    path('', index, name='index'),
    path('pegawai', pegawai.list_pegawai, name='list_pegawai'),
    path('pegawai/create', pegawai.create_pegawai, name='create_pegawai'),
    
    path('pinjaman', pinjaman.list_pinjaman, name='list_pinjaman'),
    path('pinjaman/create', pinjaman.create_pinjaman, name='create_pinjaman'),
    path('pinjaman/<int:id>/remove', pinjaman.remove_pinjaman, name='remove_pinjaman'),
    path('pinjaman/<int:id>/edit', pinjaman.update_pinjaman, name='update_pinjaman'),

    path('anggota', anggota.list_anggota, name='list_anggota'),
    path('anggota/create', anggota.create_anggota, name='create_anggota'),
    path('anggota/<int:id>/edit', anggota.edit_anggota, name='edit_anggota'),
    path('anggota/<int:id>/remove', anggota.remove_anggota, name='remove_anggota'),

    path('bnn', bnn.bnn, name='bnn'),
]