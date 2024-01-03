# Analysis Process Folder - Python Scripts

This folder contains Python code for an analyzing process. The code is structured to perform specific tasks related to data analysis.

## Overview

The purpose and goals of the analyzing process implemented in this folder is to carry out non-GIS related tasks in the mobility hub projects.

## Contents

- **GTFS_process.py**: Process the GTFS data.
- **transit_ridership_and_supply.py**: Calculate the transit index.
- **socioeconomic_access_road.py**: Calculate the sub criteria for the socioeconomic index, the accessibility index, and the infrastructure index.
- **fmlm_gap_score**: Calculate the fmlm_gap score, a sub criterion in the FM/LM connectivity index.
- **microtransit_fmlm.py**: Calculate the micro_transit_fmlm score, a sub criterion in the FM/LM connectivity index.
- **index_calculation.py**: Calculate the five indexes.
- **site_selection.ipynb**: Calculate the final mobility hub score. With an algorithm, iteratively identify hub locations based on the mobility hub score calculated.