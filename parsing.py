#movieFormat
# python ./parsing.py
def main():

	readFile();
	print(movieDictionary["1"]);

# Reading a .DAT file line by line
# passing this line to parseLine function for storing information
def readFile():

	f = open("ratings1.dat","r")
	for line in f:
	    parseLine(line[:-1]);

# This function parse the line meaning convert String value to proper
# Format. Extracting attributes from Line and then storing them in to 
# Dictionary.
def parseLine(line):
	entryInFile = line.split("::");
	fieldsDictionary = {};
	
	splitEntry = entryInFile[1].split("(");
	fieldsDictionary['NAME'] = splitEntry[0].strip();
	fieldsDictionary['YEAR'] = splitEntry[1].strip()[:-1];
	fieldsDictionary['GENRE'] = entryInFile[2].strip().split("|");

	movieDictionary[entryInFile[0]] = fieldsDictionary;


# Gloabl variable which stores Movie information.
movieDictionary = {};
main();