from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge
from prometheus_client.core import GaugeMetricFamily
from corona.helper import RapidApi

class Collector(object):

    """Prometheus Helper Functions."""

    def __init__(self):
        self._api_helper = RapidApi()
        self._metric_prefix = "coronavirus_"

    def _get_timestamp(self, timestring, timeformat):
        stat_time = datetime.strptime(timestring, timeformat)
        return datetime.timestamp(stat_time) + 330 * 60


    def _world_metrics(self):
        region = "world"
        world_stats = self._api_helper.world_stats()

        timestamp = self._get_timestamp(world_stats["statistic_taken_at"],
                                        "%Y-%m-%d %H:%M:%S")

        for key, value in world_stats.items():
            if key != "statistic_taken_at":
                clean_value = int(value.replace(",", ""))
                metric_name = self._metric_prefix + key
                metric = GaugeMetricFamily(metric_name,
                                           "%s for coronavirus" % key,
                                           labels = ["region"])
                metric.add_metric([region], clean_value, timestamp)
                yield metric


    def _countrywise_metrics(self):
        countrywise_stats = self._api_helper.stats_by_country()

        timestamp = self._get_timestamp(countrywise_stats["statistic_taken_at"],
                                        "%Y-%m-%d %H:%M:%S")

        for country_stat in countrywise_stats["countries_stat"]:
            country = country_stat["country_name"]
            region = country_stat["region"]
            for key, value in country_stat.items():
                if key not in ["country_name", "region"]:
                    clean_value = float(value.replace(",", ""))
                    metric_name = self._metric_prefix + key
                    metric = GaugeMetricFamily(metric_name,
                                            "%s for coronavirus" % key,
                                            labels = ["country", "region"])
                    metric.add_metric([country, region],
                                      clean_value,
                                      timestamp)
                    yield metric





    def collect(self):
        yield from self._world_metrics()
        yield from self._countrywise_metrics()

if __name__ == "__main__":
    coll = Collector()
    coll.collect_world_metrics()
