from django.contrib import admin
from .models import ImageModel, LikesModel, CommentsModel
# Register your models here.

admin.site.register(ImageModel)
admin.site.register(LikesModel)
admin.site.register(CommentsModel)
