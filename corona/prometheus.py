from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge
from prometheus_client.core import GaugeMetricFamily
from corona.helper import RapidApi, AnandApi
from corona.config import indian_states_abbr, country_code_map

class Collector(object):

    """Prometheus Helper Functions."""

    def __init__(self):
        self._api_helper = RapidApi()
        self._metric_prefix = "coronavirus_"

    def _get_timestamp(self, timestring, timeformat):
        stat_time = datetime.strptime(timestring, timeformat)
        return datetime.timestamp(stat_time)


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
                    # print(key,country, value)
                    if value == "N/A":
                        value = "0"
                    clean_value = float(value.replace(",", ""))
                    metric_name = self._metric_prefix + key
                    if country not in country_code_map:
                        continue
                    else:
                        code = country_code_map[country]
                    metric = GaugeMetricFamily(metric_name,
                                            "%s for coronavirus" % key,
                                            labels = ["country", "region", "code"])
                    metric.add_metric([country, region, code],
                                      clean_value,
                                      timestamp)
                    yield metric

    def collect(self):
        yield from self._world_metrics()
        yield from self._countrywise_metrics()


class IndiaCollector(object):

    def __init__(self):
        self._api_helper = AnandApi()
        self._metric_prefix = "india_coronavirus_"


    def _india_metrics(self):
        country = "India"
        india_stats = self._api_helper.india_stats()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        last_updated_time = datetime.strptime(india_stats["last_updated"],
                                              time_format )
        time_diff = (datetime.now() - last_updated_time) / 60

        yield GaugeMetricFamily("india_stats_last_update",
                                "last update time for india coronavirus stats",
                                value=int(time_diff.seconds))


        for key, value in india_stats["india"].items():
            metric_name = self._metric_prefix + "total_" + key
            metric = GaugeMetricFamily(metric_name,
                                        "%s for coronavirus in India" % key,
                                        value=value)
            yield metric

        for st, state_value in india_stats["states"].items():
            state = indian_states_abbr[st]
            for stat, number in state_value.items():
                metric_name = self._metric_prefix + stat
                metric = GaugeMetricFamily(metric_name,
                                           "%s cases for coronavirus in Indian states" % key,
                                           labels = ["state"])
                metric.add_metric([state], number)
                yield metric


    def collect(self):
        yield from self._india_metrics()


if __name__ == "__main__":
    coll = Collector()
    coll.collect_world_metrics()
