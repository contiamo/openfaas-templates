ARG watchdog_version=0.7.4
ARG python_version=3.7
FROM openfaas/of-watchdog:${watchdog_version} as watchdog

FROM python:${python_version}-alpine

RUN apk --no-cache add musl-dev gcc make
COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog

WORKDIR /root/

COPY requirements.txt   .
RUN pip install -r requirements.txt
COPY index.py           .

RUN mkdir -p function
RUN touch ./function/__init__.py
WORKDIR /root/function/
COPY function/requirements.txt	.
RUN pip install -r requirements.txt

WORKDIR /root/
COPY function           function

ENV fprocess="python index.py"

ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:5000"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
