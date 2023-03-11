from django.views.generic import FormView
from django.urls import reverse
from .forms import FormFeadback


class HomeViev(FormView):
    template_name = "home_page.html"
    form_class = FormFeadback

    def get_success_url(self):
        return self.request.GET.get("next", reverse("home_page"))

