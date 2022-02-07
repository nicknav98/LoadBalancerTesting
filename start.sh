#!/bin/bash
cd home/app
pip install -r requirements.txt
flask db init
flask db upgrade
python app.py


