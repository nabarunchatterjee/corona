from flask import Flask, Response
from corona.prometheus import Collector
from prometheus_client.exposition import generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def metrics():
    collector_obj = Collector()
    return Response(generate_latest(collector_obj),
                    mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run()
