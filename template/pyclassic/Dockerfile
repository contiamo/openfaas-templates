FROM python:3-slim

COPY requirements.txt .
RUN pip install -r requirements.txt && pip install flask

COPY *.py /

CMD ["python3", "/main.py"]
