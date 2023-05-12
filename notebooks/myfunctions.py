import pandas as pd

# read from global csv
def read_from_global_csv(name, type):

    global_vars = pd.read_csv('../global/movie_vars.csv', index_col='Name', usecols = ['Name','Value'])

    if type == list:
        global_vars['Value'] = global_vars['Value'].apply(eval)

    value = global_vars.loc[name]['Value']      
    
    return(value)

# create and/or add to global variable csv
def add_to_global_csv(name, value):
    try:
        existing_data = get_csv_data('../global/movie_vars.csv',['Name','Value'])

    except FileNotFoundError:
        print('Global var file will be created.')
        existing_data =  pd.DataFrame(columns=['Name', 'Value'])
        
    finally:
        new_data = pd.DataFrame(columns=['Name', 'Value'])

        new_data.at[1, 'Name'] = name
        new_data.at[1, 'Value'] = value

        new_data['Value'] = new_data['Value'].astype('object')

        final_data = pd.concat([existing_data, new_data], ignore_index = True )

        final_data.index = [x for x in range(1, len(final_data.values)+1)]
        final_data.index.name = 'Id'

        final_data.to_csv('../global/movie_vars.csv') 
    
# read from scv function with customised arguments
def get_csv_data(path, columns = []):
    if columns:
        data = pd.read_csv(path, usecols=columns) 
    else:   
        data = pd.read_csv(path, index_col= 'id') 
    return data     