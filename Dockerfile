FROM --platform=linux/amd64 python:3.7-slim-buster

RUN mkdir home/app && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc python3-dev musl-dev && \
    apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5050

COPY . /home/app
ADD . /start.sh /

RUN chmod +x start.sh
CMD ["/start.sh"]
