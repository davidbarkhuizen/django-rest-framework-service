#! /usr/bin/env bash

echo
echo "python venv"
python3 -m venv .venv
. .venv/bin/activate

echo
echo "venv: $(which python)"

echo
echo "installing pip"
python -m pip install --upgrade "pip==24.0"

echo
echo "installing pip-tools"
python -m pip install "pip-tools==7.4.1"

echo
echo "compiling requirements.txt from requirements.in"
pip-compile requirements.in

echo
echo "installation of project dependencies from requirements.txt"
python -m pip install -r requirements.txt