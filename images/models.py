from django.db import models

# Create your models here.


class ImageModel(models.Model):
	title = models.CharField(max_length=20)
	about = models.CharField(max_length=1024)

	image = models.ImageField(upload_to='paint_folder')

	num_likes = models.IntegerField(default=0)
	date_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
	    ordering = ('-num_likes', )


class LikesModel(models.Model):
	person = models.GenericIPAddressField()
	image = models.ForeignKey(ImageModel, on_delete = models.CASCADE)


class CommentsModel(models.Model):
	person = models.GenericIPAddressField()
	image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
	name = models.CharField(max_length=50,default="anonymous")
	posted_on = models.DateTimeField(auto_now_add=True,null=True)
	comment = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.name+" "+self.comment

	class Meta:
		ordering = ('-posted_on',)



