FROM docker.io/centos:7.4.1708

RUN yum install -y \
        openssh-server \
        && \
    yum clean all && \
    rm -rf /var/cache/yum

EXPOSE 22

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
