from django import forms

class PostForm(forms.Form):
	cName = forms.CharField(min_length=1,initial='')
	cUID = forms.CharField(min_length=1,max_length=9,initial='')
	cSex = forms.CharField(max_length=2,initial='')	
	cBirthday = forms.DateField()
	cEmail = forms.EmailField(max_length=100,initial='',required=True)
	cPhone = forms.CharField(min_length=9,max_length=50,initial='',required=True)
	cAddr = forms.CharField(min_length=4,max_length=255,initial='',required=True)