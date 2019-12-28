FROM python:3-alpine

WORKDIR /usr/src/simple_web_app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]
