Reader Files on Meteorite Landings Data 

These files read meteorite landings data provided by NASA. They output a set of summary statistics, including (in order), the average mass of the meteorites (for that data set), the hemisphere in which the meteorites landed, and the amount (in %) each hemisphere shows up.

These programs accept the file name as an argument in the commandline. 
To run these scripts, input into the commandline "python3 ml_(type of file)_reader.py (dataset file name)"
For example, if you wanted to run the json file, you would type (into the commandline): python3 ml_json_reader.py Meteorite_Landings.json

Once you run this command a set of numbers will be output. The first number printed out on the screen is the average mass of the meteorites, the second set of numbers is the coordinates of all the meteorites, the third set of information provides not the coordinates of the meteorites but the hemisphere's in which they landed, and finally, the last set of information provides insight into where (what hemisphere) meteorites land the most by tying percentages to each hemisphere!
