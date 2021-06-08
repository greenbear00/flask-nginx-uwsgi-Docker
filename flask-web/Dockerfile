FROM python:3

# install vi Editor
RUN apt-get update
RUN apt-get install -y vim

# 가상환경이 아닌 자체에 requirements를 설치해서 실행
WORKDIR /app
ADD . /app
RUN rm -rf venv
RUN pip install -r requirements.txt

#CMD ["uwsgi", "uwsgi.ini"]
ENTRYPOINT ["./gunicorn.sh"]