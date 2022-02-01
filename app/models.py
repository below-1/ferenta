from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from dateutil.relativedelta import relativedelta

def integer_min_error_message(label, value):
    return _(f'{label} harus lebih besar dari {value}')

error_messages = {
  'penghasilan': integer_min_error_message('Penghasilan', 0),
  'tanggungan': integer_min_error_message('Tanggungan', 0),
  'besar_pinjaman': integer_min_error_message('Besar Pinjaman', 100_000),
  'potongan_koperasi': integer_min_error_message('Potongan koperasi', 100_000),
  'penghasilan_end': integer_min_error_message('Penghasilan setelah potongan', 100_000)
}

class Sex(models.TextChoices):
    PRIA = 'PR', _('Pria')
    WANITA = 'WN', _('Wanita')

class StatusPeminjam(models.TextChoices):
    LAJANG = 'LJ', _('Lajang')
    MENIKAH = 'MN', _('Menikah')
    JANDA_DUDA = 'JD', _('Janda/Duda')

class Pekerjaan(models.TextChoices):
    HONOR = 'HO', _('Honor')
    PEGAWAI_TETAP = 'PT', _('Pegawai Tetap')
    DOSEN = 'DO', _('Dosen')

class StatusPinjaman(models.TextChoices):
    LANCAR = 'LA', _('Lancar')
    TIDAK_LANCAR = 'TL', _('Tidak Lancar')

class Pegawai(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=256, null=True)
    sex = models.CharField(
      max_length=2, 
      null=True,
      choices=Sex.choices)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def get_sex(self):
        return Sex(self.sex).label

class Anggota(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    nama = models.CharField(max_length=256, null=True)
    sex = models.CharField(
      max_length=2, 
      null=True,
      choices=Sex.choices)
    pekerjaan = models.CharField(
      max_length=2,
      null=True,
      choices=Pekerjaan.choices)
    tempat_lahir = models.CharField(max_length=256)
    tanggal_lahir = models.DateField()
    status = models.CharField(
      max_length=2, 
      null=True,
      choices=StatusPeminjam.choices)
    alamat = models.CharField(max_length=256)
    penghasilan = models.IntegerField(
      validators=[MinValueValidator(0, error_messages['penghasilan'])])
    tanggungan = models.IntegerField(
      validators=[MinValueValidator(0, error_messages['tanggungan'])])
    telpon = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    tanggal_masuk = models.DateField()
    photo = models.ImageField(upload_to="static/uploads", null=True, default="static/user.jpg")

    def get_sex(self):
        return Sex(self.sex).label

    def get_status(self):
        return StatusPeminjam(self.status).label

    def get_pekerjaan(self):
        return Pekerjaan(self.pekerjaan).label

    def get_umur(self):
        now = date.today()
        birth = self.tanggal_lahir
        rd = relativedelta(now, birth)
        return rd

    def __str__(self):
        return f"#{self.id} {self.nama}"

# Create your models here.
class Pinjaman(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    penghasilan = models.IntegerField(
      validators=[MinValueValidator(0, error_messages['penghasilan'])])
    tanggungan = models.IntegerField(
      validators=[MinValueValidator(0, error_messages['tanggungan'])])
    nominal = models.IntegerField(
      validators=[MinValueValidator(100_000, error_messages['besar_pinjaman'])])
    potongan_koperasi = models.IntegerField(
      validators=[MinValueValidator(100_000, error_messages['potongan_koperasi'])])
    penghasilan_end = models.IntegerField(
      validators=[MinValueValidator(100_000, error_messages['penghasilan_end'])])

    tanggal_pinjam = models.DateField()
    jatuh_tempo = models.DateField()
    status = models.CharField(
      max_length=2, 
      null=True,
      choices=StatusPinjaman.choices)

    anggota = models.ForeignKey(Anggota,  on_delete=models.CASCADE)

    def get_status(self):
        return StatusPinjaman(self.status).label

    def to_array(self):
        x1, x2, x3, x4, x5, x6, x7, x8 = [0, 0, 0, 0, 0, 0, 0, 0]
        x1 = 1 if self.anggota.sex == Sex.PRIA else 2

        if self.anggota.status == StatusPeminjam.LAJANG:
            x2 = 1
        elif self.anggota.status == StatusPeminjam.MENIKAH:
            x2 = 2
        else:
            x2 = 1

        if self.anggota.pekerjaan == Pekerjaan.HONOR:
            x3 = 3
        elif self.anggota.pekerjaan == Pekerjaan.PEGAWAI_TETAP:
            x3 = 2
        else:
            x3 = 1

        x4 = self.penghasilan
        x5 = self.tanggungan
        x6 = self.nominal
        x7 = self.potongan_koperasi
        x8 = self.penghasilan_end

        return [x1, x2, x3, x4, x5, x6, x7, x8]


class Angsuran(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nominal = models.IntegerField()
    tanggal_setor = models.DateField()

    pinjaman = models.ForeignKey(Pinjaman, on_delete=models.CASCADE)

class Setoran(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nominal = models.IntegerField()
    saldo = models.IntegerField()
    tanggal_setor = models.DateField()

    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
