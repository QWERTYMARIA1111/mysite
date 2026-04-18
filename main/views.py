from django.shortcuts import render
from .models import User  # Предполагаем, что модель User определена в main/models.py

def index(request):
    # Если в GET-запросе есть параметр 'username', добавляем нового пользователя
    if 'username' in request.GET:
        name = request.GET['username']
        # Используем get с значением по умолчанию для пароля
        password = request.GET.get('password', '12345')
        User.objects.create(username=name, password=password)

    # Получаем всех пользователей из базы данных
    users = User.objects.all()

    # Рендерим шаблон index.html, передавая в него список пользователей
    return render(request, 'index.html', {'users': users})



# Create your views here.
