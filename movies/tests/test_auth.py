import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_register_user(client):
    url = reverse('register')
    response = client.post(url, {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'Testpass123!',
        'password2': 'Testpass123!'
    })
    if response.status_code == 200:
        print("Form errors:", response.context['form'].errors)
    assert response.status_code in [200, 302]
    assert User.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_login_user(client):
    User.objects.create_user(username='testuser', password='Testpass123!')
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'Testpass123!'
    })
    assert response.status_code == 302
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_protected_view_requires_login(client):
    # Используем защищённую админку
    response = client.get('/admin/')
    assert response.status_code == 302  # редирект на login

@pytest.mark.django_db
def test_logout_user(client):
    User.objects.create_user(username='logoutuser', password='Testpass123!')
    client.login(username='logoutuser', password='Testpass123!')
    response = client.post(reverse('logout'))
    assert response.status_code in [200, 302]
