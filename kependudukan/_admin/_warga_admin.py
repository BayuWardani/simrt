from django.contrib import admin


from kependudukan.models import RiwayatStatusHubungan

from kependudukan._forms._warga_forms import (FormWarga,FormWargaSementara)

class RiwayatStatusHubunganInline(admin.StackedInline):
	model = RiwayatStatusHubungan
	extra = 1

class WargaAdmin(admin.ModelAdmin):
	list_display = ('Nik','nama_lengkap','jenis_kelamin','agama','usia','kwarganegaraan')
	list_filter = ('jenis_kelamin','agama',)
	search_fields = ('username','nama_lengkap','tempat_lahir','kwarganegaraan','jenis_pekerjaan__nama_jenis_pekerjaan',)
	form = FormWarga
	inlines = [
		RiwayatStatusHubunganInline
	]

	def Nik(self,obj=None):
		if obj.username:
			return obj.username
		return "-"

	def usia(self,obj=None):
		return obj.get_usia()


class WargaSementaraAdmin(admin.ModelAdmin):
	list_display = ('Nik','nama_lengkap','jenis_kelamin','agama','usia','asal_daerah','tanggal_datang','kwarganegaraan',)
	list_filter = ('jenis_kelamin','agama',)
	search_fields = ('username','nama_lengkap','tempat_lahir','kwarganegaraan','jenis_pekerjaan__nama_jenis_pekerjaan',)
	form = FormWargaSementara
	inlines = [
		RiwayatStatusHubunganInline
	]

	def Nik(self,obj=None):
		if obj.username:
			return obj.username
		return "-"

	def usia(self,obj=None):
		return obj.get_usia()


class SuratPengantarAdmin(admin.ModelAdmin):
	list_display = ("warga","keperluan","tanggal","created_by")
	search_fields = ("warga__username","warga__nama_lengkap","keperluan",)

	fieldsets = (
		(None,{
			'fields':("warga","keperluan","tanggal")
			}),
		)
	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		return super(SuratPengantarAdmin,self).save_model(request,obj,form,change)
