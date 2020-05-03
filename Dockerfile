FROM ubuntu:20.04

# Remote SSH
RUN apt-get update && apt-get install -y openssh-server sudo
RUN useradd --shell /bin/bash -m ubuntu
RUN gpasswd -a ubuntu sudo
RUN mkdir /var/run/sshd
RUN echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "ubuntu ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Set disable_coredump false" >> /etc/sudo.conf

# Live Share
RUN apt-get update && apt-get install -y libicu66 libkrb5-3 zlib1g openssl gnome-keyring desktop-file-utils desktop-file-utils x11-utils

# Dev
RUN apt-get update && apt-get install -y git curl jq

# initialize task
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install invoke pyyaml
COPY tasks.py /root/

# nodejs development
RUN apt-get update && apt-get install -y nodejs npm

EXPOSE 22
WORKDIR /root/
CMD ["python3", "-u", "-m", "invoke", "-e", "start"]
