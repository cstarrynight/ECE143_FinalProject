Regarding GitHub Repository - Well documented, reusable Python module targeted at solving your proposal task. Follow all good coding practices and conventions discussed in class

Include all your code as .py files (therefore remember to write modular code to make life easier) 
Include 1 Jupyter notebook which shows all the visualizations you generated for your presentation.
Include a readme file that explains your file structure, how to run your code, and name all third-party modules you are using. 
Include the final presentation as a pdf file


# City Visualization of Traffic Data Project Description

Our final project for ECE 143 @ UC San Diego focused on city visualization of traffic data. Motivated by visualizing vehicle traffic in various cities, identifying popular hotspot destinations and any potential hotspots in cities, and estimated time to get to a destination, we visualized and analyzed traffic data on that gave insight into...

1. Bike Station Placement in New York
2. Tourism in San Diego 
3. San Diego Road Traffic
4. San Diego Hiking

Based on the data from San Diego Traffic Volumes (2007-2022), we identified four spots with high concentrations of traffic: Downtown, Northpark, Black Mountain, and Balboa Ave. Surprisingly, the beach was not one a hotspot based on the visualization of the dataset. From these, we identified Downtown and Northpark as being hotspots due to tourism as these locations have bars, clubs, restaurants, and book stores that are attractive destinations. Another hotspot is Black Mountain, a hiking spot; based on the hotspot data visualization, the spot is potentially a very attractive place to hike. Last of the four was Balboa Avenue; In a deep dive look into google maps, we found that this region has a lot of big comapnies located here such as those under the Department of Defense and Solar Turnbines, banks, and restaurants that would normally be frequented. 

# File Structure

- `src/`: This folder contains all the code (python scripts and notebooks)
    - `process_sd_data.py`: Preprocessing script for San Diego Traffic Volumes (2007-2022) dataset
    - `process_sd_visuals.ipynb`: Script that takes processed data and generates coordinate data for visualization
    - `display_sd.ipynb`: Script that displays the SD map

    - `process_sf_data.py`: Preprocessing script for San Francisco Traffic Count dataset
    - `process_sf_visuals.ipynb`: Script that takes processed data and generates coordinate data for visualization specifically for the SF dataset
    - `display_sf.ipynb`: Script that displays the SF map

    - `process_ny.ipynb`: Script that takes processed data and generates coordinate data for visualization specifically for the NY dataset. Code is based off: https://python.plainenglish.io/how-to-build-route-heatmaps-in-python-ebac363471d7
    - `display_ny.ipynb`: Script that displays the NY map. Code is based off: https://python.plainenglish.io/how-to-build-route-heatmaps-in-python-ebac363471d7

    

- `processed_datasets/`: all the processed csv files
    - `sd_data_processed.csv`: original dataset gets processed into this .csv file
    - `sd_cleaned.csv`: this is sd_data_processed.csv after removing unusable datapoints or NaN values
    - `sd_final.csv`: this is the final csv file containing all coordinates to be plotted for display_sd.ipynb
    
    - `sf_data_processed.csv`: original sf dataset gets processed into this .csv file
    - `sf_cleaned.csv`: this takes sf_data_processed.csv and removes unusable or empty data values
    - `sf_final.csv`: this is the final csv file containing all coordinates to be plotted for display_sf.ipynb

    - `ny_processed.csv`: new york data after being processed from the original ny citibike dataset
    - `ny_final.csv`: this is the final csv file containing all coordinates to be plotted for display_ny.ipynb



- `datasets/`: original datasets
    - `traffic_counts_datasd_v1.csv`: San Diego Traffic Volumes (2007-2022) dataset
    - `sfmta_corridor_counts_2014-2018.csv`: San Francisco Traffic Count dataset
    - `JC-202209-citibike-tripdata.csv`: New York citibike dataset



# Usage
To display the SD map

1. run process_sd_visuals.ipyn

    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "sd_final.csv" is already in ./src

2. execute display_sd.ipynb from ./src which displays the data from sd_final.csv

end

To display the SF map

1. run process_sf_visuals.ipynb
        
    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "sf_final.csv" is already in ./src

