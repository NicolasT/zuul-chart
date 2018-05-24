#!/bin/bash

set -e
set -u

if test ! -f /etc/ssh/ssh_host_rsa_key \
        -a ! -f /etc/ssh/ssh_host_ecdsa_key \
        -a ! -f /etc/ssh/ssh_host_ed25519_key;
then
        echo "Generating host keys"
        /usr/sbin/sshd-keygen
fi

if test ! -f ~/.ssh/authorized_keys \
        -a -n "${AUTHORIZED_KEYS}";
then
        echo "Creating authorized_keys file"
        mkdir -p ~/.ssh && chmod 0700 ~/.ssh
        echo "${AUTHORIZED_KEYS}" > ~/.ssh/authorized_keys
        chmod 0600 ~/.ssh/authorized_keys
fi

exec /usr/sbin/sshd -D -e
