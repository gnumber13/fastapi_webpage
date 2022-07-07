#!/bin/sh

application_path=$(realpath "$0" | rev | cut -d'/' -f2- | rev)
cd $application_path

#git pull

python3 -m uvicorn main:app
