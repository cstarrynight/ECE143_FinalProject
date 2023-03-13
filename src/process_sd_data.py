import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from tqdm import tqdm
import argparse

class FixStreetNames():
    def __init__(self):
        '''
        Initializes The FixStreetNames class. This class stores variables that the user can alter
        NOTE: User can change the following attributes based on the street names of their data

        INPUTS:
            None

        ATTRIBUTES:
            self.corrected_start_roads: List<str>
                - This contains the correct names of the starting roads that have invalid names from dataset

            self.corrected_end_roads: List<str>
                - This contains the correct names of the ending roads that have invalid names from dataset
        '''

        self.corrected_start_roads = ['1st AV', '2nd AV', '3rd AV', '4th AV', '5th AV', '6th AV', '7th AV', '8th AV', '9th AV',\
                                '10th AV', '14th ST', 'Washington ST', '16th ST', '16th ST', '16th ST', '17th ST', \
                                '18th ST', '18th ST', '22nd ST', '24th ST', '25th ST', '25th ST', '26th ST', '26th ST', \
                                '27th ST', '27th ST', '28th ST', '29th ST', '30th ST', '30th ST', '30th ST', '32nd ST', \
                                '33rd ST', '35th ST', '36th ST', '37th ST', '37th ST', '38th ST', '39th ST', '41st ST', '42nd ST', \
                                '43rd ST', '44th ST', '45th ST', '46th ST', '47th ST', '48th ST', '49th ST', '50th ST', '51st ST', \
                                '52nd ST', '53rd ST', '54th ST', '54th ST', '55th ST', '56th ST', '58th ST', '61st ST', '62nd ST', \
                                '63rd ST', '65th ST', '67th ST', '68th ST', '72nd ST', 'La Jolla Scenic Drive North', 'Alderley ST', \
                                'Ventura PL', 'Auto Circle', 'Auto Circle', 'Auto Circle', 'Avenida De La Fuente', 'Avenida Del Rio', \
                                'Vista ST', 'Bob Wilson DR', 'Bernardo Heights Pkwy', 'Bernardo Heights Pkwy', 'Beyer Way', \
                                'Blue Lake DR', 'Babcock ST', 'Britannia Boulevard', 'Clara Lee Avenue', 'Calle Del Oro', \
                                'Calle Primera', 'Calle De Las Rosas', 'Calle De Las Rosas', 'Camino Del Rio North', 'Camino Del Arroyo', \
                                'Camino De La Reina', 'Camino De La Plaza', 'Camino De La Reina', 'Camino Del Rio North', \
                                'Camino Del Rio South', 'Camino Del Rio West', 'Camino Del Sur', 'Camino Del Sur', 'Carmel Creek RD', \
                                'Cedar ST', 'Central Plaza', 'Clay Avenue', 'College Grove DR', 'College Grove DR', 'College Grove Way', \
                                'College Grove Way', 'Costa Verde Boulevard', 'Del Mar Heights RD', 'Datsun ST', 'Voyager Cir', \
                                'Del Sur Boulevard', 'Derrick DR', 'Dowdy DR', 'Dubois DR', 'Evening Creek Drive E', 'Evening Creek Drive S', \
                                'Evening Creek Drive N', 'Evening Creek Drive S', 'Executive Drive', 'Fairbrook RD', 'Federal Boulevard', \
                                'Garnet Avenue', 'Gemini Avenue', 'Genesee Avenue', 'East Harbor Drive', 'North Harbor Drive' ,\
                                'Harbor Island Drive', 'Hawthorn ST', 'Highland Ranch Road', 'Hotel Circle North', 'Hotel Circle North', \
                                'Rancho Mission RD', 'Rancho Mission RD', 'Juniper ST', 'La Jolla Scenic Drive South', 'Grand AV', \
                                'Lise AV', 'Main ST', 'Miramar PL', 'Tern Drive', 'Tern Drive', 'University AV', '32nd ST', 'Otay Mesa RD',\
                                'Pacific Center Boulevard', 'Palm AV', 'Park Boulevard', 'Park Boulevard', 'Park Ridge Boulevard', \
                                'Park Ridge Boulevard', 'Park Row', 'Paseo Del Sur', 'Pottery Park Driveway', 'Prestwick Drive', \
                                'Qualcomm Way', 'Inman ST', '6th AV', 'Rappahannock AV', 'Reed AV', 'Rue De Anne', 'Santa Fe ST', \
                                'Soledad Park Road', 'Valley Centre Drive', 'Virginia AV', 'Valley Centre DR', 'Valley Centre DR', \
                                'Waterloo AV', 'Wing ST', 'West Point Loma Boulevard']

        self.corrected_end_roads = ['54th ST', '1st AV', 'Beyer Way', '1st AV', '2nd AV', '3rd AV', '4th AV', '5th AV', '6th AV', '7th AV', \
                            '8th AV', '9th AV', '1st AV', '54th ST', '14th ST', '16th ST', '17th ST', '25th ST', '25th ST', \
                            'Imperial AV', '26th ST', '27th ST', '27th ST', '27th ST', '28th ST', '29th ST', '29th ST', \
                            '30th ST', '30th ST', '32nd ST', '32nd ST', '33rd ST', '34th ST', '35th ST', '38th ST', '39th ST', '41st ST', \
                            '42nd ST', '43rd ST', '44th ST', '45th ST', '46th ST', '47th ST', '48th ST', '50th ST', 'Monroe AV', \
                            '51st ST', '52nd ST', '53rd ST', '54th ST', '54th ST', '55th ST', '58th ST', '62nd ST', '63rd ST', '65th ST', \
                            '68th ST', '69th ST', '69th ST', '70th ST', 'Albemarle Street', '6th AV', '38th ST', '42nd ST', '43rd ST', \
                            '50th ST', '52nd ST', '52nd ST', 'Grand AV', 'Mission Boulevard', '38th ST', '42nd ST', '52nd ST', \
                            '52nd ST', 'Amity Street', 'Auto Circle', 'Auto Circle', 'Avenida de la Fuente', 'Avenida de la Playa', \
                            'Bob Wilson DR', 'Balboa AV', 'Bernardo Heights Pkwy', 'Bernardo Plaza Drive', 'Black Mountain Road', \
                            'Babcock ST', 'Broadway', 'C ST', 'Calle Tres Lomas', 'Camino Del Sur', 'Carmel Creek RD', \
                            'Camino de la Costa', 'Camino de la Costa', 'Camino de la Reina', 'Camino Del Norte', 'Camino Del Norte', \
                            'Camino de la Plaza', 'Camino Santa Fe', 'Camino Del Sur', 'Truman St', 'Truman St', \
                            'Truman St', 'Cather Avenue', 'Chesapeake Drive', 'Coast Boulevard South', 'College Grove DR', \
                            'Del Mar Heights RD', 'Del Mar Heights RD', 'Darwin Avenue', 'Del Sur Boulevard', 'Miramar Road', '30th ST', \
                            'E ST', 'Evening Creek Drive N', 'Evening Creek Drive S', 'Franklin Ridge Road', 'Friars Road', \
                            'Friars Road', 'Front ST', 'Front ST', 'Genesee Avenue', 'Girard Avenue', 'Park Boulevard', 'Harbor Drive', \
                            'Harbor Island Drive', 'Harris Plant Road', 'Highland Ranch Road', 'Howard Avenue', 'Kearny Mesa Road', \
                            'Lake Ben Avenue', 'Lake Murray Boulevard', 'Clara Lee Avenue', 'Lincoln Avenue', 'Market ST', \
                            'Kettner Blvd', 'Miramar College Drwy', 'Overland Avenue', 'Mission City Parkway', \
                            'North Torrey Pines Road', 'National Avenue', 'University Avenue', 'National City Boulevard', \
                            'Oberlin Drive', 'Old Rancho Santa Fe Road', 'Rancho Santa Fe Road', 'South Rancho Santa Fe Road', \
                            'Ocean Boulevard', 'Orchard Avenue', 'Otsego Drive', 'Overland Avenue', 'Overland Avenue', \
                            'Overland Avenue', 'Overland Avenue', 'Pacific Highway', 'Park Boulevard', '11th AV', '12th AV', '12th AV', \
                            'Park Boulevard', 'Park Ridge Blvd', 'Pepper Drive', 'Piccard Avenue', 'Poyntell Circle', \
                            'Valley Centre Drive', 'Regents Park Row', 'Westover PL', 'Sandrock Road', 'Garnet AV', 'Heritage ST',\
                            'Smythe Avenue', 'Soledad Mountain Road', 'Sorrento Valley Boulevard', 'South Lane', 'South Lane', \
                            'Avenida Del Mexico', 'Torrey Ridge Drive', 'Torrey Ridge Drive', 'Toyne Street', 'Twin Lake Drive', \
                            'University AV', 'Upas Street', 'Valley Centre Drive', 'Village Place', 'Valley Centre Drive', \
                            'West Point Loma Boulevard', 'West Point Loma Boulevard', '43rd ST', 'University AV', 'Westview Parkway']

