FROM docker.io/alpine:3.7

RUN apk add --no-cache \
        libffi \
        openssl \
        python3

WORKDIR /usr/src/nodepool-config-builder

COPY requirements.txt .
RUN apk add --no-cache --virtual build-dependencies \
        gcc \
        libffi-dev \
        make \
        musl-dev \
        openssl-dev \
        python3-dev \
        && \
    pip3 install -r requirements.txt && \
    rm -rf ~/.cache/pip && \
    apk del build-dependencies

COPY . .

ENTRYPOINT ["/usr/src/nodepool-config-builder/nodepool-config-builder.py"]
