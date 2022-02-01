from django.forms import ModelForm, DateInput, ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Anggota, Pinjaman, Pegawai

class AnggotaChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nama}"

class AnggotaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Anggota
        exclude = ['created_at', 'updated_at']
        widgets = {
            'tanggal_lahir': DateInput(attrs={'type': 'date'}),
            'tanggal_masuk': DateInput(attrs={'type': 'date'})
        }

class PegawaiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Pegawai
        exclude = ['created_at', 'updated_at']

class PinjamanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Pinjaman
        exclude = ['created_at', 'updated_at', 'penghasilan', 'status']
        labels = {
          "penghasilan_end": "Penghasilan setelah potongan"
        }
        widgets = {
            'tanggal_pinjam': DateInput(attrs={'type': 'date'}),
            'jatuh_tempo': DateInput(attrs={'type': 'date'})
        }


class PinjamanUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Pinjaman
        exclude = ['created_at', 'updated_at']
        labels = {
          "penghasilan_end": "Penghasilan setelah potongan"
        }
        widgets = {
            'tanggal_pinjam': DateInput(attrs={'type': 'date'}),
            'jatuh_tempo': DateInput(attrs={'type': 'date'})
        }