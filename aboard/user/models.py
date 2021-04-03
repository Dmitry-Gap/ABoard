import os 
import traceback
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
# from  PIL import Image



# class  DelManage(models.Manager):
#     def delete(self):
#         for el in self:
#             el.delete()

class User(AbstractUser):
    def path_upload(self, filename):
        type_file = "." + filename.split(".")[-1]
        return os.path.join(
            "users",
            "avatars",
            self.username + type_file,
        )

    phone = models.CharField(
        null=True,
        max_length=20,
        verbose_name="User phone number.",
    )
    sex = models.CharField(
        null=True,
        max_length=1,
        verbose_name="Sex.",
    )
    # avatar = models.ImageField(
    #     upload_to=path_upload,
    #     verbose_name="Avatar",
    #     null=True,
    # )
    
    # objects = DelManage()
    
    def __str__(self):
        return self.username
    
    # def delete(self):
    #     try:
    #         os.unlink(os.path.abspath(self.avatar))
    #     except Exception as error:
    #         traceback.print_exc()
    #     return super().delete()

    # @receiver(pre_delete, sender=User)
    # def clean_avatar(sender, instance, **kwargs):
    #     instance.file.delete(False)

    # @receiver(post_save, sender=User)
    # def process_img(sender, instance, **kwargs):
    #     img_path = os.path.join(settings.MEDIA_ROOT.path)
    #     image = Image.open(img_path)
    #     image.show()
