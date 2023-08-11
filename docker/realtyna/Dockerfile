FROM python:3.9
LABEL MAINTAINER="realtyna | https://realtyna.com"
LABEL VERSION="0.0.0.1"

ENV PYTHONUNBUFFERED 1

ENV HOME=/opt/realtyna/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
ADD requirements/base.txt $HOME
RUN pip install --upgrade pip
RUN pip install -r base.txt

COPY configs $HOME/configs
COPY manage.py $HOME
COPY realtyna $HOME/realtyna
COPY docker/realtyna/entrypoints/* $HOME
