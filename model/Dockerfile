FROM python:3.8.13 as base

ARG UID
ARG GID

# Add a non-root user
RUN addgroup --gid $GID model_image
RUN adduser --disabled-login --geco '' --uid $UID --gid $GID model_image
USER model_image

# Append /home/app/.local/bin/ to PATH variable because
# gunicorn is installed there.
ENV PYTHONPATH=$PYTHONPATH:/home/model_image/
ENV PATH=$PATH:/home/model_image/.local/bin/

ADD requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /home/model_image/

WORKDIR /home/model_image

FROM base as test
RUN ["pytest", "-v", "tests"]

FROM base as build
ENTRYPOINT ["python3", "ml_service.py"]

