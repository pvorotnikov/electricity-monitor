FROM python:3

RUN mkdir /usr/app
ADD ["README.md", "LICENSE", "requirements.txt",  "setup.py", "setup.cfg", "/usr/app/"]
ADD ["monitor", "/usr/app/monitor/"]
WORKDIR /usr/app
RUN PBR_VERSION=0.0.0-dev pip install .