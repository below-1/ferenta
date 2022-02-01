from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import Pegawai, Sex
from app.forms import PegawaiForm

def create_pegawai(request):
    context = {}
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        form.save()
        return redirect('list_pegawai')
    else:
        context['form'] = PegawaiForm()
    context['page_title'] = 'Data Pegawai'
    context['page_pretitle'] = 'Tambah Data Pegawai'
    return render(request, 'app/pegawai/create.html', context)

def list_pegawai(request):
    context = {}
    context['items'] = Pegawai.objects.all()
    context['page_title'] = 'Data Pegawai'
    context['page_pretitle'] = 'List Data Pegawai'

    return render(request, 'app/pegawai/list.html', context)
