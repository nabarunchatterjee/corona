import requests
from corona.config import HOST, API_KEY


class RapidApi(object):
    """Helper class for Corona Rapid API."""

    headers = {
        "x-rapidapi-host": HOST,
        "x-rapidapi-key": API_KEY
    }

    host = HOST

    def _get_complete_url(self, url):
        """Construct complete url to make request to."""
        return "https://%s/%s/%s.php" % (self.host, "coronavirus", url)

    def _make_request(self, url, params={}):
        """Make request to Rapid API."""
        req_url = self._get_complete_url(url)
        results = requests.get(req_url, headers=self.headers, params=params)
        if results.status_code == 200:
            return results

    def stats_by_country(self):
        """Get world stats."""
        res = self._make_request("cases_by_country")
        return res.json()


    def world_stats(self):
        """Get world stats."""
        res = self._make_request("worldstat")
        return res.json()

    def country_history(self, country):
        params = {"country": country}
        res = self._make_request("cases_by_particular_country", params)
        return res.json()

    def country_latest_stat(self, country):
        params = {"country": country}
        res = self._make_request("latest_stat_by_country", params)
        return res.json()

class AnandApi(object):
    """Helper for Anand's India Data"""

    def india_stats(self):
        url = "http://covid19-india.anandology.com/cases/live"

        results = requests.get(url)
        return results.json()
