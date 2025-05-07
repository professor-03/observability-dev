from flask import Flask, request
import logging
import time
import random
import sys
from prometheus_client import Counter, generate_latest, Summary, start_http_server
from jaeger_client import Config
import opentracing

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("app")

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')
REQUEST_LATENCY = Summary('app_request_latency_seconds', 'Request latency')

# Jaeger tracer
def init_tracer(service):
    config = Config(
        config={ 'sampler': {'type': 'const', 'param': 1},
                 'logging': True },
        service_name=service,
    )
    return config.initialize_tracer()

tracer = init_tracer('observability-app')
app = Flask(__name__)

@app.route("/")
@REQUEST_LATENCY.time()
def index():
    with tracer.start_span('index-request') as span:
        REQUEST_COUNT.inc()
        latency = random.random()
        logger.info(f"Request latency: {latency:.2f}")
        time.sleep(latency)
        return f"Hello! Latency: {latency:.2f}s"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    start_http_server(8001)  # Expose metrics
    app.run(host='0.0.0.0', port=8000)

