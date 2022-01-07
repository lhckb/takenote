from django.shortcuts import redirect, render
from core.models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User 

def index(request):
    return render(request, 'index.html')

# present this page for every unfinished feature
@login_required(login_url = '/login/')
def workInProgress(request):
    return render(request, 'wip.html')


@login_required(login_url = '/login/')
def accountPage(request):
    user = User.objects.filter(username = request.user)
    return render(request, 'account.html', {'user':user})


@login_required(login_url = '/login/')
def submitAccountUpdate(request):
    curr_user = request.user
    user = User.objects.filter(username = curr_user)

    if request.POST:

        username = request.POST.get('username')
        if not User.objects.filter(username = username):
            user.username = username
            #user.save()
            messages.success(request, 'Username updated!')

        
        password = request.POST.get('password')
        passw_confirm = request.POST.get('confirmPassw')
        # if password == passw_confirm:
        #     if not User.objects.filter(username = curr_user, password = password):
        #         curr_user.set_password(password = password)
        #         messages.success(request, 'Password updated successfully!')

    return redirect('/account/')


@login_required(login_url = '/login/')
def notesPage(request):
    current_user = request.user
    notes = Note.objects.filter(user = current_user)
    notes = notes.order_by('-date_created')
    return render(request, 'notes.html', {'notes' : notes})


@login_required(login_url = '/login/')
def addNote(request):
    if request.POST:
        title = request.POST.get('title')
        if title != '':
            text = request.POST.get('text')
            user = request.user

            Note.objects.create(title = title, text = text, user = user)

        else:
            messages.error(request, 'Please, add a title to your note.')
            return redirect('/notes/')

    return redirect('/notes/') 


@login_required(login_url = '/login/')
def deleteNote(request, id):
    user = request.user
    note = Note.objects.filter(id = id, user = user)

    if note:
        return redirect('/notes/')

    else:
        return redirect('/notes/')


@login_required(login_url = '/login/')
def updatePage(request, id):
    user = request.user
    note = Note.objects.filter(id = id, user = user)

    if note:
        return render(request, 'update.html', {'note':note})

    else:
        return redirect('/notes/')


@login_required(login_url = '/login/')
def submitUpdate(request, id):
    if request.POST:
        new_title = request.POST.get('title')
        if new_title != '':
            new_text = request.POST.get('text')

            note = Note.objects.filter(id = id)

            note.update(title = new_title)
            note.update(text = new_text)

            return redirect('/notes/')

        else:
            messages.error(request, 'Please, add a title to your note.')
            return redirect(f'/notes/update/{id}')


def loginPage(request):
    return render(request, 'login.html')


def submitLoginIndex(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username and password) != '':
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/notes/')
    
            else:
                messages.error(request, 'Username or password is incorrect. Try again.')
                return redirect('/')

        else:
            messages.error(request, 'Please, fill out fields correctly.')
            return redirect('/')


def submitLoginPage(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username and password) != '':
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/notes/')
    
            else:
                messages.error(request, 'Username or password is incorrect. Try again.')
                return redirect('/login/')

        else:
            messages.error(request, 'Please, fill out fields correctly.')
            return redirect('/login/')



def submitLogout(request):
    logout(request)
    return redirect('/')


def register(request):
    return render(request, 'register.html')


def submitRegisterIndex(request):
    if request.POST:
        username = request.POST.get('username')
        if not User.objects.filter(username = username):
            if username != '':
                password = request.POST.get('password')
                password_confirm = request.POST.get('confirmPassw')

                if password == password_confirm:
                    if password != '':
                        User.objects.create_user(username, '', password)

                    else: 
                        messages.error(request, 'Password field cannot be empty.')
                        return redirect('/')
            
                else:
                    messages.error(request, 'Passwords don\'t match.')
                    return redirect('/')

            else:
                messages.error(request, 'Please, inform an username.')
                return redirect('/')
            
        else:
            messages.error(request, 'Username already exists.')
            return redirect('/')
    
    return redirect('/notes/')


def submitRegisterPage(request):
    if request.POST:
        username = request.POST.get('username')
        if not User.objects.filter(username = username):
            if username != '':
                password = request.POST.get('password')
                password_confirm = request.POST.get('confirmPassw')

                if password == password_confirm:
                    if password != '':
                        User.objects.create_user(username, '', password)

                    else: 
                        messages.error(request, 'Password field cannot be empty.')
                        return redirect('/register/')
            
                else:
                    messages.error(request, 'Passwords don\'t match.')
                    return redirect('/register/')

            else:
                messages.error(request, 'Please, inform an username.')
                return redirect('/register/')
            
        else:
            messages.error(request, 'Username already exists.')
            return redirect('/register/')
    
    return redirect('/notes/')  


def pin(request):
    pass


# TODO add exception treatment