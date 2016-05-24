#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cmustify="${DIR}/cmustify.py"
python $cmustify "$*" &
