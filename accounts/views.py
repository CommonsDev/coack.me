from userena import settings as userena_settings
from django.shortcuts import redirect, get_object_or_404
from userena.utils import signin_redirect, get_profile_model, get_user_model
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect
from django.utils.translation import ugettext as _
from userena.views import ExtraContextTemplateView
from django.core.urlresolvers import reverse_lazy
from userena.views import profile_edit as userena_profile_edit
from django.views.generic import TemplateView
from userena.decorators import secure_required
from guardian.decorators import permission_required_or_403

from .forms import ProfileEditForm

class ProfileDetailView(TemplateView):
    template_name = userena_settings.USERENA_PROFILE_DETAIL_TEMPLATE
    
    def get_context_data(self, username, extra_context=None, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        
        user = get_object_or_404(get_user_model(),
                                 username__iexact=username)

        profile_model = get_profile_model()
        try:
            profile = user.get_profile()
        except profile_model.DoesNotExist:
            profile = profile_model.objects.create(user=user)
            
        if not profile.can_view_profile(self.request.user):
            return HttpResponseForbidden(_("You don't have permission to view this profile."))
        
        if not context:
            context = dict()
            
        context['profile'] = profile
        context['hide_email'] = userena_settings.USERENA_HIDE_EMAIL

        

        return context

@secure_required
@permission_required_or_403('change_profile', (get_profile_model(), 'user__username', 'username'))
def profile_edit(request, username, *args, **kwargs):
    return userena_profile_edit(request,
                                username=username,
                                edit_profile_form=ProfileEditForm,
                                template_name='userena/profile_form.html',
                                success_url=reverse_lazy('profile-detail', args=(username,))
    )
