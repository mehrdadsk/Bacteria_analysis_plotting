#!/usr/bin/env python
# coding: utf-8

#Contributions: Equally by Mehrdad Shoae Kazemi - s200090 , Nick Nielsen - s195360 and Nicklas Plum Toft - s135239.

 
# The function _dataLoad(filename)_ takes one input (an string value of the file name) and
# returns a matrix only from the valid data in the file.



#Import of required libraries.
import numpy as np
import sys

#Body of the function.
def dataLoad(filename):
    
    infile = None

    while not infile:
        try:
            infile = open(filename, "r")
            if infile:
                break
        
        except: 
            filename = input("try again or quit by typing 'exit':  ")
            try:
                infile = open(filename, "r")
                if infile:
                    break
            except:
                if filename == 'exit':
                    sys.exit()
                else:
                    continue

    # Defining an empty list for making data matrix. 
    data = []
    # Dictionary which keeps bacteria types with its associated key value.
    bacteria_dictionary = {1: 'Salmonella enterica', 2:'Bacillus cereus',
                           3:'Listeria', 4:'Brochothrix thermosphacta'}
    
    # A counter to identify the lines where there are invalid data.
    line_counter = 0
    
    # The for loop iterates through the file and split the string into 3 parts
    #temperature, growth rate and bacteria with its associated values.    
    for line in infile:
        line_counter += 1
        line = line.split()
        
        # Using try/except to protect the progrm from crashing while assigning values to temperature
        # growth rate and bacteria type variables
        try:
            temperature, growthRate, bacteria = float(line[0]), float(line[1]), int(line[2])
          
        # Here we skip the data that is not a number.
        except ValueError as error:
            print("Error in line {}".format(line_counter))
            print("At least one input is not valid!")
            print("Continuing ... ")
        
        # Conditional statement which takes the data, only when all 3 parts of the line are valid.
        if (10 <= temperature <= 60) and growthRate >= 0 and bacteria in bacteria_dictionary.keys():
            data.append([float(i) for i in line])
        
        # Printing out the errors including the line number and the error type.
        else:
            print("Error in line {}".format(line_counter))
            if temperature < 10:
                print('Temperature is too low')
            if temperature > 60:
                print('Temperature is too high')
            if growthRate < 0:
                print('Growth rate is Zero or Negative: Not valid!')
            if bacteria not in bacteria_dictionary.keys() :
                print('Bacteria type is not valid!')
            print("Continuing ... ")
            print('---------------------------------------')
            
    # Converting the nested lists of data to a matrix.
    data = np.matrix(data)
    
    return data


