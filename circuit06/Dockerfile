FROM resin/raspberrypi3-python:2.7.14

RUN apt-get update \
 && apt-get install -y --no-install-recommends python-smbus \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get -y autoremove

WORKDIR /usr/src/app
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . ./

ENV INITSYSTEM on

CMD ["python", "main.py"]
