#lib
import pandas as pd 
import sys

# Read and store content 
# of an excel file  
file = pd.read_excel(sys.argv[1]) 

  
# Write the dataframe object 
# into csv file 
file.to_csv ('{}.csv'.format(sys.argv[1]), index = None, header=True)