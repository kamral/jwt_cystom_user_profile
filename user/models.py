from django.db import models
# uuid - это 128-битное число, представленное
# как строка utf8 из пяти шестнадцатеричных чисел.
import uuid
# Create your models here.
# AbstractBaseUser импортируется для настройки пользовательской
# модели пользователя, а BaseUserManager используется,
# когда необходимо определить настраиваемый менеджер,
# т.е. если мы хотим определить поля, отличные от UserManger,
# нам нужно определить настраиваемый менеджер,
# который расширяет BaseUserManager.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# мы создаем настраиваемый пользовательский менеджер,
# расширяя BaseUserManager и предоставляя два дополнительных метода:
# create_user () и create_superuser ()
# create_user () и create_superuser () должны принимать поле имени пользователя
# и другие обязательные поля в качестве аргументов.



class UserManager(BaseUserManager):

    def create_user(self,email,password=None):

        if not email:
            raise ValueError('User must be have an email')

        user=self.model(
            # self.normalize_email (email) нормализует адрес
            # электронной почты, уменьшая регистр доменной части.
            email=self.normalize_email(email),
        )
        # set_password (пароль) сохраняет пароль и сохраняет хеш в базе данных.
        user.set_password(password)
        # user.save (using = self._db) сохраняет пользователя
        # в текущей базе данных (self._db)
        # наконец, этот метод возвращает пользователя, если он
        # был успешно сохранен, в противном случае возникает ошибка.
        user.save(using=self._db)
        return user

    # create_superuser () сохраняет пользователя с правами
    # администратора, которые достигаются
    # включением is_superuser = True и is_staff = True.
    def create_superuser(self, email,password):

        if password is None:
            raise  TypeError('Superusers must  have a password')

        user=self.create_user(email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()

        return  user

# класс User расширяет AbstractBaseUser
# для создания пользователя с настраиваемыми полями.

class User(AbstractBaseUser):
    # Поле id используется для хранения первичного ключа в формате uuid.
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # В поле электронной почты хранится электронная почта.
    email=models.EmailField(verbose_name='email_address',
                            max_length=100,
                            unique=True)
    # По умолчанию новый пользователь всегда должен быть активен.
    # Пользователь может не быть администратором или сотрудником,
    # поэтому я установил для него значение по умолчанию как False.
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    # USERNAME_FIELD настроен на адрес электронной почты, поскольку он должен
    # использоваться в качестве имени пользователя при входе в систему.
    USERNAME_FIELD='email'
    # REQUIRED_FIELDS содержит список обязательных полей, но в нашем случае он пуст.
    REQUIRED_FIELDS = []

    objects=UserManager()

    def __str__(self):
        return self.email


    class Meta:

        db_table='login'



