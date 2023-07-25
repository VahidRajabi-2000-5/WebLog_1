from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    
# @login_required
# def profile_view(request):
#     profile = get_object_or_404(User, username = request.user.username)
#     return render(request,'accounts/profile.html',{'pro':profile})

    
class ProfileView(LoginRequiredMixin,generic.DetailView):
    template_name ='accounts/profile.html'
    context_object_name = 'pro'
    def get_object(self):
        return get_object_or_404(User,username=self.request.user.username)