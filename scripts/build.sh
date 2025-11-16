#!/bin/bash
set -e
rm -rf dist build *.egg-info
python3 -m build
