# Choice on wheels: What tips the scale between Uber and other rides?

This project was developed as part of the Machine Learning course in the Master's program at the Faculty of Mathematics, University of Belgrade.

## Authors
1. Marija Markovic 1011/2023
2. Marko Savic 1016/2023

## Project ideas and goals

The goal of this project is to analyze data from both Uber and non-Uber rides to identify differences in demand, understand the factors that influence clients' choices between these options, and explore opportunities for improvement. The insights gained from this analysis can be leveraged to enhance business strategies, ultimately benefiting both clients and companies.

## Dataset

The dataset used in this project is available for download from [Kaggle](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city/data).  
You can explore more about the dataset there and discover interesting articles that resulted from its analysis.

   ### Short summary 
   The dataset has information on about 4.5 million Uber pickups in New York City from April 2014 to September 2014 and 14 million more from January 2015 to June 2015.  
   Trip-level data on 10 other for-hire vehicle (FHV) companies, as well as aggregated data for 329 FHV companies, is also included.


## Required Installations

1. **Git Large File Storage**  
   Download Git LFS [here](https://git-lfs.com/) and follow the installation instructions.  
   **Note:** Some datasets used in this project are large and managed with Git LFS.  
   To ensure that you download all the necessary files, please use `git lfs pull` instead of `git pull`.


## Required Libraries

2. **numpy**
3. **matplotlib**
4. **pandas**
5. **seaborn**

```bash
pip install numpy matplotlib pandas seaborn
```
6. **basemap**
### On Linux (Debian/Ubuntu)
```bash
sudo apt-get install libgeos-dev
pip install basemap basemap-data-hires
```
### On Windows or Mac
```bash
pip install basemap basemap-data-hires
```
## Code summary
### Notebooks
1. Analysis of Uber trips from April to September 2014
2. Analysis of non-uber for-hire vehicle trips from January to August 2015
3. Analysis of Uber trips from January to June 2015
4. Analysis of American trips from July to September 2014
5. Analysis of Lyft trips from July to September 2014 
6. Analysis of Skyline trips from July to September 2014 
7. Analysis of Dial trips from July to September 2014 
* Datasets of the rest of the Non-hire-vehicle were not possible to load due to a coding mistake
### Scrips
1. extract_data : Script for extraction of time-date specific data from dataset
2. plot_rides : Script with frequently used plot functions


