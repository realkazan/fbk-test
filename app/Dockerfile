FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

COPY . .

RUN ls -la && pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
