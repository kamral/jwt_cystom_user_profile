from rest_framework import serializers
from  profiles.models import UserProfile
from user.models import User


from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from user.models import User


# JWT_PAYLOAD_HANDLER: данные, которые мы хотим передать как полезную нагрузку.
JWT_PAYLOAD_HANDLER=api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER: полезная нагрузка, которую мы хотим кодировать.
JWT_ENCODE_HANDLER=api_settings.JWT_PAYLOAD_HANDLER


# мы создаем класс UserSerializer, который расширяет сериализатор.
# Ссылка на класс Meta выполняется во время создания экземпляра
# формы / объекта перед определением самого класса.

# Сериализатор Django rest framework - это обычный сериализатор,
# который будет использоваться при создании API с Django.
# Он просто анализирует данные сложных типов в JSON или XML.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Указывает, какая модель будет использоваться.
        model=UserProfile
        # Сообщает поля, которые будут использоваться сериализатором.
        # Если мы хотим включить все поля модели, мы можем просто использовать.
        fields=('first_name','last_name','phone_number','age','gender')

# сериализатор для регистрации пользователя
# с помощью вложенного объекта профиля.
# Пароль был установлен только для чтения.
class UserRegistrationSerializer(serializers.ModelSerializer):

    profile=UserSerializer(required=True)

    class Meta:
        model=User
        fields=('email','password','profile')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        profile_data=validated_data.pop('profile')
        user=User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )

        return user



# Сериализатор модели аналогичен описанному выше сериализатору в том смысле,
# что он выполняет ту же работу, только создает сериализатор на основе модели,
# что упрощает создание сериализатора по сравнению с его обычным построением.

# Мы написали собственный метод проверки для проверки пользователя и возврата токена.
# Authenticate используется для аутентификации пользователя,
# то есть проверки учетных данных пользователя.
# Если пользователь не аутентифицирован или не существует, возникает ошибка.
# Если пользователь аутентифицирован, пользователь передается
# в качестве полезной нагрузки JWT_PAYLOAD_HANDLER,
# а затем токен генерируется путем кодирования полезной нагрузки,
# которая передается в качестве аргумента JWT_ENCODE_HANDLER.

class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255, write_only=True)
    token=serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email=data.get("email",None)
        password=data.get("password",None)
        user=authenticate(email=email,password=password)
        if user is None:
            raise serializers.ValidationError(
                'Если пользовательне нашел email и password'
            )
        try:
            # JWT_PAYLOAD_HANDLER: данные, которые мы хотим передать как полезную нагрузку.
            # Если пользователь аутентифицирован, пользователь передается
            # в качестве полезной нагрузки JWT_PAYLOAD_HANDLER
            payload=JWT_PAYLOAD_HANDLER(user)
            # затем токен генерируется путем кодирования полезной нагрузки,
            # которая передается в качестве аргумента JWT_ENCODE_HANDLER.
            jwt_token=JWT_ENCODE_HANDLER(payload)
            update_last_login(None,user)
        except User.DoesNotExist:
            raise  serializers.ValidationError(
                'Пользователь отправляет почту и пароль . Он не должен быть пустым'
            )
        return {
            'email':user.email,
            'token':jwt_token
        }