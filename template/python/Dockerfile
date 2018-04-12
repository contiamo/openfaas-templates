FROM python:3-slim

RUN pip install flask
RUN touch /tmp/.lock

COPY *.py /

CMD ["python3", "/main.py"]
