from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganisorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated, and is an organisor """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated is True or request.user.is_organisor is False:
            print("--------------------------")
            print("the user is authenticated but not an organisor")
            print("--------------------------")
            return redirect("landing_page")
        if  request.user.is_organisor is True:
            print("The user is an organizer")
            return redirect("agents")

        return super().dispatch(request, *args, **kwargs)