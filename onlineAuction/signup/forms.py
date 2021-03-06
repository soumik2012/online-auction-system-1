from django import forms
from captcha.fields import CaptchaField
from .models import *
class UserForm(forms.ModelForm):#user form pre build class
    password = forms.CharField(widget=forms.PasswordInput,min_length=6)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'onkeypress':'checkEmail(this)','onkeyup':'checkEmail(this)'}))
    captcha=CaptchaField(output_format= u'%(hidden_field)s%(image)s%(text_field)s')
    userName=forms.CharField(label="Username:",widget=forms.widgets.TextInput(attrs={'onkeypress':'checkUserName(this)','onkeyup':'checkUserName(this)'}))
    Choices=(('Book','Book'),('Vehicle','Vehicle'),('Coin or Stamp','Coin or Stamp'),('Antique','Antique'),
             ('Electronics','Electronics'),('Others','Others'))
    interests=forms.ChoiceField(choices=Choices, label = "Interest:")
    class Meta:
    	model = UserDetail
    	fields = '__all__'



class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)

class VisaForm(forms.Form):#user form pre build class
	visaNum = forms.CharField(max_length = 10,label="Visa Number")
	expDate= forms.DateTimeField(label="Expiry Date:",widget=forms.DateTimeInput(attrs={'placeholder':'YYYY-MM-DD', 'type' : 'date'}))
class PassRecoverForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'onkeypress':'checkEmail(this)','onkeyup':'checkEmail(this)'}))
class PassChangeForm(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput(),label="Enter New Password:",min_length=6)

