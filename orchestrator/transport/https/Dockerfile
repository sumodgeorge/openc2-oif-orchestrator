FROM screambunn/alpine_python3

LABEL name="HTTPS Transport Module" \
vendor="OpenC2" \
license="BSD" \
version="2.0" \
description="This is the HTTPS Transport Module container"

# Add Files
ADD HTTPS/ /opt/transport/HTTPS
ADD requirements.txt /tmp/requirements.txt
ADD docker_dev_start.sh /opt/transport/dev_start.sh

# Requirements install
RUN apk update
RUN apk add --no-cache \
  bash \
  openssl && \
apk add --no-cache --virtual .build-deps \
  gcc \
  libffi-dev \
  musl-dev \
  openssl-dev \
  python3-dev &&\
pip3 install -r /tmp/requirements.txt && \
#
# Script Setup
chmod +x /opt/transport/dev_start.sh && \
dos2unix /opt/transport/dev_start.sh && \
#
# Cleanup
apk del .build-deps && \
rm -rf /var/cache/apk/* *.tar.gz* /usr/src /root/.gnupg /tmp/*

# Set working directory
WORKDIR /opt/transport

# Run command when container launches
CMD ["./dev_start.sh"]

