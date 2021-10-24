FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/myapp

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./myapp .
RUN pip install ./profile ./profile_infrastructure ./health_diary ./health_diary_infrastructure
RUN adduser --disabled-password user
RUN chown -R user:user /usr/src
USER user
