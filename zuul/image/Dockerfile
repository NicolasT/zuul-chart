FROM docker.io/centos:7.4.1708

ARG version=3.0.3

# Install runtime dependencies
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y \
        git \
        libffi \
        python35u \
        re2 \
        && \
    yum clean all && \
    rm -rf /var/cache/yum

VOLUME /etc/zuul

RUN adduser --system zuul --home-dir /var/lib/zuul --create-home
VOLUME /var/lib/zuul/.ssh

# Install build-time dependencies, package and remove build-time dependencies
# Note: not removing libffi-devel due to
# https://bugs.centos.org/view.php?id=10828
RUN yum install -y \
        gcc \
        gcc-c++ \
        libffi-devel \
        python35u-devel \
        python35u-pip \
        re2-devel \
        && \
    pip3.5 install zuul==$version && \
    rm -rf ~/.cache/pip && \
    yum remove -y \
        gcc \
        gcc-c++ \
        python35u-devel \
        python35u-pip \
        re2-devel \
        && \
    yum clean all && \
    rm -rf /var/cache/yum

USER zuul:zuul
ENTRYPOINT ["zuul", "-c", "/etc/zuul/zuul.conf"]
