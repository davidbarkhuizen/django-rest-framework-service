#! /usr/bin/env bash

python3 -m venv .venv

. .venv/bin/activate
which python
python --version

python -m pip install --upgrade "pip==24.0"
python -m pip install "pip-tools==7.4.1"

# python -m pip-compile requirements.in

python -m pip install -r requirements.txt
