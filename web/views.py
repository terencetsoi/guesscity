import random

from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView

from web.country import CountryMap


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
        country_map = CountryMap()

        context = {
            "country": country_map.get_random_country(),
        }
        context.update(kwargs)
        return super().get_context_data(**context)


class ResultView(APIView):
    """
    Return result.
    """

    allowed_methods = ["post"]
    success_response = ["Correct!", "Awesome!", "You got it!", "Brilliant!"]

    def post(self, request):
        """
        Respond to any post request with an empty status 200 response.
        """
        if request.data is None or request.data.get("data") is None:
            return JsonResponse(status=200, data={"result": "Empty request."})

        country_map = CountryMap()
        country = request.data.get("data").get("country")
        answer = request.data.get("data").get("city")

        capital = country_map.get_capital(country)

        if str(answer).lower() == str(capital).lower():
            result = random.choice(self.success_response)
        elif capital == "" and "no" in str(answer).lower():
            result = random.choice(self.success_response)
        else:
            result = f"Correct Answer: {capital}"

        return JsonResponse(status=200, data={"result": result})
