# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class LoginView(TemplateView):
	template_name = 'v1/login.html'

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)

		context['title'] = u'Đăng nhập'
		
		return context

class DashboardView(TemplateView):
	template_name = 'v1/admin_base.html'

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)

		context['title'] = u'Bảng điều khiển'
		context['page_title'] = u'Bảng điều khiển'

		return context