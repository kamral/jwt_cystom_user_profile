from rest_framework import serializers
from  profiles.models import UserProfile
from user.models import User


# мы создаем класс UserSerializer, который расширяет сериализатор.
# Ссылка на класс Meta выполняется во время создания экземпляра
# формы / объекта перед определением самого класса.


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



