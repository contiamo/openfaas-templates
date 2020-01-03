ARG watchdog_version=0.7.4
ARG go_version=1.13
ARG alpine_version=3.11
FROM openfaas/of-watchdog:${watchdog_version} as watchdog
FROM golang:${go_version} as build

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux

RUN mkdir -p /app
WORKDIR /app

COPY go.mod go.sum ./
RUN go mod tidy && go mod download
COPY . .

RUN go test -cover handler/function/...
RUN go build -a --ldflags "-s -w" -o handler .


FROM alpine:${alpine_version}
# Add non root user and certs
RUN apk --no-cache add ca-certificates \
    && addgroup -S app && adduser -S -g app app \
    && mkdir -p /home/app \
    && chown app /home/app

WORKDIR /home/app

COPY --from=watchdog /fwatchdog .
COPY --from=build /app/handler    .

RUN chown -R app /home/app

USER app

ENV fprocess="./handler"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:8082"

CMD ["./fwatchdog"]
