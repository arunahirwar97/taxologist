
FROM python:3.8-slim-buster
LABEL maintainer="mytaxboard"
ENV PYTHONNUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 install --upgrade django-cors-headers 


ENV  CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apt-get update \
    && apt-get -y install libpq-dev gcc libgl1 ffmpeg libsm6 libxext6\
    && pip install psycopg2

ENV  CRYPTOGRAPHY_DONT_BUILD_RUST=1


COPY ./corerequirements.txt ./corerequirements.txt
RUN pip3 install -r /corerequirements.txt

COPY ./baserequirements.txt ./baserequirements.txt
RUN pip3 install -r /baserequirements.txt


RUN mkdir /mytaxboard
WORKDIR /mytaxboard
COPY ./mytaxboard /mytaxboard
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser user --no-create-home --disabled-password
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
VOLUME /vol/web

CMD ["entrypoint.sh"]
