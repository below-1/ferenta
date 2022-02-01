from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import Pinjaman, Anggota, StatusPinjaman
from app.forms import PinjamanForm, PinjamanUpdateForm
from app.comp import build_classifier
import numpy as np

def list_pinjaman(request):
    context = {}
    items = Pinjaman.objects.all()
    context['items'] = items
    context['page_title'] = 'Data Pinjaman'
    context['page_pretitle'] = 'List Data Pinjaman'
    return render(request, "app/pinjaman/list.html", context)

def create_pinjaman(request):
    context = {}
    if request.method == 'POST':
        form = PinjamanForm(request.POST)
        # Get anggota
        if form.is_valid():
            anggota = form.cleaned_data['anggota']
            pinjaman = form.save(commit=False)
            pinjaman.penghasilan = anggota.penghasilan

            classifier = build_classifier()
            x = pinjaman.to_array()

            result = classifier.predict([ x ])

            status = StatusPinjaman.LANCAR if np.isclose(result, 1) else StatusPinjaman.TIDAK_LANCAR
            pinjaman.status = status
            pinjaman.save()

            return redirect('list_pinjaman')
        context['form'] = form
        context['errors'] = form.errors.as_data()


    else:
        context['form'] = PinjamanForm()
    context['page_title'] = 'Data Pinjaman'
    context['page_pretitle'] = 'Tambah Data Pinjaman'
    return render(request, 'app/pinjaman/create-1.html', context)

def remove_pinjaman(request, id):
    item = Pinjaman.objects.get(id=id)
    item.delete()
    return redirect('list_pinjaman')

def update_pinjaman(request, id):
    context = {}
    item = Pinjaman.objects.get(id=id)
    context['item'] = item
    if request.method == 'POST':
        form = PinjamanUpdateForm(request.POST, instance=item)
        if form.is_valid():
            # Process form
            form.save()
            return redirect('list_pinjaman')
        context['form'] = form
    else:
        context['form'] = PinjamanUpdateForm(instance=item)
    context['page_title'] = 'Data Pinjaman'
    context['page_pretitle'] = 'Update Data Pinjaman'
    return render(request, 'app/pinjaman/edit.html', context)
