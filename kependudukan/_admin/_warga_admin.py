from django.contrib import admin,messages
from django.utils.html import mark_safe
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.template import loader

from kependudukan.models import RiwayatStatusHubungan,SuratPengantar
from master.models import KonfigurasiSistem

from kependudukan._forms._warga_forms import (FormWarga,FormWargaSementara)

from datetime import datetime

# library
from weasyprint import HTML

IS_POPUP_VAR = '_popup'

def Warga_Sementara_Keluar(modeladmin,request,queryset):
	queryset.update(tanggal_keluar=datetime.today())
	messages.success(request,'{} Warga Sementara Keluar Pada Tanggal {}'.format(queryset.count(),datetime.today()))

class RiwayatStatusHubunganInline(admin.StackedInline):
	model = RiwayatStatusHubungan
	extra = 1

class WargaAdmin(admin.ModelAdmin):
	list_display = ('Nik','nama_lengkap','jenis_kelamin','agama','usia','kwarganegaraan')
	list_filter = ('jenis_kelamin','agama',)
	search_fields = ('username','nama_lengkap','tempat_lahir','kwarganegaraan','jenis_pekerjaan__nama_jenis_pekerjaan',)
	form = FormWarga
	# inlines = [
	# 	RiwayatStatusHubunganInline
	# ]

	def Nik(self,obj=None):
		if obj.username:
			return obj.username
		return "-"

	def usia(self,obj=None):
		return obj.get_usia()


	def get_queryset(self,request):
		qs = super(WargaAdmin,self).get_queryset(request)
		qs = qs.filter(wargasementara__isnull=True)
		return qs


class WargaSementaraAdmin(admin.ModelAdmin):
	list_display = ('Nik','nama_lengkap','jenis_kelamin','usia','asal_daerah','tanggal_datang','tanggal_keluar','lama_tinggal',)
	list_filter = ('jenis_kelamin','agama',)
	search_fields = ('username','nama_lengkap','tempat_lahir','kwarganegaraan','jenis_pekerjaan__nama_jenis_pekerjaan',)
	form = FormWargaSementara
	# inlines = [
	# 	RiwayatStatusHubunganInline
	# ]
	actions = [Warga_Sementara_Keluar]

	def Nik(self,obj=None):
		if obj.username:
			return obj.username
		return "-"

	def usia(self,obj=None):
		return obj.get_usia()

	def lama_tinggal(self,obj=None):
		return obj.lama_tinggal()


class SuratPengantarAdmin(admin.ModelAdmin):
	list_display = ("nomor_surat","warga","keperluan","tanggal","created_by","aksi")
	search_fields = ("warga__username","warga__nama_lengkap","keperluan",)

	fieldsets = (
		(None,{
			'fields':("nomor_surat","warga","keperluan","tanggal")
			}),
		)

	def aksi(self,obj=None):
		btn = "<button onclick='CommandRedirect(this)' type='button' class='btn btn-sm btn-success' data-url='{}' ><i class='fa fa-print'></i> Cetak</button>".format(reverse("admin:kependudukan_suratpengantar_cetak_pdf",args=[obj.id]))

		return mark_safe(btn)

	def response_post_save_add(self, request, obj):
		return HttpResponseRedirect(reverse("admin:kependudukan_suratpengantar_cetak_pdf",args=[obj.id]))

	def cetak_pdf(self,request,object_id):
		pengantar = None
		tanggal_pengantar = None
		sistem = KonfigurasiSistem.get_solo()
		try:
			pengantar = SuratPengantar.objects.get(pk=object_id)
		except SuratPengantar.DoesNotExist:
			messages.warning(request,'Surat Pengantar dengan ID {} tidak dapat ditemukan'.format(object_id))
			return HttpResponseRedirect(reverse("admin:kependudukan_suratpengantar_changelist"))
		except Exception as e:
			print (e)
			raise Http404()
		
		if pengantar:
			tanggal_pengantar = pengantar.tanggal.strftime('%d %B %Y')

		context = {
			# "tanggal_pengantar":pengantar.tanggal,
			"pengantar":pengantar,
			"title":"{} ~ {}".format(pengantar.warga,pengantar.keperluan),
			'sistem':sistem
		}

		# if pengantar.body_cetak:
		# 	print (pengantar.body_cetak)
			# return HttpResponse(pengantar.body_cetak,content_type='application/pdf')

		template_name = 'admin/kependudukan/suratpengantar/cetak/format_1_A4_pdf.html'
		html_template = loader.render_to_string(template_name, context, request, using=None)
		
		pdf_file = HTML(string=html_template).write_pdf()
		# print (dir(pdf_file))
		# pengantar.body_cetak = pdf_file
		# pengantar.save()
		response = HttpResponse(pdf_file,content_type='application/pdf',status=None)
		# print(dir(response))
		# pengantar.body_cetak = response.content
		# pengantar.save()
		# return response
		return render(request,template_name,context)

	# def download_pdf(self,request,object_id):


	def get_urls(self):
		from django.urls import path
		
		urls = super().get_urls()

		info = self.model._meta.app_label, self.model._meta.model_name

		my_urls = [
			path('cetak/<path:object_id>',self.admin_site.admin_view(self.cetak_pdf),name="%s_%s_cetak_pdf" % info)
		]

		return urls+my_urls

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		return super(SuratPengantarAdmin,self).save_model(request,obj,form,change)
