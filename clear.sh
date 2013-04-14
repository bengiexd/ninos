#!/bin/sh

#eliminar pyc pre-compiled
find . -type f -name "*.pyc" -exec rm -f {} \;
