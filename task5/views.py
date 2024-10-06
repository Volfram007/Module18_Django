from django.shortcuts import render
from task5.forms import UserRegister

# Псевдосписок существующих пользователей
users = ['user1', 'user2', 'user3']


# Представление с использованием Django формы
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif len(password or repeat_password)< 8:
                info['error'] = 'Длина пароля должна быть не менее 8 символов'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(username)
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
            return render(request, 'fifth_task/registration_page.html', info)

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


# Представление с использованием данных из HTML формы
def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(username, password, repeat_password, age)
        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif len(password or repeat_password)< 8:
            info['error'] = 'Длина пароля должна быть не менее 8 символов'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            users.append(username)
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)
