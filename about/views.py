from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import Contact

# Create your views here.

def about(request):
	if request.method == "POST":
		form = Contact(request.POST)
		if form.is_valid():
			send_mail("User: "+form.cleaned_data["name"],form.cleaned_data["information"],"adityachandla@gmail.com",
				["khuranaprakriti@gmail.com"])
		messages.info(request,"Mail is on it's way")
		return redirect('about')
	else:
		form = Contact()
	return render(request,"about/about.html",{"form":form})
