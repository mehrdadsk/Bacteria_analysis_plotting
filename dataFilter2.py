#Contributions: Equally by Nick Nielsen - s195360 and Nicklas Plum Toft - s135239.

#Import of required libraries.
import numpy as np

#Body of the function.
def dataFilter2 (dataset, lower_growthRate , upper_growthRate):
        # Here we make an empty list, where we can put extracted range of growth rates.
        filterList2 = []
        
        #This is iteration for extracting the specific range of growth rates.
        for i in dataset.tolist():
            # Here we specify the range of extraction.
            if lower_growthRate < i[1] < upper_growthRate:
                filterList2.append(i)
        
        # We change the list into an array to have a userfriendly output.
        filterList2 = np.array(filterList2)
        return filterList2
