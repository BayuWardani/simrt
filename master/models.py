from django.db import models
from solo.models import SingletonModel
# Create your models here.
class KonfigurasiSistem(SingletonModel):
	kecamatan = models.CharField(max_length=255,blank=True,null=True)
	desa = models.CharField(max_length=255,blank=True,null=True)
	dusun = models.CharField(max_length=255,blank=True,null=True)
	rt_rw = models.CharField(max_length=255,blank=True,null=True)
	ketua_rt = models.CharField(max_length=255,blank=True,null=True)
	ketua_rw = models.CharField(max_length=255,blank=True,null=True)


	class Meta:
		verbose_name = "Konfigurasi Sistem"
		verbose_name_plural = "Konfigurasi Sistem"
