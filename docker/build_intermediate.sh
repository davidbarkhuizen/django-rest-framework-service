#! /usr/bin/env bash

python3 -m venv .venv

. .venv/bin/activate

echo "venv: $(which python)"

echo "installing pip"
python -m pip install --upgrade "pip==24.0"

echo "installing pip-tools"
python -m pip install "pip-tools==7.4.1"

echo "compiling requirements.txt from requirements.in"
pip-compile requirements.in

echo "installation of project dependencies from requirements.txt"
python -m pip install -r requirements.txt