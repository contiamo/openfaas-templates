FROM python:3.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.9.4/of-watchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY index.py .
COPY handler.py .

ENV fprocess="python index.py"
ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:5000"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
