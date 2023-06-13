#!/bin/bash
for file in *.csv
do
    python3 plotter.py "$file"
done
