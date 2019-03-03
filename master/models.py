from django.db import models
from solo.models import SingletonModel
from kependudukan.models import Warga
# Create your models here.
class KonfigurasiSistem(SingletonModel):
	kabupaten = models.CharField(max_length=255,blank=True,null=True,verbose_name='Kabupaten')
	kecamatan = models.CharField(max_length=255,blank=True,null=True,verbose_name='Kecamatan')
	desa = models.CharField(max_length=255,blank=True,null=True,verbose_name='Desa')
	dusun = models.CharField(max_length=255,blank=True,null=True,verbose_name="Dusun")
	kode_pos = models.CharField(max_length=255,blank=True,null=True,verbose_name='Kode Pos')
	# rt_rw = models.CharField(max_length=255,blank=True,null=True,verbose_name='RT/RW')
	rt = models.CharField(max_length=255,blank=True,null=True,verbose_name='RT')
	rw = models.CharField(max_length=255,blank=True,null=True,verbose_name='RW')
	ketua_rt = models.ForeignKey(Warga,blank=True,null=True,verbose_name="Ketua RT",on_delete=models.CASCADE,related_name='sistem_kertua_rt')
	ketua_rw = models.ForeignKey(Warga,blank=True,null=True,verbose_name="Keuata RW",on_delete=models.CASCADE,related_name='sistem_kertua_rw')

	def __str__(self):
		return "Konfigurasi Sistem"

	class Meta:
		verbose_name = "Konfigurasi Sistem"
		verbose_name_plural = "Konfigurasi Sistem"
