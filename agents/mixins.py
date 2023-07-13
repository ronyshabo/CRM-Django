from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganisorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated, and is an organisor """
    def dispatch(self, request, *args, **kwargs):

        # if not request.user.is_authenticated and request.user.is_organisor:
        #     return redirect("landing_page")
        # if  request.user.is_organisor is True:
        #     # return redirect("agents:agent-list")
        #     # causing an infinate loop

        #     return super().dispatch(request, *args, **kwargs)

        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect("leads:lead-list")
        return super().dispatch(request, *args, **kwargs)