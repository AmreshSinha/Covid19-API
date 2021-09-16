FROM ubuntu:18.04
COPY . /app

EXPOSE 80
EXPOSE 443

CMD ./app/run.sh