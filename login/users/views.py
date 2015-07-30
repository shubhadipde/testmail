from django.shortcuts import render, render_to_response
from users.models import UserInfo, EmailApp
from .forms import RegisterForm, SendEmailForm, SignInForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView, FormView, ListView



# Create your views here.



class Register(FormView):
	template_name = 'users/registration.html'
	success_url = 'regc'
	form_class = RegisterForm



class Login(FormView):
	template_name = 'users/index.html'
	success_url = 'inbox'
	form_class = SignInForm

	def form_valid(self, form):
		self.request.session['email'] = self.request.POST.get('email')
		return super(Login, self).form_valid(form)



class SendMail(FormView):
	template_name = 'users/send_mail.html'
	form_class = SendEmailForm
	success_url = 'sent'

	def form_valid(self, form):
		t = self.request.POST.get('to')
		userinfo = UserInfo.objects.get(email = t)
		fm = UserInfo.objects.get(email = self.request.session.get('email'))
		sub = self.request.POST.get('subject')
		msg = self.request.POST.get('message')
		EmailApp.objects.create(to=userinfo,frm=fm, body=self.request.POST.get('message'))
		send_mail(sub, msg, self.request.session['email'], [t], fail_silently=False)
		return super(SendMail, self).form_valid(form)



class MailListView(ListView):
	model = EmailApp
	context_object_name = 'messages'



class Inbox(MailListView):
	template_name = 'users/inbox.html'

	def get_queryset(self):
		qs = super(Inbox, self).get_queryset()
		user_id = UserInfo.objects.get(email = self.request.session.get('email'))
		return qs.filter(to = user_id)



class SentMail(MailListView):
	template_name = 'users/sent_mail.html'

	def get_queryset(self):
		qs = super(SentMail, self).get_queryset()
		user_id = UserInfo.objects.get(email = self.request.session.get('email'))
		return qs.filter(frm = user_id)




'''
def regester(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST, request.FILES)
		if form.is_valid():

			return render(request, 'users/reg_compt.html', {'form':form})
	else:
		form = RegisterForm()
		return render(request, 'users/registration.html', {'form':form})

	return render(request, 'users/registration.html', {'form':form})
'''



'''
def reg_compt(request):
	return render(request, 'users/reg_compt.html')
	'''


'''
def index(request):
    return render(request, 'users/index.html')
    
    
def login(request):
    uname = request.POST.get('email')
    pwd = request.POST.get('password')
    q = UserInfo.objects.get(email = uname)
    if pwd == q.password:
    	#user = authenticate(username = uname, password = pwd)
    	#if user is not None:
    		#if user.is_active:
    			#login(request, user)
    	request.session['email'] = uname
    	user_id = UserInfo.objects.get(email = uname).id
    	messages = EmailApp.objects.filter(to = user_id)
    	return render(request, 'users/inbox.html', {'messages':messages})
        	#else:
        		#return render(request, 'users/index.html')
    else:
        return render(request, 'users/index.html')
        '''

'''
class Login(TemplateView):

	def post(self,request):
		# business logic here ..
		return render(request, 'users/home.html')
'''

'''
def sendmail(request):
	print request.user
	print request.session.get('email')
	if request.method == 'POST':
		form = SendEmailForm(request.POST)
		if form.is_valid():
			#userinfo = UserInfo.objects.filter(email=request.POST.get('to'))
			userinfo = UserInfo.objects.get(email=request.POST.get('to'))
			t = request.POST.get('to')
			#fm = request.user.email
			#fm = UserInfo.objects.filter(email=request.session['email'])
			fm = UserInfo.objects.get(email=request.session.get('email'))
			sub = request.POST.get('subject')
			msg = request.POST.get('message')

			EmailApp.objects.create(to=userinfo,frm=fm, body=request.POST.get('message'))
			send_mail(sub, msg, request.session['email'], [t], fail_silently=False)
			return render(request, 'users/mail_sent.html')
	else:
		form = SendEmailForm()
	return render(request, 'users/send_mail.html', {'form':form})
'''


'''
def inbox(request):
	try:
		user_id = UserInfo.objects.get(email = request.session.get('email'))
	except Exception as e:
		print "Inbox exception is " + str(e)
		user_id = ""
	messages = EmailApp.objects.filter(to = user_id)
	return render(request, 'users/inbox.html', {'messages':messages})
	'''


'''
def sent_mail(request):
	try:
		user_id = UserInfo.objects.get(email = request.session.get('email'))
	except Exception as e:
		print "Send Email exception is " + str(e)
		user_id = ""
	messages = EmailApp.objects.filter(frm = user_id)
	return render(request, 'users/sent_mail.html', {'messages':messages})
	'''
