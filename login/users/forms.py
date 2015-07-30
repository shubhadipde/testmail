from django import forms
from users.models import UserInfo, EmailApp


class RegisterForm(forms.Form):
	email = forms.CharField(required=True, widget = forms.TextInput())
	password = forms.CharField(required=True, widget = forms.PasswordInput())
	image = forms.ImageField()

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		uname = cleaned_data.get('email')
		pwd = cleaned_data.get('password')
		pic = cleaned_data.get('image')
		q = UserInfo.objects.filter(email = uname)
		if q.count() == 0:
			p = UserInfo(email = uname, password = pwd, picture=pic)
			if uname and pwd and pic:
				p.save()
		else:
			self._errors['email'] = 'email already exists'
			


class SendEmailForm(forms.Form):
	to = forms.CharField(required=True, widget=forms.TextInput())
	subject = forms.CharField(required=True, widget=forms.TextInput())
	message = forms.CharField(required=True, widget=forms.Textarea())

	def clean(self):
		pass
		


class SignInForm(forms.Form):
	email = forms.CharField(required = True, widget = forms.TextInput())
	password = forms.CharField(required = True, widget = forms.PasswordInput())

	def clean(self):
		cleaned_data = super(SignInForm, self).clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		try:
			q = UserInfo.objects.get(email = email)
			if q.password != password:
				self._errors['email'] = 'invalid username or password'
		except Exception as e:
			print 'Exception in signin : ' + str(e)
		

