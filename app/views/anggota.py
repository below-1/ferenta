from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import Anggota, Sex
from app.forms import AnggotaForm

def create_anggota(request):
    context = {}
    if request.method == 'POST':
        form = AnggotaForm(request.POST, request.FILES)
        anggota = form.save()
        return redirect('list_anggota')
    else:
        context['form'] = AnggotaForm()
    context['page_title'] = 'Data Anggota'
    context['page_pretitle'] = 'Tambah Data Anggota'
    return render(request, 'app/anggota/create.html', context)

def edit_anggota(request, id):
    item = Anggota.objects.get(id=id)
    context = {}
    context['page_title'] = 'Data Anggota'
    context['page_pretitle'] = 'Edit Data Anggota'
    if request.method == 'POST':
        form = AnggotaForm(request.POST, request.FILES, instance=item)
        form.save()
        return redirect('list_anggota')
    else:
        context['form'] = AnggotaForm(instance=item)
        pass
    return render(request, 'app/anggota/edit.html', context)

def list_anggota(request):
    context = {}
    context['items'] = Anggota.objects.all()
    context['page_title'] = 'Data Anggota'
    context['page_pretitle'] = 'List Data Anggota'
    return render(request, 'app/anggota/list.html', context)

def remove_anggota(request, id):
    item = Anggota.objects.get(id=id)
    item.delete()
    return redirect('list_anggota')