2. execute display_sf.ipynb from ./src which displays the data from sf_final.csv

end

To display the NY map

1. run process_ny.ipynb
        
    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "ny_final.csv" is already in ./src
    
2. execute display_ny.ipynb from ./src which displays the data from ny_final.csv

end

# Installations

**Before running this project, please install the following:**

- pandas
- numpy
- plotly
- requests
- tqdm
- folium

**These packages are built-in. No install needed:**

- sys
- ast
- time

**Versions used:**

- Python 3.11.1
- pandas 1.5.3
- numpy 1.24.1
- plotly 5.13.1
- requests 2.28.2
- tqdm 4.65.0
- folium 0.14.0

All of the dependencies can be installed in the terminal using the command:

```
pip install -r requirements.txt
```

# Preprocessing Datasets

## Preprocessing the San Diego Traffic Volumes Dataset

In this section, we will be preprocessing the San Diego traffic dataset. The raw dataset is located in `datasets/traffic_counts_datasd_v1.csv`. 

To preprocess this dataset, we will run the script `process_sd_data.py` that is located in the `src/` folder

1. Navigate to the src folder
```
cd src
```

2. In order to preprocess this dataset, we will run the `process_sd_data.py`. Make sure to also include the following flags:

    i. `--input_dir`: Specify the path to the raw dataset to be processed.

    ii. `--output_dir`: Specify the path to the new preprocessed dataset. Be sure to also include the csv file name.

    iii. `--log_start_streets`: Specify the path to the text file that contains incorrect starting street names.

    iv. `--log_end_streets`: Specify the path to the text file that contains the incorrect ending street names.

    v. `--get_invalid_streets` (Optional): Boolean flag. Set this flag to True to get the list of incorrect starting and ending street names. 

    **NOTES:** 
    
        a. The directory paths must be relative to the path from the `src/` folder since that is our current directory.
        
        b. Running the following proprocessing script can take about 1.5 hours since it calls the geocoding API which takes time to compute.

    Here is an example of how to run the code to preprocess the San Diego traffic dataset.

    ```
    python process_sd_data.py --input_dir ../datasets/traffic_counts_datasd_v1.csv --output_dir ../processed_datasets/sd_data_processed.csv --log_start_streets ../logs/start_roads_to_fix.txt --log_end_streets ../logs/end_roads_to_fix.txt
    ```
    
    The final preprocessed San Diego dataset will be located in the `processed_datasets` folder under the name `sd_data_preprocessed.csv`. 

## Preprocessing the San Francisco Traffic Counts Dataset

In this section, we will be preprocessing the San Francisco traffic dataset. The raw dataset is located in `datasets/sfmta_corridor_counts_2014-2018.csv`.

We will be using the same method we used to preprocess the San Diego dataset.

To preprocess this dataset, we will run the script `process_sf_data.py` that is located in the `src/` folder

1. Navigate to the src folder
```
cd src
```

2. In order to preprocess this dataset, we will run the `process_sd_data.py`. Make sure to also include the following flags:

    i. `--input_dir`: Specify the path to the raw dataset to be processed.

    ii. `--output_dir`: Specify the path to the new preprocessed dataset. Be sure to also include the csv file name.

    **NOTES:** 
    
        a. The directory paths must be relative to the path from the `src/` folder since that is our current directory.
        
        b. Running the following proprocessing script can take about 1.5 hours since it calls the geocoding API which takes time to compute.

    Here is an example of how to run the code to preprocess the San Francisco traffic dataset.

    ```
    python3 process_sf_data.py --input_dir ../datasets/sfmta_corridor_counts_2014-2018.csv --output_dir ../processed_datasets/sf_data_processed.csv
    ```
    
    The final preprocessed San Francisco dataset will be located in the `processed_datasets` folder under the name `sf_data_preprocessed.csv`. 


# References
**Data:**  
[San Diego Traffic Volumes (2007-2022)](https://data.sandiego.gov/datasets/traffic-volumes/)  
[San Francisco Traffic Count](https://www.sfmta.com/reports/sfmta-traffic-count-data)   
[Citibike Data (New York and New Jersey)](https://s3.amazonaws.com/tripdata/index.html)

