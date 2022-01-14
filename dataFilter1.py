
#Contributions: Equally by Nick Nielsen - s195360 and Nicklas Plum Toft - s135239.

#Import of required libraries.
import numpy as np

#Body of the function.
def dataFilter1 (dataset, bacteriaType):
    
    # We convert our data matrix into a data list.
    liste1 = dataset.tolist()
    
    # Here we make an empty list, where we can put extracted bacteriaType data in.
    filterList1 = []
    
    #This is iteration for extracting the bacteriaType data.
    for i in liste1:
        if i[2] == int(bacteriaType):
            filterList1.append(i)
            
    # We change the list into an array to have a userfriendly output.
    filterList1 = np.array(filterList1)
    return filterList1

