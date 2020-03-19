import requests
from corona.config import HOST, API_KEY


class CoronaHelper(object):
    """Helper class for Corona Rapid API."""

    headers = {
        "x-rapidapi-host": HOST,
        "x-rapidapi-key": API_KEY
    }

    host = HOST

    def _get_complete_url(self, url):
        """Construct complete url to make request to."""
        return "https://%s/%s/%s.php" % (self.host, "coronavirus", url)

    def _make_request(self, url):
        """Make request to Rapid API."""
        req_url = self._get_complete_url(url)
        results = requests.get(req_url, headers=self.headers)
        if results.status_code == 200:
            return results

    def world_stats(self):
        """Get world stats."""
        res = self._make_request("worldstat")
        return res.json()
