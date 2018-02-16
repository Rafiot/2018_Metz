#!/bin/bash

set -e
set -x

wget https://owncloud.rafiot.eu/s/gp2cn7trXXsae63/download -O data/bview.tar.gz

pushd data
tar xzf bview.tar.gz
popd
