from django.contrib import admin
from accounts._forms._accounts_forms import FormAccount

class AccountAdmin(admin.ModelAdmin):
	list_display = ('username','nama_lengkap','jenis_kelamin','tempat_lahir','tanggal_lahir','agama')
	list_filter = ('jenis_kelamin','agama',)
	search_fields = ('username','nama_lengkap','tempat_lahir',)

	form = FormAccount

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		return super(AccountAdmin,self).save_model(request,obj,form,change)

	def get_queryset(self,request):
		qs = super(AccountAdmin,self).get_queryset(request)
		qs = qs.filter(warga__isnull=True)
		return qs