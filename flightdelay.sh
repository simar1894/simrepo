# !/usr/bin/env bash
cut -d"," -f 15,17 flightdelays.csv.2 | grep "SFO" |head -3 | cut -d"," -f 1 > first3sfo.csv
cat first3sfo.csv
