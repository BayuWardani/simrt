from django.contrib import admin

from kependudukan.models import *

from kependudukan._admin._warga_admin import WargaAdmin,WargaSementaraAdmin,SuratPengantarAdmin


class JenisIdentitasAdmin(admin.ModelAdmin):
	list_display = ("nama","keterangan",)
	search_fields = ("nama_jenis_identitas",)


	def nama(self,obj):
		return obj.get_nama()

class JenisPekerjaanAdmin(admin.ModelAdmin):
	list_display = ("nama","keterangan",)
	search_fields = ("nama_jenis_pekerjaan",)

	def nama(self,obj):
		return obj.get_nama()

class JenisStatusHubunganAdmin(admin.ModelAdmin):
	list_display = ("nama","keterangan",)
	search_fields = ("nama_jenis_status_hubungan",)

	def nama(self,obj):
		return obj.get_nama()

admin.site.register(JenisIdentitas,JenisIdentitasAdmin)
admin.site.register(JenisPekerjaan,JenisPekerjaanAdmin)
admin.site.register(JenisStatusHubungan,JenisStatusHubunganAdmin)
admin.site.register(Warga,WargaAdmin)
admin.site.register(WargaSementara,WargaSementaraAdmin)
admin.site.register(SuratPengantar,SuratPengantarAdmin)
