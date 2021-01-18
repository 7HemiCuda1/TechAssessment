FROM python:3.8

RUN useradd -ms /bin/bash test_user
RUN mkdir /usr/src/app
RUN chmod -R 777 /usr/src/app
WORKDIR /usr/src/app

#replace this with git download.
COPY . .

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_87.0.4280`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN chmod -R 755 /usr/local/bin/chromedriver

# set display port to avoid crash
ENV DISPLAY=:9222

RUN pip install --upgrade pip
RUN pip install pytest
RUN pip install selenium

USER test_user

RUN pytest -s -v tests\