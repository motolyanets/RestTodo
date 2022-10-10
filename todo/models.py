from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField("Email", unique=True, max_length=256, blank=False)
    name = models.CharField(max_length=40, db_index=True, default='A', blank=False)
    surname = models.CharField(max_length=40, db_index=True, default='M', blank=False)
    is_staff = models.BooleanField("Is staff", default=False)
    is_active = models.BooleanField("Is active", default=True)
    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        app_label = "todo"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.pk}: {self.email}"

    def has_module_perms(self, app_label):
        return self.is_staff and self.is_active

    def has_perm(self, perm_list, obj=None):
        return self.is_staff and self.is_active


class Article(models.Model):
    content = models.TextField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey('MyUser', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.content


# class Executors(models.Model):
#     name = models.CharField(max_length=40, db_index=True)
#
#     class Meta:
#         verbose_name = 'Исполнитель'
#         verbose_name_plural = 'Исполнители'
#
#     def __str__(self):
#         return self.name
