FROM ubuntu

MAINTAINER Nawaz

RUN apt-get update
RUN apt install python3 -y

WORKDIR C:\Users\NawazS\Desktop\DockerFile-Custom

CMD [ "python3","Calculator_test_file.py" ]