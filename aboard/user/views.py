from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate, decorators as dec
from user.forms import UserForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from user.models import User



def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/hposts/")
    context = {
        "form": UserForm(),
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    request.META.get("HTTP_REFERER")
                    if request.META.get("HTTP_REFERER") is not None
                    else "/home/"
                )
        else:
            context.update(form=form)
    return render(request, "login.html", context)


@dec.login_required(login_url="/user/login/")
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/hposts/")




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration.html', {'new_user': new_user})
            profile = User.objects.create(user=new_user)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})


@dec.login_required(login_url="/edit/")
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'edit.html', {'user_form': user_form,  'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
        return render(request, 'edit.html', {'user_form': user_form,  'profile_form': profile_form})