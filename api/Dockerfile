FROM python:3.8.13 as base

ARG UID
ARG GID

# Add a non-root user
RUN addgroup --gid $GID api
RUN adduser --disabled-login --geco '' --uid $UID --gid $GID api
USER api

# Append /home/app/.local/bin/ to PATH variable because
# gunicorn is installed there.
ENV PYTHONPATH=$PYTHONPATH:/home/api/
ENV PATH=$PATH:/home/api/.local/bin/

COPY . /home/api/

WORKDIR /home/api/

RUN pip install --upgrade pip && pip install -r requirements.txt

FROM base as test
RUN ["pytest", "-v", "tests/"]

FROM base as build
ENTRYPOINT ["gunicorn", "--workers=8", "--bind", "0.0.0.0:5000", "app:app"]