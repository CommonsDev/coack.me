from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
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
        return reverse('profile-detail', args=(self.request.user.username,))

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        service = form.save(commit=False)
        service.profile = self.request.user.profile
        service.save()

        messages.success(self.request, _("Service '%(service_name)s' added to your profile" % {'service_name': service.service.name}))
        
        return super(ServiceAddView, self).form_valid(form)

    
class ServiceDeleteView(DeleteView):
    model = UserService
    template_name = 'services/userservice_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, request, pk, *args, **kwargs):
        user_service = get_object_or_404(UserService, pk=pk)
        if user_service.profile.user != request.user:
            raise HttpResponseForbidden

        return super(ServiceDeleteView, self).dispatch(request, pk, *args, **kwargs)

    def get_success_url(self):
        return reverse('profile-detail', args=(self.request.user.username,))


