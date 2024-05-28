#!/bin/sh

# requires root privileges

# install git, curl
apt install git curl

# install docker
curl -sfL https://get.docker.com | sh -

# add the current user to the docker group for non-root docker management
groupadd docker && usermod -aG docker $USER && newgrp docker

# clone the source code
#git clone https://github.com/...

# build and run docker containers
docker compose up -d --build

# run the migrations
docker compose exec web python manage.py migrate --noinput

