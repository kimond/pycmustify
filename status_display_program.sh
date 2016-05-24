#!/bin/sh
cmustify=`realpath cmustify.py`
python $cmustify "$*" &
