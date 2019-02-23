from django.template import Library
from django import forms
register = Library()


# @register.tag(name="menu_list")
# def menu_list():
# 	

@register.filter(name='debug')
def debug(params):
	# print(dir(params))
	# print(params.filter_specs)
	return params


# @register.inclusion_tag('admin/custom/filter.html')
# def sirt_list_filter(cl):
# 	

@register.filter(name='field_add_attr')
def field_add_attr(params):
	params.field.widget.attrs.update({'class': 'form-control'})

	return params