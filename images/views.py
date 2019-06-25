from django.shortcuts import render,redirect
from .models import ImageModel, LikesModel, CommentsModel
from .forms import CommentForm
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def home(request):
	images = ImageModel.objects.all()
	return render(request,'images/home.html',{"images":images})


def image(request,pk):
	im = ImageModel.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid() and not_commented(request,im):
			comm = CommentsModel(person=get_client_ip(request),name=form.cleaned_data['name'],
				comment=form.cleaned_data['comment'],image=im)
			comm.save()
		messages.info(request,"You have already commented")
		print("message posted")
	form = CommentForm()
	comments = im.commentsmodel_set.all()
	return render(request,'images/image.html',{"im":im, "form":form, "comments":comments})


def putLike(request,pk):
	im = ImageModel.objects.get(pk=pk)
	ip = get_client_ip(request)
	temp =  LikesModel.objects.filter(image=im).filter(person=ip)
	response = dict()
	if temp:
		response["success"] = False
	else:
		response["success"] = True
		im.num_likes += 1
		im.save()
		entry = LikesModel(image=im,person=ip)
		entry.save()
	return JsonResponse(response)


def get_client_ip(request):
	##this is for proxy, check weather it's first or last
	if request.META.get("HTTP_X_FORWARDED_FOR"):
		return request.META.get("HTTP_X_FORWARDED_FOR")[0]
	##this is for remote address
	else:
		return request.META.get("REMOTE_ADDR")

def not_commented(request,im):
	comments = CommentsModel.objects.filter(person=get_client_ip(request)).filter(image=im)
	if comments:
		return False
	return True
