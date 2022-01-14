#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ## Main Script ##
# ------------------------------------------------------------------ #
#Contributions:
"""
1- Main script  by:
Mehrdad Shoae Kazemi - s200090
Nick Nielsen - s195360 
Nicklas Plum Toft - s135239

2- Data loading by:
Mehrdad Shoae Kazemi - s200090
Nick Nielsen - s195360 
Nicklas Plum Toft - s135239

3- Data filtering 1&2
Nick Nielsen - s195360 
Nicklas Plum Toft - s135239

4- Data statistics by:
Mehrdad Shoae Kazemi - s200090

5- Data plotting by:
Mehrdad Shoae Kazemi - s200090
"""      
# ------------------------------------------------------------------ #
#Import of relevant fuctions as scripts.
#Import of relevant libraries happen here.

import sys
import copy
from dataLoad import *
from dataStatistics import *
from displayStatistics import *
from dataFilter1 import *
from dataFilter2 import *

# ------------------------------------------------------------------ #
#Body of the Main Script.
#Input_string1&2 is for helping the user understand the program.
#counter is iteration having different input_string depending on where we are in the program.
counter = 0

#Loop or iteration for taking user input continuously, until the user decides to quit the program.
while True:
    
    #List of options the user have, to navigate the program.
    print("------------------------------------------------------------------------------------")
    print("List of actions:", "Load the data = 1 ", "Filter data = 2 ", "Display statistics = 3" ,
          "Generate plots = 4" ,"Reset data = 5" ,"Quit = 6")
    print("------------------------------------------------------------------------------------")

    counter += 1
    
    # Initially loading data when you boot the program, the first time.
    if counter == 1:
    
        user_input = input("Please, choose a number from the list of actions to continue. Yes, right, you don't have any option than choosing 1 in the begining :D, but I promiss you, it gets better later ;) Your chosen code is: ")
        if int(user_input) == 1:
            print("Yes, again you don't have any option other than typing 'test.txt' :D ")
            filename = input("Please enter the file name: ")
            dataset = dataLoad(filename)
            dataset_for_filter = copy.deepcopy(dataset)
            print("Data has been loaded, now you have countless options in front of you. Enjoy!")
    
    # Running the program after the counter is > 1.
    # If the user wants to load the data again, or choose new datafile. 
    else:
        user_input = input("Please, choose a number from the list of actions to continue: ")
        
        #This part is used for loading data from a file.
        if int(user_input) == 1:
            print("Yes, again you don't have any option other than typing 'test.txt' :D")
            filename = input("Please enter the file name: ")
            dataset = dataLoad(filename)
            dataset_for_filter = copy.deepcopy(dataset)
            print("Data has been loaded, now you have countless options in front of you. Enjoy!")
            
        
        #This part is used for filtering based on bacteria type and growth rate.
        elif int(user_input) == 2:
            print("------------------------------------------------------------------------------------")
            print("Please choose a filter type, otherwise we ")
            print("Option 1 - Filter by Bacteria type:  1")
            print("Option 2 - Filter by the Growth rate input number 2")
            filterType = input("Please enter your filter type here: ")
            print("------------------------------------------------------------------------------------")
            
            #This part is for selecting desired bacteria type.
            if int(filterType) == 1:
                print("For 'Salmonella enterica' input 1")
                print("For 'Bacillus cereus' input 2")
                print("For 'Listeria' input 3")
                print("For 'Brochothrix thermosphacta' input 4")
                bacteriaType = input("Your bacteria code is: ")
                dataset_for_filter = dataFilter1(dataset_for_filter, bacteriaType)
                # If the dataset is empty because of filtering, the user is prompted to reset the data.
                if dataset_for_filter.size != 0:
                    print(dataset_for_filter)
                else:
                    print("The dataset is empty after filtering! Please reset the data")
                    continue

            #This part is for selecting desired bacteria growth range.
            elif int(filterType) == 2:
                lower_growthRate = float(input("Please input a number as the lower growth rate limit. "))
                upper_growthRate = float(input("Please input a number as the upper growth rate limit. "))
                dataset_for_filter = dataFilter2(dataset_for_filter, lower_growthRate, upper_growthRate)
                # If the dataset is empty because of filtering, the user is prompted to reset the data.
                if dataset_for_filter.size != 0:
                    print(dataset_for_filter)
                else:
                    print("The dataset is empty after filtering! Please reset the data")
                    continue
                
        #This part is for giving the user the desired statistic
        elif int(user_input) == 3:
            print("------------------------------------------------------------------------------------")
            print("Statistics Menu:", "\n",
                  "Mean Temperature = 1","\n",
                  "Mean Growth rate = 2","\n", 
                  "Std Temperature = 3","\n",
                  "Std Growth rate = 4", "\n",
                  "Rows = 5","\n",
                  "Mean Cold Growth rate = 6","\n", 
                  "Mean Hot Growth rate = 7")
            print("------------------------------------------------------------------------------------")
            user_input = int(input("Please, enter an statistic code from the Statistics Menu: "))
            print(dataStatistics(dataset_for_filter, user_input))
        
        #This part is for plotting the whole or filtered data
        elif int(user_input) == 4:
            print(dataPlot(dataset_for_filter))
        
        #This part is for resetting the chosen data filters.
        #Here we use our intact data set for recovering the original data.
        elif int(user_input) == 5:
            dataset_for_filter = dataset
            print("\n")
            print("------------------------------------------------------------------------------------")
            print("The filters on your data has been removed.")
            print("------------------------------------------------------------------------------------")
        
        #This part is for quitting the program.
        elif int(user_input) == 6:
            break
            sys.exit()

# ------------------------------------------------------------------ #












