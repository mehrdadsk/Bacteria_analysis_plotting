
#Contributions: Equally by Mehrdad Shoae Kazemi - s200090.


#Import of required libraries.
import numpy as np

#Body of the function.
def dataStatistics(data, user_input):
    
    # It extracts the averages of temperature (column 1) and growth rate (column 2).
    averages = np.mean(np.array(data[:,0:2]), axis = 0)
    
    # It extracts the standard deviation of temperature (column 1) and growth rate (column 2).
    standard_devs = np.std(np.array(data[:,0:2]), axis = 0)
    
    # This part is used for calculating mean temperature.
    if int(user_input) == 1:
        result = "Mean temperature is {}".format(averages[0]) 

    # This part is used for calculating mean growth rate.    
    elif int(user_input) == 2:
        result = "Mean growth rate is {}".format(averages[1]) 

    # This part is used for calculating std of temperature.        
    elif int(user_input) == 3:
        result = "Standard deviation of the temperature is {}".format(standard_devs[0])
        
    # This part is used for calculating std of growth rate.
    elif int(user_input) == 4:
        result = "Standard deviation of the growth rate is {}".format(standard_devs[1]) 
        
    # This part is for counting number of rows currently in the data.
    elif int(user_input) == 5:
        result = "There are {} rows in the dataset".format(data.shape[0])
        
    # This part is used for calculating the growth rate where temperature < 20.
    elif int(user_input) == 6:
        cold_growth_rates = np.array(data[:,1][np.where(data[:,0] < 20)])
        result = "Mean Cold Growth rate is {}".format(np.mean(cold_growth_rates))
        
    # This part is used for calculating the growth rate where temperature > 50.
    elif int(user_input) == 7:
        hot_growth_rates = np.array(data[:,1][np.where(data[:,0] > 50)])
        result = "Mean Hot Growth rate is {}".format(np.mean(hot_growth_rates))

    return result
