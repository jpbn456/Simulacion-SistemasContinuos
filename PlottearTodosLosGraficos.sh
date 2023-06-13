#!/bin/bash
for file in *.csv
do
    python3 Plotter.py "$file"
done
