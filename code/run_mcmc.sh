#!/bin/bash
python mcmc.py
python burnin.py
python corner_plots.py
zathura corner.pdf
