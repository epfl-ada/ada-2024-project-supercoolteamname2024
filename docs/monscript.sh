#!/bin/bash

if [ "$1" == "build" ]; then
    echo "Building the site..."
    bundle exec jekyll build --config _config.yml,_config_dev.yml
elif [ "$1" == "serve" ]; then
    echo "Starting the local server..."
    bundle exec jekyll serve --config _config.yml,_config_dev.yml
else
    echo "Usage: $0 {build|serve}"
fi
