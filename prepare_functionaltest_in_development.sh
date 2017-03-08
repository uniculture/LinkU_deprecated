#!/usr/bin/env bash

./linku/manage.py migrate --settings=linku.settings.development
./linku/manage.py runserver --settings=linku.settings.development  

