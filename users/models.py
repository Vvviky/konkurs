from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='users/', verbose_name= "Аватар")
    firstname = models.CharField(max_length=200, verbose_name= "Имя")
    surname = models.CharField(max_length=200, verbose_name= "Игнатович")
    email = models.EmailField(verbose_name='Электронная почта',
                              unique=True, )
    is_staff = models.BooleanField(
        verbose_name='Доступ к панели адмнистратора',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='активен',
        default=True,
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name= "Аватар"
        verbose_name= "Имя"
        verbose_name= "Игнатович"
        verbose_name= "Электронная почта"
        verbose_name= "Пользователь"
        verbose_name_plural= "Пользователи"
        