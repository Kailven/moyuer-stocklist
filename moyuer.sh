#!/usr/bin/env bash

cd ~/moyuer-stocklist
if [[ $1 == '-v' || $1 == '--version' ]] ; then
    python moyuer.py $1
elif [[ $1 == '-c' || $1 == '--codes' ]] ; then
    python moyuer.py $*
    clear
else
    python moyuer.py
    clear
fi