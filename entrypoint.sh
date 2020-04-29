#!/bin/bash
if [ -n "$AUTHORIZED_KEYS" ] ;then
    mkdir -p /home/ubuntu/.ssh
    echo $AUTHORIZED_KEYS >> /home/ubuntu/.ssh/authorized_keys
fi
if [ -n "$REPO" ] ;then
    cd /home/ubuntu/
    sudo -u ubuntu git clone $REPO
fi
/usr/sbin/sshd -D
