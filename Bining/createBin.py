import xlwt;
import csv;

def main():
	readFileForParsing("movies.csv");
	readFileForParsing("ratings.csv",1);
	calculateAverageRating();
	covertToExcel();

def readFileForParsing(fileName, option=0):
	f = open(fileName,"r");
	if(option == 0):
		for movie in f:
			storeMovieInDictinary(movie);
	else:
		for rating in f:
			if('movieId' not in rating):
				storeRatingsInDictinary(rating);

def storeMovieInDictinary(movie):
	fieldsDictionary = {};
	if('"' in movie):
		temp = movie.split('"');
		movieAttributes = [];
		movieAttributes.append(temp[0][:-1]);
		movieAttributes.append(temp[1]);
		movieAttributes.append(temp[2][1:]);
	else:
		movieAttributes = movie.split(",");
	splitEntry = movieAttributes[1].split("(");

	fieldsDictionary['ID'] = movieAttributes[0].strip();
	fieldsDictionary['NAME'] = splitEntry[0].strip().replace("'","");
	fieldsDictionary['YEAR'] = splitEntry[-1].strip()[:-1];
	fieldsDictionary['GENRE'] = movieAttributes[2].rstrip();
	fieldsDictionary['CODE'] = bining(movieAttributes[2].rstrip());
	fieldsDictionary['RATINGS'] = [];

	movieDictionary[movieAttributes[0]] = fieldsDictionary;

def bining(generes):
	genresList = generes.split("|");
	bin1 = 0;
	bin2 = 0;
	bin3 = 0;
	bin4 = 0;
	bin5 = 0;
	for genre in genresList:
		temp = genre.rstrip();
		if temp.upper() in bins[1]:
			bin1+=1;
		if temp.upper() in bins[2]:
			bin2+=1;
		if temp.upper() in bins[3]:
			bin3+=1;
		if temp.upper() in bins[4]:
			bin4+=1;
		if temp.upper() in bins[5]:
			bin5+=1;
	code = str(1) + str(bin1) + str(bin2) + str(bin3) + str(bin4) + str(bin5);
	return code;

def storeRatingsInDictinary(rating):
	fileAttributes = rating.split(",");
	movieDictionary[fileAttributes[1]]['RATINGS'].append(float(fileAttributes[2]));

def calculateAverageRating():
	for movieID in movieDictionary:
		movieDictionary[movieID]['RATING'] = float(average(movieDictionary[movieID]['RATINGS']));

# This function converts dictionary to excel file
def covertToExcel():

	csvFile = "movieLists.csv";
	csv = open(csvFile, "w");
	columnTitleRow = "id,name,year,rating,genres,code\n";
	csv.write(columnTitleRow);

	for movieID in movieDictionary:
		mId = (str)( movieDictionary[movieID]['ID'] );
		name = '"' + (str)( movieDictionary[movieID]['NAME'] ) + '"';
		year = (str)( movieDictionary[movieID]['YEAR'] );
		rating = (str)( movieDictionary[movieID]['RATING'] );
		genres = (str)( movieDictionary[movieID]['GENRE'] );
		code = (str)( movieDictionary[movieID]['CODE'] );
		row = mId + "," + name + "," + year + "," + rating + "," + genres + "," + code + "\n";
		csv.write(row);

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
bins = {};
bins[1] = ['ACTION','ADVENTURE','WAR','THRILLER','DOCUMENTARY'];
bins[2] = ['FANTASY','CHILDREN','ANIMATION'];
bins[3] = ['MYSTERY','HORROR','CRIME','IMAX','SCI-FI','FILM-NOIR'];
bins[4] = ['DRAMA','WESTERN','MUSICAL','ROMANCE','COMEDY'];
bins[5] = ['(NO GENRES LISTED)'];

main();