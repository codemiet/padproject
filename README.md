# padproject
Project repository for the subject "Programming and Databases". 

The starting point of the project task is a CSV source file containing various meteorological records. These data come from several weather stations in Portugal and were collected in this CSV file. Afterwards the Python program to be created ensures that the records are read in and errors within the input data set are corrected. For example, duplicate data sets or incorrect measured values are corrected. The cleaned data is then persistently loaded into a database and can then be queried. This is intended to create automated analyses, for example to determine average temperatures or to calculate maximum and minimum values within the data.

Installation:
1. Install python in version 3
2. Navigate to project folder
3. Start the application: `python3 main.py`
4. Configure the parameters