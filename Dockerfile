FROM python:3.6.8-stretch


RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt --src /usr/local/src
RUN python3 -c "import nltk;nltk.download('stopwords', download_dir='/usr/local/share/nltk_data')"
RUN python3 -c "import nltk;nltk.download('punkt', download_dir='/usr/local/share/nltk_data')"

COPY . /srv/flask_app
WORKDIR /srv/flask_app

COPY nginx.conf /etc/nginx
ENTRYPOINT ["/bin/bash", "run.sh"]
