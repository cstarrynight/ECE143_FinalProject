import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from tqdm import tqdm
import argparse

def read_csv_file(_file):
    '''
    This function reads a CSV file from the datasets folder.
    It also adds two additional columns to the dataframe to separate the starting and ending roads.

    INPUTS:
        _file: str
            - Contains the path to the CSV file to read.
    
    RETURNS:
        ef: pd.DataFrame
    '''

    assert isinstance(_file, str)  # file must be a path given as a string
    assert '../datasets' in _file  # file must be in the datasets folder 
    assert '.csv' in _file         # file must be in a csv format

    df = pd.read_csv(_file)

    # Remove the unnamed columns in dataframe
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Filter the dataframe with only the necessary attributes
    ef = df[['CNN', 'PRIMARY_ST', 'CROSS_STREET_1', 'CROSS_ST_2', 'VOLUME_ADT', 'DATE']]\
        .query('VOLUME_ADT.notna()').query('CROSS_STREET_1.notna()').query('CROSS_ST_2.notna()')

    return ef

def generate_coordinates(df, geolocator):
    '''
    This function generates the Latitudes and Longitudes 
    of the corresponding starting and ending street names.

    INPUTS: 
        df: pd.DataFrame
        geolocator: Nominatim
        start_lookup_table: Dict<str>
        end_lookup_table: Dict<str>

    OUTPUTS:
        ef: pd.DataFrame
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(geolocator, Nominatim)

    # Adding the columns for Latitudes and Longitudes 
    # for the starting and ending street names
    ef = df.copy()
    ef['lat_x'] = np.nan
    ef['lon_x'] = np.nan
    ef['lat_y'] = np.nan
    ef['lon_y'] = np.nan

    # Renaming the columns of the dataframe and removing the unnamed columns
    ef = ef.rename(columns={'CROSS_STREET_1':'start_loc', 'CROSS_ST_2':'end_loc', 'VOLUME_ADT':'count'})
    ef = ef.loc[:, ~ef.columns.str.contains('^Unnamed')]
    
    for i in tqdm(range(0, len(ef))):
        # These flags indicate whether the coordinates for the road intersections are valid
        flag_start = True
        flag_end = True

        # Geocoding the intersections of the starting roads
        try:
            start_loc = geolocator.geocode(f"{ef.at[i,'PRIMARY_ST']} & {ef.at[i,'start_loc']}, San Francisco, CA")

        # If the Intersection is not a valid input, then flag it to False
        except:
            flag_start = False
            start_loc = None

        # If the intersection of the road doesn't generate valid coordinates,
        # then geocode the starting road
        if flag_start is False or start_loc is None:
            try:
                start_loc = geolocator.geocode(f"{ef.at[i,'start_loc']}, San Francisco, CA")
            except:
                print('Invalid street name at start loc!')
                lat_x = np.nan
                lon_x = np.nan

        if start_loc is None:
            lat_x = np.nan
            lon_x = np.nan
        else:
            lat_x = start_loc.latitude
            lon_x = start_loc.longitude

        # Geocoding the intersections of the ending roads
        try:
            end_loc = geolocator.geocode(f"{ef.at[i,'PRIMARY_ST']} & {ef.at[i,'end_loc']}, San Francisco, CA")

        # If the Intersection is not a valid input, then flag it to False
        except:
            flag_start = False
            end_loc = None

        # If the intersection of the road doesn't generate valid coordinates,
        # then geocode the ending road
        if flag_end is False or end_loc is None:
            try:
                end_loc = geolocator.geocode(f"{ef.at[i,'end_loc']}, San Francisco, CA")
            except:
                print('Invalid street name at end loc!')
                lat_y = np.nan
                lon_y = np.nan

        if end_loc is None:
            lat_y = np.nan
            lon_y = np.nan
        else:
            lat_y = end_loc.latitude
            lon_y = end_loc.longitude

        # Populating the latitudes and longitudes to the corresponding columns
        ef.at[i, 'lat_x'] = lat_x
        ef.at[i, 'lon_x'] = lon_x
        ef.at[i, 'lat_y'] = lat_y
        ef.at[i, 'lon_y'] = lon_y
    
    return ef

def export_data_to_csv(df, filename):
    '''
    This function exports a DataFrame to a csv file.

    INPUTS: 
        df: pd.DataFrame
        filename: str
    
    RETURNS: 
        None
    '''

    # Make sure that the file is exported to a csv file within the processed_datasets folder
    assert isinstance(df, pd.DataFrame)
    assert '../processed_datasets' in filename
    assert '.csv' in filename

    df.to_csv(filename)

if __name__=='__main__':
    #create an ArgumentParser object
    parser = argparse.ArgumentParser\
                (description = 'Specify the file names for the preprocessed dataset'\
                               'and logging street names')
    
    #declare arguments
    parser.add_argument('-i','--input_dir', type = str, required = True, help='file name of raw dataset')
    parser.add_argument('-o','--output_dir', type = str, required = True, help='file name of preprocessed dataset')
    args = parser.parse_args()

    # initializing variables from command line arguments
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Initializing the geocoding
    geolocator = Nominatim(user_agent='Lat-Lon-conversion')

    df = read_csv_file(input_dir)
    ef = generate_coordinates(df, geolocator)

    # Exporting the preprocessed data
    export_data_to_csv(ef, output_dir)
    print('Successfully exported dataset to {}'.format(output_dir.replace('../', '')))
