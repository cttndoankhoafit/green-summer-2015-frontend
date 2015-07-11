# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class DashboardView(TemplateView):
	template_name = 'adm/base.html'

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)

		context['title'] = u'Bảng điều khiển'
		context['page_title'] = u'Bảng điều khiển'

		return context