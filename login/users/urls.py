from django.conf.urls import url
from django.views.generic import TemplateView
from .views import Login, Register, SendMail, Inbox, SentMail


from . import views

urlpatterns = [
	#url(r'^sentmail$', views.sent_mail, name='sentmail'),
	url(r'^sentmail$', SentMail.as_view(), name='sentmail'),
	#url(r'^inbox$', views.inbox, name='inbox'),
	url(r'^inbox$', Inbox.as_view(), name='inbox'),
	url(r'^sent$', TemplateView.as_view(template_name='users/mail_sent.html'), name='sent'),
	#url(r'^sendmail$', views.sendmail, name='send_mail'),
	url(r'^sendmail$', SendMail.as_view(), name='send_mail'),
	#url(r'^regc$', views.reg_compt, name='register_compt'),
	url(r'^regc$', TemplateView.as_view(template_name='users/reg_compt.html'), name='register_compt'),
    #url(r'^reg$', views.regester, name='register'),
    url(r'^reg$', Register.as_view(), name='register'),
    #url(r'^$', views.index, name='index'),
    #url(r'^$', TemplateView.as_view(template_name='users/index.html'), name='index'),
    #url(r'^home$', views.login, name='login')
    url(r'^$', Login.as_view(), name='login')

]