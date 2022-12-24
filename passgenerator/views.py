import random
from django.shortcuts import render


# Create homepage view
def home(request):
    """Render the homepage"""
    return render(request, 'passgenerator/home.html')


# Create about view
def about(request):
    """Render the about page"""
    return render(request, 'passgenerator/about.html')


# Create the password generator output page
def password(request):
    """Based on user selection the function will extend the lowercase 
    list to include the list selected by the user"""

    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('QWERTYUIOPLKJHGFDSAZXCVBNM')
    numbers = list('0123456789')
    special = list('!@#$%^&*()')

    # if user selected uppercase, add those to characters
    if request.GET.get('uppercase'):
        characters.extend(uppercase)

    # if user selected special, add those to characters
    if request.GET.get('special'):
        characters.extend(special)

    # if user selected numbers, add those to characters
    if request.GET.get('numbers'):
        characters.extend(numbers)

    # The default length will be set to 12
    length = int(request.GET.get('length', 12))

    the_password = ''

    i = 0
    while i < length:
        the_password += random.choice(characters)
        i += 1

    # for char in range(length):
    #     the_password += random.choice(characters)

    return render(request, 'passgenerator/password.html', {
        'password': the_password
    })
