from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
from django.conf import settings

from accounts.utils import JENIS_KELAMIN,AGAMA

from datetime import datetime,date
# Create your models here.
class Account(AbstractUser):
	nama_lengkap = models.CharField(max_length=255,blank=True,null=True)
	jenis_kelamin = models.CharField(choices=JENIS_KELAMIN,default='N',max_length=2,blank=True,null=True)
	tempat_lahir = models.CharField(max_length=255,blank=True,null=True)
	tanggal_lahir = models.DateField(blank=True,null=True)
	agama = models.PositiveIntegerField(choices=AGAMA,default=1,blank=True,null=True)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE,related_name="dibuat_oleh")

	def __str__(self):
		return "[{}] {}".format(self.username,self.nama_lengkap)

	def get_full_name(self):
		if self.nama_lengkap:
			return self.nama_lengkap
		return self.username

	def get_usia(self):
		hari_ini = date.today()
		usia = hari_ini - self.tanggal_lahir
		return str(usia)

	
	def save(self,*args,**kwargs):
		if not self.id:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		return super(Account,self).save()

	class Meta:
		verbose_name = "Account"
		verbose_name_plural = "Account"