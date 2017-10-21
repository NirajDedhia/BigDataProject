# Program to converts movie data in .DAT
# file to .csv file.
# Author : Niraj Dedhia
# python ./parsing.py

# This is the main function which initiates the program
# Fetch the data from movies and ratings file and store 
# them in a dictionary then convert that dictionary in 
# to .csv file.
def main():

	#readFileForParsing("../BIGFILES/movies.dat");
	#readFileForParsing("../BIGFILES/ratings.dat",1);
	readFileForParsing("movies.dat");
	readFileForParsing("ratings.dat",1);
	calculateAverageRating();
	print(movieDictionary);
	

# Reads the .DAT file line by line
# Based on the option it reads movies and rating files 
# respectively.
# Forwards the line to parse it and to fetch the information
def readFileForParsing(fileName, option=0):

	f = open(fileName,"r");
	if(option == 0):
		for movie in f:
			storeMovieInDictinary(movie[:-1]);
	else:
		for rating in f:
			storeRatingsInDictinary(rating[:-1]);
	

# Parse the line having movie information and
# stores the fetched data in to dictionary object.
def storeMovieInDictinary(movie):
	fieldsDictionary = {};
	movieAttributes = movie.split("::");
	splitEntry = movieAttributes[1].split("(");

	fieldsDictionary['NAME'] = splitEntry[0].strip();
	fieldsDictionary['YEAR'] = splitEntry[1].strip()[:-1];
	fieldsDictionary['GENRE'] = movieAttributes[2].strip().split("|");
	fieldsDictionary['RATINGS'] = [];

	movieDictionary[movieAttributes[0]] = fieldsDictionary;


# Parse the line having ratings information and
# stores them in dictionary object.
def storeRatingsInDictinary(rating):
	fileAttributes = rating.split("::");
	movieDictionary[fileAttributes[1]]['RATINGS'].append(float(fileAttributes[2]));


# Thi function calculates the average ratings for
# every movie
def calculateAverageRating():
	for movieID in movieDictionary:
		movieDictionary[movieID]['RATING'] = float(average(movieDictionary[movieID]['RATINGS']));


# Calculates the average for given list
def average(list):
	lengthOfList = len(list);

	if(lengthOfList == 0):
		return 0;

	result = 0;
	for element in list:
		result += float(element);
	result /= lengthOfList;

	return result;


# Global variable which stores Movie information.
movieDictionary = {};
main();
