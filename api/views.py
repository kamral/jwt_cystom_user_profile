from django.shortcuts import render

# Create your views here.
# выдает статус кода()
from rest_framework import status
# создание аpi
from rest_framework.generics import CreateAPIView
# отправляет ответ
from rest_framework.response import Response
# разрешение всем
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserLoginSerializer


from rest_framework.generics import RetrieveAPIView

# создание представления путем расширения CreateAPIView.
class UserRegistrationView(CreateAPIView):
    # Serializer_class сообщает, какой сериализатор использовать,
    serializer_class = UserRegistrationSerializer
    # а permission_classes определяет, кто может получить доступ к API.
    permission_classes = (AllowAny,)

    def post(self, request):
        # Разрешить любому пользователю
        # (аутентифицированному или нет) подключаться к этой конечной точке.
        # восстановить эти собственные типы данных в словарь проверенных данных.
        serializer = self.serializer_class(data=request.data)
        # проверяет, соответствуют ли данные полям сериализатора,
        # в противном случае выдается исключение.
        serializer.is_valid(raise_exception=True)
        # чтобы вернуть экземпляр объекта на основе проверенных данных.
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


#
# RetrieveAPIView
# Используется для создания неизменяемых конечных точек для экземпляра одной модели.
# Предоставляет: обработчик метода get.
# Расширяет: GenericAPIView, RetrieveModelMixin

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self,request):
        # Разрешить любому пользователю
        # (аутентифицированному или нет) подключаться к этой конечной точке.
        # восстановить эти собственные типы данных в словарь проверенных данных.
        serializer=self.serializer_class(data=request.data)
        # проверяет, соответствуют ли данные полям сериализатора,
        # в противном случае выдается исключение.
        serializer.is_valid(raise_exception=True)
        # в случае успешной авторизации
        response={
            'success':'True',
            'status_code':status.HTTP_200_OK,
            'message':'Ваш логин успешно зарегистрирован',
            # формируем токен
            'token':serializer.data['token']
        }
        status_code=status.HTTP_200_OK
        # возвращаем ответ
        return Response(response, status=status_code)



