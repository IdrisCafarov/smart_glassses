from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.translation import gettext_lazy as _
from .helper import *
from .options import USERTYPE, DISEASES
import random
# from django.contrib.auth import get_user_model

# User = get_user_model()
# from product.helper import seo
# from accounts.options import USERTYPE
# from phone_field import PhoneField
USER_MODEL = settings.AUTH_USER_MODEL








class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), null=True, max_length=100, unique=False)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, )
    company_name = models.CharField(_('company name'), max_length=50, blank=True)
    # phone_number = PhoneField(_("phone number"), blank=True, null=True)
    birthday = models.DateField(_("birth date"), blank=True, null=True)
    usertype = models.IntegerField(verbose_name="Gender",choices=USERTYPE,null=True,blank=True,default=1)
    adress = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    ########### Custom #######################

    created_date = models.DateTimeField(auto_now_add=True,null=True)
    ##############################################

    image = models.FileField(_("image"),null=True,blank=True,upload_to="user_pp")

    video = models.FileField(_("video"),null=True,blank=True,upload_to="user_video")

    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    email = models.EmailField(_('email address'), unique=True, max_length=255, blank=False)

    slug = models.SlugField(unique=True, editable=False, null=True)


    is_admin = models.BooleanField(_('user admin'), default=False)

    is_user = models.BooleanField(_('user user'), default=False)




    # is_pro = models.BooleanField(_('pro seller'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        managed = True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    # def save(self, *args, **kwargs):
    #     super(MyUser, self).save(*args, **kwargs)
        # self.slug = "{}.{}".format(seo(self.first_name + "-" + self.last_name), self.id)
        # super(MyUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        self.slug = seo(self.first_name)+str(random.randrange(99999999,9999999999))+seo(self.last_name)
        super(MyUser, self).save(*args, **kwargs)

    # def get_avatar(self):
    #     if self.image:
    #         return self.image.url
    #     elif self.usertype == 1:
    #         return "/static/img/man_avatar.png"
    #     elif self.usertype == 2:
    #         return "/static/img/woman_avatar.jpg"


# class GuideImage(models.Model):
#     image = models.ImageField(upload_to="Guide Images")
#     user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="images")





class Disease(models.Model):
    name = models.CharField(max_length=50,verbose_name="Choose your Diseases", null=True)

    def __str__(self):
        return str(self.name)


class UserDisease(models.Model):
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE, related_name="user_disease",null=True)
    description = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="user_disease",null=True)





class CallHelp(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,limit_choices_to={'is_user': True},)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    place = models.TextField()
    condition = models.TextField(null=True)
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email

