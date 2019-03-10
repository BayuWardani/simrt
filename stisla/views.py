from django.shortcuts import render
from django.views.generic import TemplateView
from kependudukan.models import Warga,SuratPengantar
# Create your views here.

class Home(TemplateView):
	template_name = 'admin/home.html'
	
	warga = Warga.objects.filter(wargasementara__isnull=True)
	warga_sementara = Warga.objects.filter(wargasementara__isnull=False)

	jumlah_warga = 0
	jumlah_wargasementara = 0
	jumlah_perempuan = 0
	jumlah_laki_laki = 0
	jumlah_perempuan_sementara = 0
	jumlah_laki_laki_sementara = 0

	if warga:
		jumlah_warga = warga.count()
		jumlah_perempuan = warga.filter(jenis_kelamin='P').count()
		jumlah_laki_laki = warga.filter(jenis_kelamin='L').count()

	if warga_sementara:
		jumlah_wargasementara = warga_sementara.count()
		jumlah_perempuan_sementara = warga_sementara.filter(jenis_kelamin='P').count()
		jumlah_laki_laki_sementara = warga_sementara.filter(jenis_kelamin='L').count()

	month_lst = [
		(1,'January'), 
		(2,'February'), 
		(3,'March'), 
		(4,'April'), 
		(5,'May'), 
		(6,'June'), 
		(7,'July'),
		(8,'August'), 
		(9,'September'), 
		(10,'October'), 
		(11,'November'), 
		(12,'December')
	]

	statistik_data = []

	surat_pengantars = SuratPengantar.objects.all()

	# if surat_pengantars:
	for x,y in month_lst:
		bulan_ini = 0
		if surat_pengantars:
			bulan_ini = surat_pengantars.filter(tanggal__month=x).count()
		statistik_data.append(bulan_ini)

	extra_context = {
		"title":"Beranda",
		"jumlah_warga":jumlah_warga,
		"jumlah_wargasementara":jumlah_wargasementara,
		"jumlah_perempuan":jumlah_perempuan+jumlah_perempuan_sementara,
		"jumlah_laki_laki":jumlah_laki_laki+jumlah_laki_laki_sementara,
		"month_lst":month_lst,
		"statistik_data":statistik_data
		# "jumlah_perempuan_sementara":jumlah_perempuan_sementara,
		# "jumlah_laki_laki_sementara":jumlah_laki_laki_sementara
	}

	print (extra_context)