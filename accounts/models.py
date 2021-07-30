from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is Required')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    object = UserManager()
    user_name = models.CharField(max_length=25)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    super_user = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_superuser(self):
        return self.super_user
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='User')
    address_location = models.CharField(max_length=255)
    is_default = models.BooleanField()

    def __str__(self):
        return f'{self.user_id.email} {self.address_location}'


class Phone(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='User')
    phone_number = models.IntegerField()
    is_default = models.BooleanField()

    def __str__(self):
        return f'{self.user_id.email} {self.phone_number}'