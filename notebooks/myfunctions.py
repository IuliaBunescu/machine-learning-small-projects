import pandas as pd

# read from global csv
def read_from_global_csv(name, type):

    global_vars = pd.read_csv('../global/movie_vars.csv', index_col='Name', usecols = ['Name','Value'])

    if type == list:
        global_vars['Value'] = global_vars['Value'].apply(eval)

    value = global_vars.loc[name]['Value']      
    
    return(value)