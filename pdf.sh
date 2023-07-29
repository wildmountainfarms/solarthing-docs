#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
cd "$BASEDIR/docs" || exit 1
python3 -m venv .venv
. .venv/bin/activate
pip install -r source/requirements.txt
make clean latexpdf
xdg-open "file://$(pwd)/build/latex/solarthing.pdf"
