FROM ubuntu:22.04
COPY . /app
WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install matplotlib && pip install pyyaml
CMD ["bash", "params/runExperiment.sh"]
