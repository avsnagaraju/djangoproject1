from django.shortcuts import render,redirect
from django.http import HttpResponse
#from DjProject.forms import Usregis,Upd,Pad,MblForm
from DjProject.forms import Usregis,Upd,Pad
from DjangoProject import settings 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from DjProject.models import Exfd
#from DjProject.models import Exfd,Mobile



# Create your views here.

def home(request):
	#return HttpResponse("hi welcome")
    return render(request,'sa/home.html')

def about(request):
	return render(request,'sa/about.html')

def contact(request):
	return render(request,'sa/contact.html')

def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			# print(rc)
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
			# print(p.username,p.email)
	y = Usregis()
	return render(request,'sa/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'sa/dashboard.html')

@login_required
def prfle(request):
	return render(request,'sa/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'sa/updateprofile.html',{'r':p,'q':t}) 
	
@login_required
def ct(request):
	return render(request,'sa/cart.html')

#@login_required
def tku(request):
	return render(request,'sa/tq.html')

#@login_required
def ipinfo(request):
	return render(request,'sa/iphoneinfo.html')


#@login_required
#def ph(request):
#	p = Mobile.objects.filter(m_id=request.user.id)
#	return render(request,'sa/mobile.html',{'y':p})

#def cmb(request):
#	if request.method == "POST":
#		m = Mobile.objects.filter(m_id=request.user.id,date=request.POST['date'])
#		if len(m)==0:
#			r = MblForm(request.POST)
#			if r.is_valid():
#				t = r.save(commit=False)
#				t.m_id = request.user.id
#				t.save()
#				messages.success(request,"Successfully Completed Booking Mobile")
#				return redirect('/pl')
#		messages.info(request,"Sorry you have already Completed  for today")
#		return redirect('/ml')
#	r = MblForm()
#	return render(request,'sa/cmb.html',{'d':r})