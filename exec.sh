#!/usr/bin/env bash
# automating some boring stuff

tree

# Test Shell script style
shellcheck "$0"

# Make all python files executable
find . -type f -name "*.py" -exec chmod +x {} \;

# SetUp black code formater
# You need first to install `Black code` formatter
find . -type f -name "*.py" -exec black {} \;

# Test python code style
# You need first to install `pycodestyle` linter
find . -type f -name "*.py" -exec pycodestyle {} \;


