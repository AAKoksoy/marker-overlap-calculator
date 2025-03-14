# marker-overlap-calculator

# Marker Overlap Calculator

## Overview
This script calculates the overlap percentages between various markers in cell data.
The function takes in a df and a list of markers of interest

## Requirements
- Python
- Pandas library

## Sample df
dfp = pd.DataFrame({
    'CD45': ['Other', 'CD45', 'CD45'],
    'CD31': ['CD31', 'Other', 'CD31'],
    'CK': ['Other', 'CK', 'Other'],
    'CD3': ['CD3', 'Other', 'CD3']
})

# List of markers of interest
markers = ['CD45', 'CD31', 'CK', 'CD3']

## Usage
Run the script with Python. Ensure that you have Pandas installed:

```bash
pip install pandas
python overlap_calculator.py
