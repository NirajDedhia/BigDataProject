# Program to converts movie data in .DAT
# file to .csv file.
# Author : Niraj Dedhia
# python ./parsing.py

import xlwt;

# This is the main function which initiates the program
# Fetch the data from movies and ratings file and store 
# them in a dictionary then convert that dictionary in 
# to .csv file.
def main():

	# readFileForParsing("../BIGFILES/movies.dat");
	# readFileForParsing("../BIGFILES/ratings.dat",1);
	readFileForParsing("movies.dat");
	readFileForParsing("ratings.dat",1);
	calculateAverageRating();
	covertToExcel();
	#print(movieDictionary);
	

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
	fieldsDictionary['GENRE'] = movieAttributes[2].strip();
	fieldsDictionary['RATINGS'] = [];

	movieDictionary[movieAttributes[0]] = fieldsDictionary;


# Parse the line having ratings information and
# stores them in dictionary object.
def storeRatingsInDictinary(rating):
	fileAttributes = rating.split("::");
	movieDictionary[fileAttributes[1]]['RATINGS'].append(float(fileAttributes[2]));


# This function calculates the average ratings for
# every movie
def calculateAverageRating():
	for movieID in movieDictionary:
		movieDictionary[movieID]['RATING'] = float(average(movieDictionary[movieID]['RATINGS']));


# This function converts dictionary to excel file
def covertToExcel():
	excelFile = xlwt.Workbook(encoding="utf-8");
	sheet = excelFile.add_sheet("Sheet");

	sheet.write(0, 0, "Movie ID");
	sheet.write(0, 1, "Movie Name");
	sheet.write(0, 2, "Movie Rating");
	sheet.write(0, 3, "Movie Genere");

	row = 1;

	for movieID in movieDictionary:
		sheet.write(row, 0, movieID);
		sheet.write(row, 1, movieDictionary[movieID]['NAME']);
		sheet.write(row, 2, movieDictionary[movieID]['RATING']);
		sheet.write(row, 3, movieDictionary[movieID]['GENRE']);
		row += 1;

	excelFile.save("Movie_Dataset_File");
		


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
