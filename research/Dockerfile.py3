FROM tensorflow/tensorflow:1.4.1-py3

RUN apt-get update \
    && apt-get install -y python3-tk protobuf-compiler

COPY . /tensorflow/models

RUN cd /tensorflow/models \
    && protoc object_detection/protos/*.proto --python_out=. \
    && python setup.py sdist \
    && (cd slim && python setup.py sdist)

ENV PYTHONPATH=$PYTHONPATH:/tensorflow/models:/tensorflow/models/slim
