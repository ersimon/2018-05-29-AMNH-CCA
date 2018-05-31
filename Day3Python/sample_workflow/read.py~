'''Here we store some sample ways to read in data and spit out the pieces that we want from the dataset let's assume all of the data we are using has a header and columns so we can read it in using pandas read_csv method
let's create a function to read in our kind of data set, then returns an x and y value that we care about '''

import pandas as pd

def read_my_csv(csvfile):
    data = pd.read_csv(csvfile, sep =' ')
    return data.xaxis, data.yaxis
