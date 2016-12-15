#!/usr/local/bin/python
# Author: Sjors van Heuveln; 01-08-2016
# About: Creates a practice sheet for multiplication tables and important fractions.

import random
import sys

#functions
def table():
	a = str(random.randint(2,9))
	b = str(random.randint(2,9))
	table = a + " x " + b + "=\t\t"
	return table

def random_fraction():
	fractions = ["0.5","0,333.","0.666.","0.25","0.75","0.2","0.4","0.6","0.8","0.166.","0.833.","0.125","0.375","0.625","0.875","0,1","0,3","0,7","0,9","0,05","0,01"]
	fraction = str(fractions[random.randint(2,len(fractions)-1)]) + "=\t\t"
	return fraction

def line(width):
	#creates a line of questions

	line = ""
	random_position = random.randint(0,3)
	for i in range(0,width):
		if i==random_position:
			line += random_fraction()
		else:
			line += table()
	line += "\n"
	return line

def sheet(height,col_height,width):
	#creates a sheet of questions

	sheet = "Tafel en Breuken Memorisatie - (C) WisCAT Bijles 2016\nStreeftijd = 3m:30\n\n"
	for i in range(0,height):
		for j in range(0,col_height):
			sheet += line(width)
		sheet += '\n'

	return sheet

def print_sheet(copies,height,col_height,width):
	#prints n copies of random sheets 
	for i in range(1,copies+1):
		file_name = "/Users/svanheuveln/Desktop/tafel_oefening" + str(i) + ".txt"
		print(file_name)
		page = sheet(height,col_height,width)
		text_file = open(file_name, "w")
		text_file.write(page)
		text_file.close()

#### MAIN ####

#parameters to be set
width = 4
height = 8
col_height = 5

#allows copies argument in commandline 
if len(sys.argv) < 2:
	copies = 1
else: 
	copies = int(sys.argv[1]) #number of sheets to make

print_sheet(copies,height,col_height,width)
