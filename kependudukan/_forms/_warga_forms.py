from django import forms

#models
from kependudukan.models import Warga,WargaSementara

class FormWarga(forms.ModelForm):
	username = forms.CharField(max_length=255,label='NIK')
	class Meta:
		model  = Warga
		fields = ("username","nama_lengkap","jenis_kelamin","tempat_lahir","tanggal_lahir","agama","nama_ayah","nama_ibu","alamat")

class FormWargaSementara(forms.ModelForm):
	username = forms.CharField(max_length=255,label='NIK')
	tanggal_datang = forms.CharField(label='Tanggal Datang')
	class Meta:
		model  = WargaSementara
		fields = ("username","nama_lengkap","jenis_kelamin","tempat_lahir","tanggal_lahir","agama","nama_ayah","nama_ibu","alamat",'asal_daerah','asal_alamat','tanggal_datang',)