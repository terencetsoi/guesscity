from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    """
    Class view for index page.
    """

    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        """
        Update context.
        """
        context = {
            "map": {"Afghanistan": "Kabul"},
        }
        context.update(kwargs)
        return super().get_context_data(**context)
