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
def submitUsernameUpdate(request):
    curr_user = request.user
    user = User.objects.filter(username = curr_user)

    if request.POST:
        new_username = request.POST.get('username')

        if new_username != ('' and curr_user):

            if not User.objects.filter(username = new_username):
                try:
                    user.update(username = new_username)
                    messages.success(request, 'Username changed successfully.')

                except:
                    messages.error(request, 'There was an error updating your username, try again.')
            
            else:
                messages.error(request, 'Username already exists.')

        else:
            messages.error(request, 'Invalid username.')

    return redirect('/account/')


@login_required(login_url = '/login/')
def submitPasswordUpdate(request):
    curr_user = request.user
    user = User.objects.get(username = curr_user)

    if request.POST:
        new_passw = request.POST.get('password')
        new_passw_confirm = request.POST.get('confirmPassw')

        if new_passw != '':

            if new_passw == new_passw_confirm:
                try:
                    user.set_password(new_passw)
                    user.save()
                    messages.success(request, 'Password changed successfully.')

                except:
                    messages.error(request, 'There was an error updating your password, try again.')
            
            else:
                messages.error(request, 'Passwords don\'t match')

        else:
            messages.error(request, 'Password cannot be empty')

    return redirect('/account/')


@login_required(login_url = '/login/')
def deleteAccount(request, username):
    request_user = request.user
    user_to_del = User.objects.get(username = username)

    if request_user == user_to_del:
        try:
            user_to_del.delete()
            messages.success(request, 'Account deleted successfully.')

        except:
            messages.error(request, 'There was an error deleting your account, try again.')
    
    else:
        messages.error(request, 'couldnt delete')

    return redirect('/')


@login_required(login_url = '/login/')
def notesPage(request):
    current_user = request.user
    notes = Note.objects.filter(user = current_user)
    notes = notes.order_by('-pinned', '-date_created')
    return render(request, 'notes.html', {'notes' : notes})


@login_required(login_url = '/login/')
def addNote(request):
    if request.POST:
        title = request.POST.get('title')

        if title != '':
            text = request.POST.get('text')
            user = request.user

            try:
                Note.objects.create(title = title, text = text, user = user)

            except:
                messages.error(request, 'There was an error uploading your note. Try again.')

        else:
            messages.error(request, 'Please, add a title to your note.')

    return redirect('/notes/') 


@login_required(login_url = '/login/')
def deleteNote(request, id):
    user = request.user
    note = Note.objects.filter(id = id, user = user)

    if note:
        try:
            note.delete()

        except:
            messages.error(request, 'There was an error deleting your note, try again.')

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

            try:
                note = Note.objects.filter(id = id)
                note.update(title = new_title)
                note.update(text = new_text)
            
            except:
                messages.error(request, 'There was an error updating your note, try again.')
            
        else:
            messages.error(request, 'Please, add a title to your note.')
            return redirect(f'/notes/update/{id}')

    return redirect('/notes/')


def loginPage(request):
    return render(request, 'login.html')


def submitLoginIndex(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username and password) != '':
            user = authenticate(username = username, password = password)

            try:
                if user is not None:
                    login(request, user)
                    return redirect('/notes/')
        
                else:
                    messages.error(request, 'Username or password is incorrect. Try again.')

            except:
                messages.error(request, 'There was an error logging you in, try again.')
                

        else:
            messages.error(request, 'Please, fill out fields correctly.')
    
    return redirect('/')


def submitLoginPage(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if (username and password) != '':
            user = authenticate(username = username, password = password)

            try:
                if user is not None:
                    login(request, user)
                    return redirect('/notes/')
        
                else:
                    messages.error(request, 'Username or password is incorrect. Try again.')

            except:
                messages.error(request, 'There was an error loggin you in, try again.')
                    
        else:
            messages.error(request, 'Please, fill out fields correctly.')
    
    return redirect('/login/')


@login_required(login_url = '/login/')
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
                        try:
                            User.objects.create_user(username, '', password)
                            return redirect('/notes/')

                        except:
                            messages.error(request, 'There was an error registering you, try again.')

                    else: 
                        messages.error(request, 'Password field cannot be empty.')
                        
            
                else:
                    messages.error(request, 'Passwords don\'t match.')
                    

            else:
                messages.error(request, 'Please, inform an username.')
                
            
        else:
            messages.error(request, 'Username already exists.')
            
    return redirect('/')
    

def submitRegisterPage(request):
    if request.POST:
        username = request.POST.get('username')

        if not User.objects.filter(username = username):

            if username != '':
                password = request.POST.get('password')
                password_confirm = request.POST.get('confirmPassw')

                if password == password_confirm:

                    if password != '':
                        try:
                            User.objects.create_user(username, '', password)
                            return redirect('/notes/')

                        except:
                            messages.error(request, 'There was an error registering you, try again.')

                    else: 
                        messages.error(request, 'Password field cannot be empty.')
                        
            
                else:
                    messages.error(request, 'Passwords don\'t match.')
                    

            else:
                messages.error(request, 'Please, inform an username.')
              
            
        else:
            messages.error(request, 'Username already exists.')
    
    return redirect('/register/')
    
      
@login_required(login_url = '/login/')
def togglePin(request, id):
    user = request.user
    note = Note.objects.filter(id = id, user = user)

    if Note.objects.filter(id = id, user = user, pinned = True):
        try:
            note.update(pinned = False)

        except:
            messages.error(request, 'Couldn\'t unpin your note, try again. ')
       
    elif Note.objects.filter(id = id, user = user, pinned = False):
        try:
            note.update(pinned = True)

        except:
            messages.error(request, 'Couldn\'t pin your note, try again.')

    return redirect('/notes/')
