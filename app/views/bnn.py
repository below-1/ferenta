from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import Pinjaman, Anggota, StatusPinjaman

def bnn(request):
    context = {}
    context['page_title'] = 'Data Pegawai'
    context['page_pretitle'] = 'Tambah Data Pegawai'

    items = Pinjaman.objects.all()
    context['items'] = items

    return render(request, 'app/bnn.html', context)
