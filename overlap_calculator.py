#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


def calculate_overlaps(df, markers):
    """
    Calculate and return the overlaps between pairs of markers.

    Parameters:
    - df (DataFrame): The dataframe containing the marker data.
    - markers (list of str): A list of marker names to consider for overlap calculation.

    Returns:
    - DataFrame: A dataframe with the overlap results for each marker pair.
    """
    results = []
    for i in range(len(markers)):
        for j in range(i + 1, len(markers)):
            marker1 = markers[i]
            marker2 = markers[j]
            count1 = (df[marker1] == marker1).sum()  # Count how many cells are positive for marker1
            count2 = (df[marker2] == marker2).sum()  # Count how many cells are positive for marker2
            both = ((df[marker1] == marker1) & (df[marker2] == marker2)).sum()  # Count cells positive for both

            # Calculate the percentage overlap
            perc_of_1 = (both / count1 * 100) if count1 else 0
            perc_of_2 = (both / count2 * 100) if count2 else 0
            
            # Append results for each pair to the results list
            results.append({
                'Markers': f'{marker1} & {marker2}',
                'Count of ' + marker1: count1,
                'Count of ' + marker2: count2,
                'Count of Both': both,
                f'Percentage in {marker1}': perc_of_1,
                f'Percentage in {marker2}': perc_of_2
            })

    return pd.DataFrame(results)

# Calculate and print the overlaps
overlap_results = calculate_overlaps(dfp, markers)
overlap_results = pd.DataFrame(overlap_results)
print(overlap_results)

