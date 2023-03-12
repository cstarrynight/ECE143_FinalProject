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

- [insert src folder name]: all of the code
    - [insert San Diego Traffic Volumes (2007-2022) dataset]
    - [insert San Francisco Traffic Count dataset]
    - [insert Citibike Data (New York & New Jersey) dataset]
- [insert datasets folder name]: original datasets
- [insert jupyter ntbk name] * 4: takes SD data and cleans for plotting | plots SD | plots SF | plots NJ & NY


- **[insert src folder name]**: 
# Usage
To run the project...

1. execute [insert python file here] from [insert src direcotry] for data manipulation to output [insert .csv file here]
2. run [input corresponding jupyter ntbk] to output [insert visualization name]
    .
    .
    .
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

Can be installed via the terminal such as:
`pip install numpy`


# References
**Data:**  
[San Diego Traffic Volumes (2007-2022)](https://data.sandiego.gov/datasets/traffic-volumes/)  
[San Francisco Traffic Count](https://www.sfmta.com/reports/sfmta-traffic-count-data)   
[Citibike Data (New York and New Jersey)](https://s3.amazonaws.com/tripdata/index.html)

