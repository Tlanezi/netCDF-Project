# TAMA Project "Runnoff App"

This project was developed as final project for the course Python Programming for Water Resources Engineering and Research
TAMA project is a GUI (Graphical User Interface) based on the netcdf file provided in GRUN platform by [ETH Zurich](https://www.research-collection.ethz.ch/handle/20.500.11850/324386)
GRUN: an observation-based global gridded runoff dataset from 1902 to 2014).       


## Getting Started
Runnoff App will help you to extract runoff data from specific coordinates and retrieves a excel file with the data for the required coordinates.

These instructions will get you a copy of the project up and running on your local machine for testing purposes. 
Get ready by cloning the exercise repository:

```
git clone https://github.com/Tlanezi/1st-Repo.git
```                                 

### Prerequisites
*Python* libraries: *tkinter*, *numpy*, and *pandas*.
Install create a new environment and install flusstools

```
-m pip install flusstools
```

Also is required to install a netcdf reader

```
-m pip install netCDF4
```

Finally is requiered for you to download the data (Zip format) from [GRUN dataset from 1902-2014](https://www.research-collection.ethz.ch/handle/20.500.11850/324386)
It is important not to change the name of the document once downloaded

![git](https://github.com/Tlanezi/netCDF-Project/blob/a0ce7fa0444301056260bcfa5df83bc9bf5c7afc/ETH.png)

IMPORTAT!! 
Save the document directly in the Gru folder

***ADDimage!

### What is a NetCDF file?

NetCDF (network Common Data Form) is a file format for storing multidimensional scientific data (variables) such as temperature, years, runoff, wind speed, etc.
Many organizations and scientific groups in different countries have adopted netCDF as a standard way to represent some forms of scientific data.

GRUN is an observation-based global gridded runoff dataset. The data is stored in a single NetCDFv4 file at monthly resolution covering the period 1902-2014. 


## Running the Runnoff App

Here is explained how to run the RunnoffApp

1) Run gui.py

![](https://github.com/Tlanezi/netCDF-Project/blob/6c94ac9257e5323ea56fdf1608e57410ceb61058/gui.png)

2) Select your excel file with the coordinates
included in the program there is a file named "points.xlsx"
press the yellow button to select the file

![](https://github.com/Tlanezi/netCDF-Project/blob/97bbe0681d83af8ef594883f1685ab5c70164062/runnoffapp.png)

3) Select the desired folder where the output file will be saved  

4) Press "START"




### B

Explain what these tests test and why

```
Give an example
```


## Authors

* **Tlanezi Martinez**  
* **Areeb Mohammed**



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details




