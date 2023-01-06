import json
import random

import requests
from django.conf import settings


class CountryMap:
    """
    Class view for index page.
    """

    country_map = None

    def get_mapping(self):
        """
        Get mapping from internet.
        """
        if self.country_map is not None:
            return self.country_map

        try:
            # Load countries list as json to dict
            response = requests.get(settings.COUNTRY_URL)
            content = json.loads(response.content)
            self.country_map = {}
            for item in content["data"]:
                country = item.get("name")
                capital = item.get("capital")
                self.country_map[country] = capital

            return self.country_map

        except Exception:
            return None

    def get_random_country(self):
        """
        Pick random country from map.
        """
        country_map = self.get_mapping()
        if country_map is None:
            return ""

        # Draw a country
        country = random.choice(list(country_map.keys()))

        return country

    def get_capital(self, country):
        """
        Get capital from country map.
        """
        country_map = self.get_mapping()

        return country_map[country]
