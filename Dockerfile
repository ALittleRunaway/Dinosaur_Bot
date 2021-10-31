FROM python:3.8

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["python", "-m", "bot"]
