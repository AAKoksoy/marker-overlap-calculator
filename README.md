
# Marker Overlap Calculator
This function is designed for quality control (QC) in high-plex proteomic or transcriptional single-cell datasets, such as those obtained from CODEX (Co-Detection by indEXing) or IMC (Imaging Mass Cytometry) technologies. It specifically evaluates the overlap of markers that are typically considered 'mutually exclusive' within individual cells. This assessment helps in identifying potential issues with marker specificity, staining quality, or data processing algorithms, ensuring the reliability and accuracy of the dataset analysis.

## Overview
This script calculates the overlap percentages between various markers in cell data.
The function takes in a df and a list of markers of interest

## Requirements
- Python
- Pandas library

## Sample df
```python

dfp = pd.DataFrame({
    'CD45': ['Other', 'CD45', 'CD45'],
    'CD31': ['CD31', 'Other', 'CD31'],
    'CK': ['Other', 'CK', 'Other'],
    'CD3': ['CD3', 'Other', 'CD3']
})

## List of markers of interest
markers = ['CD45', 'CD31', 'CK', 'CD3']

## Usage
Run the script with Python. Ensure that you have Pandas installed:

```bash
pip install pandas
python overlap_calculator.py
