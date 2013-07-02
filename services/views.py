from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic import DeleteView

from accounts.models import UserService

from .forms import ServiceAddForm

class ServiceAddView(FormView):
    """
    Add a service for the current user
    """
    template_name = 'services/add.html'
    form_class = ServiceAddForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ServiceAddView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('userena_profile_detail', args=(self.request.user.username,))

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        service = form.save(commit=False)
        service.profile = self.request.user.profile
        service.save()
        
        return super(ServiceAddView, self).form_valid(form)

class ServiceDeleteView(DeleteView):
    model = UserService
    template_name = 'services/userservice_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ServiceDeleteView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('userena_profile_detail', args=(self.request.user.username,))


