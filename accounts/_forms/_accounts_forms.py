from django import forms

#models
from accounts.models import Account

class FormAccount(forms.ModelForm):
	# username = forms.CharField(max_length=255,label='NIK')
	class Meta:
		model  = Account
		fields = ("username","nama_lengkap","jenis_kelamin","tempat_lahir","tanggal_lahir","agama",'is_staff','is_superuser')