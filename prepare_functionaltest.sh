#!/usr/bin/env bash

./linku/manage.py migrate
./linku/manage.py loaddata linku/moim/fixtures/meeting-data.json
./linku/manage.py runserver