def read_csv_file(_file):
    '''
    This function reads a CSV file from the datasets folder.
    It also adds two additional columns to the dataframe to separate the starting and ending roads.

    INPUTS:
        _file: str
            - Contains the path to the CSV file to read.
    
    RETURNS:
        df: pd.DataFrame
    '''

    assert isinstance(_file, str)  # file must be a path given as a string
    assert '../datasets' in _file  # file must be in the datasets folder 
    assert '.csv' in _file         # file must be in a csv format

    df = pd.read_csv(_file)

    # Adding two new columns to separate the starting and ending streets from original dataset
    df[['start_loc', 'end_loc']] = df['limits'].str.split(' - ', 1, expand=True)

    return df

def get_invalid_street_names(df, geolocator, log_start_streets, log_end_streets):
    '''
    This function gets a list of invalid street names from the dataset
    and stores it to a text file.

    INPUTS:
        df: pd.DataFrame
        geolocator: Nominatim
        log_start_streets: str
        log_end_streets: str

    RETURNS:
        log_start_streets: str
            - Text file containing the list of all the invalid starting street names
        log_end_streets: str
            - Text file containing the list of all the invalid ending street names
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(geolocator, Nominatim)
    assert isinstance(log_start_streets, str)
    assert isinstance(log_end_streets, str)

    # txt files must be in the logs folder
    assert '../logs' in log_start_streets and '../logs' in log_end_streets

    start_roads_to_fix = set()
    end_roads_to_fix = set()

    # List of all the combinations of starting and ending locations
    l = list(df.groupby(['start_loc', 'end_loc'])['total_count'].sum().index)

    for i in tqdm(range(0, len(df['limits'].unique()))):

        # Checking whether a street name generates valid coordinates
        try:
            start_loc = geolocator.geocode(f"{l[i][0]}, San Diego, CA")
        # The geocoding function throws an exception for invalid street inputs, so this 
        # handles those cases by logging those street names
        except:
            print('Invalid Starting Street Name found!')
            start_roads_to_fix.add(l[i][0])

        # Checking whether a street name generates valid coordinates
        try:
            end_loc = geolocator.geocode(f"{l[i][1]}, San Diego, CA")

        # The geocoding function throws an exception for invalid street inputs, so this 
        # handles those cases by logging those street names
        except:
            print('Invalid Ending Street Name found!')
            end_roads_to_fix.add(l[i][1])

    # Store the invalid starting street names to a txt file
    with open(log_start_streets, 'a+') as file:
        for i in start_roads_to_fix:
            file.write(str(i)+"\n")

    # Store the invalid ending street names to a txt file
    with open(log_end_streets, 'a+') as file:
        for i in end_roads_to_fix:
            file.write(str(i)+"\n")

    return start_roads_to_fix, end_roads_to_fix

def invalid_streets_from_file(invalid_start_roads, invalid_end_roads):
    '''
    This function extracts the invalid streets from the txt files and 
    stores them in a set

    INPUTS:
        invalid_start_roads: str
            - path to txt file containing the list of invalid starting roads
        invalid_end_roads: str
            - path to txt file containing the list of invalid ending roads

    RETURNS:
        start_roads_to_fix: Set<str>
        end_roads_to_fix: Set<str>
    '''

    assert isinstance(log_start_streets, str)
    assert isinstance(log_end_streets, str)

    # txt files must be in the logs folder
    assert '../logs' in log_start_streets and '../logs' in log_end_streets
    
    # Initializing sets to store the invalid street names
    start_roads_to_fix = set()
    end_roads_to_fix = set()

    # Store invalid street names to the sets
    with open(invalid_start_roads, 'r') as f:
        for line in f:
            start_roads_to_fix.add(line.strip('\n'))

    with open(invalid_end_roads, 'r') as f:
        for line in f:
            end_roads_to_fix.add(line.strip('\n'))

    return start_roads_to_fix, end_roads_to_fix

def generate_lookup_tables(start_roads_to_fix, end_roads_to_fix, fixed_streets):
    '''
    This function maps the incorrect street names to the corresponding correct names.
    This step is implemented to get the Latitude and Longitudes of the steets.

    INPUTS:
        start_roads_to_fix: Set<str>
        end_roads_to_fix: Set<str>
        fixed_streets: FixStreetNames

    RETURNS:
        start_lookup_table: Dict<str>
        end_lookup_table: Dict<str>
    '''

    assert isinstance(start_roads_to_fix, set)
    assert isinstance(end_roads_to_fix, set)
    assert isinstance(fixed_streets, FixStreetNames)

    # sorting the incorrect street values because the fixed street names are in this order
    start_roads_list = sorted(list(start_roads_to_fix))
    end_roads_list = sorted(list(end_roads_to_fix))

    start_lookup_table = {}
    end_lookup_table = {}

    # Populating the lookup tables/ mapping between the incorrect street values with the correct ones
    for i in range(0, len(start_roads_list)):
        start_lookup_table[start_roads_list[i]] = fixed_streets.corrected_start_roads[i]

    for i in range(0, len(end_roads_list)):
        end_lookup_table[end_roads_list[i]] = fixed_streets.corrected_end_roads[i]

    return start_lookup_table, end_lookup_table

def generate_coordinates(df, geolocator, start_lookup_table, end_lookup_table):
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
    assert isinstance(start_lookup_table, dict)
    assert isinstance(end_lookup_table, dict)
    
    # Aggregating all the starting and ending roads and summing up all the vehicle counts
    l = list(df.groupby(['start_loc', 'end_loc'])['total_count'].sum().index)
    s = df.groupby(['start_loc', 'end_loc'])['total_count'].sum()

    # Initializing new dataframe that contains the relevant attributes and coordinates
    ef = pd.DataFrame(columns=['start_loc', 'end_loc', 'lat_x', 'lon_x',\
                            'lat_y', 'lon_y', 'count'])


    for i in tqdm(range(0, len(l))):

        # Checking if geocoding a starting street name generates valid coordinates
        try:
            if l[i][0] in start_lookup_table:
                start_loc = geolocator.geocode(f"{start_lookup_table[l[i][0]]}, San Diego, CA")
            elif l[i][1] in end_lookup_table:
                start_loc = geolocator.geocode(f"{end_lookup_table[l[i][0]]}, San Diego, CA")
            else:
                start_loc = geolocator.geocode(f"{l[i][0]}, San Diego, CA")
        
        # If the geocoding throws an exception, leave the entries of the coordinates empty
        except:
            print('Invalid street name at start loc!')
            lat_x = np.nan
            lon_x = np.nan

        # Checking if geocoding a ending street name generates valid coordinates
        try:
            if l[i][1] in end_lookup_table:
                end_loc = geolocator.geocode(f"{end_lookup_table[l[i][1]]}, San Diego, CA")
            elif l[i][1] in start_lookup_table:
                end_loc = geolocator.geocode(f"{start_lookup_table[l[i][1]]}, San Diego, CA")
            else:
                end_loc = geolocator.geocode(f"{l[i][1]}, San Diego, CA")

        # If the geocoding throws an exception, leave the entries of the coordinates empty
        except:
            print('Invalid street name at end loc!')
            lat_y = np.nan
            lon_y = np.nan

        # Leave the coordinate entries empty if the geocoding value for a street name returns None
        if start_loc is None:
            lat_x = np.nan
            lon_x = np.nan
        else:
            lat_x = start_loc.latitude
            lon_x = start_loc.longitude

        if end_loc is None:
            lat_y = np.nan
            lon_y = np.nan
        else:
            lat_y = end_loc.latitude
            lon_y = end_loc.longitude

        # Gather the street names and their coordinates to append to the new dataframe
        ef.loc[i] = [l[i][0], l[i][1], lat_x, lon_x, lat_y, lon_y, s.iloc[i]]

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


if __name__ == '__main__':
    #create an ArgumentParser object
    parser = argparse.ArgumentParser\
                (description = 'Specify the file names for the preprocessed dataset'\
                               'and logging street names')
    
    #declare arguments
    parser.add_argument('-i','--input_dir', type = str, required = True, help='file name of raw dataset')
    parser.add_argument('-o','--output_dir', type = str, required = True, help='file name of preprocessed dataset')
    parser.add_argument('-s','--log_start_streets', type=str, required=True, help='Path to invalid start street names txt file')
    parser.add_argument('-e','--log_end_streets', type=str, required=True, help='Path to invalid end street names txt file')
    parser.add_argument('--get_invalid_streets', type=bool, required=False, help='Log invalid street names from raw dataset')
    args = parser.parse_args()

    # initializing variables from command line arguments
    input_dir = args.input_dir
    output_dir = args.output_dir
    log_start_streets = args.log_start_streets
    log_end_streets = args.log_end_streets
    get_invalid_streets = args.get_invalid_streets


    # Initializing geocoding to get coordinates
    geolocator = Nominatim(user_agent='Lat-Lon-conversion')
    fixed_streets = FixStreetNames()

    df = read_csv_file(input_dir)

    # This logs the invalid street names to a txt file
    if get_invalid_streets is True:
        get_invalid_street_names(df, geolocator, log_start_streets, log_end_streets)
        print('Successfully logged invalid start streets to {}'.format(log_start_streets.replace('../', '')))
        print('Successfully logged invalid end streets to {}'.format(log_end_streets.replace('../', '')))

    # Fixing invalid street names to valid ones and
    # Generating Latitude and Longitude coordinates for each starting and ending streets
    start_roads_to_fix, end_roads_to_fix = invalid_streets_from_file(log_start_streets, log_end_streets)
    start_lookup_table, end_lookup_table = generate_lookup_tables(start_roads_to_fix, end_roads_to_fix, fixed_streets)
    ef = generate_coordinates(df, geolocator, start_lookup_table, end_lookup_table)

    # Exporting preprocessed data
    export_data_to_csv(ef, output_dir)
    print('Successfully exported dataset to {}'.format(output_dir.replace('../', '')))
