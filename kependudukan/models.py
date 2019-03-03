from django.db import models
from django.conf import settings


from accounts.models import Account
from kependudukan.utils import KWARGANEGARAAN


from datetime import datetime


class JenisIdentitas(models.Model):
	nama_jenis_identitas = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.nama_jenis_identitas

	def get_nama(self):
		return self.nama_jenis_identitas

	class Meta:
		verbose_name = "Jenis Identitas"
		verbose_name_plural = "Jenis Identitas"

class JenisPekerjaan(models.Model):
	nama_jenis_pekerjaan = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.nama_jenis_pekerjaan

	def get_nama(self):
		return self.nama_jenis_pekerjaan

	class Meta:
		verbose_name = "Jenis Pekerjaan"
		verbose_name_plural = "Jenis Pekerjaan"

class KategoriTidakAktif(models.Model):
	nama_kategeori = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.nama_kategeori

	class Meta:
		verbose_name = "Kategori Tidak Aktif"
		verbose_name_plural = "Kategori Tidak Aktif"

class JenisStatusHubungan(models.Model):
	nama_jenis_status_hubungan = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.nama_jenis_status_hubungan

	def get_nama(self):
		return self.nama_jenis_status_hubungan

	class Meta:
		verbose_name = "Jenis Status Hubungan"
		verbose_name_plural = "Jenis Status Hubungan"

class Warga(Account):
	# jenis_identitas = models.ForeignKey(JenisIdentitas,on_delete=models.CASCADE)
	jenis_pekerjaan = models.ForeignKey(JenisPekerjaan,verbose_name='Jenis Pekerjaan',on_delete=models.CASCADE,blank=True,null=True)
	kwarganegaraan = models.PositiveIntegerField(choices=KWARGANEGARAAN,default=1,blank=True,null=True)
	nama_ayah = models.CharField(max_length=255,blank=True,null=True)
	nama_ibu = models.CharField(max_length=255,blank=True,null=True)
	alamat = models.TextField(blank=True,null=True,help_text="di isi dengan alamat domisili sekarang")
	lt = models.CharField(max_length=255,blank=True,null=True)
	lg = models.CharField(max_length=255,blank=True,null=True)
	kategori_tidak_aktif = models.ForeignKey(KategoriTidakAktif,blank=True,null=True,on_delete=models.CASCADE)
	keterangan = models.TextField(blank=True,null=True)
	
	class Meta:
		verbose_name = "Warga"
		verbose_name_plural = "Warga"

class WargaSementara(Warga):
	asal_daerah = models.CharField(max_length=255,help_text="Isi Nama Kota/Kabupaten asal")
	asal_alamat = models.TextField()
	tanggal_datang = models.DateField()
	tanggal_keluar = models.DateField(blank=True,null=True)

	def lama_tinggal(self,mode='hari'):
		tanggal_datang = self.tanggal_datang
		if self.tanggal_keluar:
			tanggal_keluar = self.tanggal_keluar
		else:
			tanggal_keluar = datetime.now().date()

		total = (tanggal_keluar - tanggal_datang)
		if mode == 'hari':
			return "{} Hari".format(total.days)
		return str(total)

	class Meta:
		verbose_name = "Warga Sementara"
		verbose_name_plural = "Warga Sementara"


class RiwayatStatusHubungan(models.Model):
	warga = models.ForeignKey(Warga,on_delete=models.CASCADE)
	jenis_status_hubungan = models.ForeignKey(JenisStatusHubungan,on_delete=models.CASCADE)
	tmt_tanggal = models.DateField()
	keterangan = models.TextField(blank=True,null=True)


	def __str__(self):
		return "[{}] {}".format(str(self.jenis_status_hubungan),str(self.warga))

	class Meta:
		verbose_name = "Riwayat Status Hubungan"
		verbose_name_plural = "Riwayat Status Hubungan"


class NomorIdentitas(models.Model):
	warga = models.ForeignKey(Warga,on_delete=models.CASCADE)
	jenis_identitas = models.ForeignKey(JenisIdentitas,on_delete=models.CASCADE)
	nomor_identitas = models.CharField(max_length=255)

	def __str__(self):
		return "[{}] {}".format(str(self.warga))

	class Meta:
		verbose_name = "Nomor Identitas"
		verbose_name_plural = "Nomor Identitas"

def user_directory_path(instance, filename):
	return "berkas/surat_pengantar/%Y/%m/%d/{}_%d%m%d%H%i.pdf".format(str(instance.warga))

class SuratPengantar(models.Model):
	nomor_surat = models.CharField(max_length=255,blank=True,null=True)
	warga = models.ForeignKey(Warga,on_delete=models.CASCADE)
	keperluan = models.TextField()
	tanggal = models.DateField()
	file_cetak = models.FileField(upload_to=user_directory_path,blank=True,null=True)
	body_cetak = models.TextField(blank=True,null=True)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE,related_name="surat_pengantar_dibuat_oleh")

	def __str__(self):
		return "Surat Pengantar {}".format(self.warga)

	def save(self,*args,**kwargs):
		if not self.id:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		return super(SuratPengantar,self).save()


	class Meta:
		verbose_name = 'Surat Pengantar'
		verbose_name_plural = "Surat Pengantar"
