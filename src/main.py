from flask import Flask, render_template, Response
import time
import prometheus_client
from prometheus_client import Counter, Histogram
import logging
from imports import LOGGING, Service

# Initialize
app = Flask(__name__)
logging.basicConfig(encoding=LOGGING['encoding'], level=LOGGING['level'], format=LOGGING['format'], datefmt=LOGGING['datefmt'])
logger = logging.getLogger("logger")
testing_service = Service("Testing service")
graphs = {'c': Counter('python_request_operations_total', 'The total number of processed requests'),
          'h': Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds',
                         buckets=(0, 0.0001, 0.001, 0.01, 0.1, 1,))}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/logme")
def logme():
    logger.warning('TEST LOG msg')
    return "nothing"


@app.route("/break/")
def breakit():
    testing_service.change_status()
    return "nothing"


@app.route("/metrics/")
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")


@app.route("/health/")
def health():
    if testing_service.ready:
        return Response(status=200)
    else:
        return Response(status=500)


@app.route("/readiness/")
def readiness():
    if testing_service.ready:
        return Response(status=200)
    else:
        return Response(status=503)


@app.route("/meter")
def meter():
    start = time.time()
    graphs['c'].inc()
    time.sleep(0.100)
    end = time.time()
    graphs['h'].observe(end - start)
    return "nothing"


if __name__ == "__main__":
    app.run(port=8080, debug=True)