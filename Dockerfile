FROM ubuntu:20.04

# For Remote SSH
RUN apt-get update && apt-get install -y openssh-server sudo
RUN useradd --shell /bin/bash -m ubuntu
RUN gpasswd -a ubuntu sudo
RUN mkdir /var/run/sshd
RUN echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "ubuntu ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Set disable_coredump false" >> /etc/sudo.conf

# For Live Share
RUN apt-get update && apt-get install -y libicu66 libkrb5-3 zlib1g openssl gnome-keyring desktop-file-utils desktop-file-utils x11-utils

# For Dev
RUN apt-get update && apt-get install -y git curl

RUN apt-get update && apt-get install -y nodejs npm
COPY ./entrypoint.sh /root/

EXPOSE 22
ENTRYPOINT ["bash", "/root/entrypoint.sh"]
