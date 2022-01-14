
#Contributions: By Mehrdad Shoae Kazemi - s200090.

#Import of required libraries.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dictionary which keeps bacteria types with its associated key value.
bacteria_dictionary = {1: 'Salmonella enterica', 2:'Bacillus cereus',
                      3:'Listeria', 4:'Brochothrix thermosphacta'}
# Body of the function.
def dataPlot(data):
    
    # We create 3 different lists for for bacteria: count, names and codes.
    # Bacteria code is the key of the bacteria in the bacteria dictionary.
    bacteria_count = []
    bacteria_names = []
    bacteria_codes = []
    
    #Iterate through data set to extract: count, names and codes of each bacteria.
    for n in range(4):
        counter = 0
        for i in data.tolist():
            if i[2] == n + 1:
                counter += 1
        
        # Here we exclude the bacteria filtered by the user, from plotting.
        if counter != 0:
            bacteria_count.append(counter)
            bacteria_names.append(bacteria_dictionary[n+1])
            bacteria_codes.append(n+1)



    # Here we make Plot 1: Number of bacteria in the selected dataset.
    sns.set(rc={'figure.figsize':(8,4)}, font_scale = 1)
    sns.set_style('white')
    fig = sns.barplot(x = bacteria_names, y = bacteria_count, palette="ch:start=.2,rot=-.3", )
    fig.axes.set_title("Number of bacteria in the selected dataset",fontsize = 14)
    fig.set_xlabel("Bacteria type",fontsize = 12);
    fig.set_ylabel("The number of bacteria",fontsize = 12);
    plt.show()

  
    # Here we make 2 empty lists for keeping each bacterias temperature and growth rate data.
    temp_total = []
    growthR_total = []
    
    # Here we exclude the bacteria filtered by the user, from plotting.
    for n in range(len(bacteria_names)):
        temperatures = []
        growth_rates = []
        
        # We extract temperature and growth rates for each bacteria, in the data, into their own list. A list of lists.
        for i in data.tolist():
            if i[2] == bacteria_codes[n]:
                temperatures.append(i[0])
                growth_rates.append(i[1])
        temp_total.append(temperatures) 
        growthR_total.append(growth_rates)

    # Here we make plot 2: Growth rate of each selected bacteria.
    for n in range(len(bacteria_names)):
        title = "Growth rate of each selected bacteria in different temperature"
        sns.set(rc={'figure.figsize':(8,4)}, font_scale = 1)
        sns.set_style('white')
        fig = sns.lineplot(x = temp_total[n], y = growthR_total[n], label = bacteria_names[n])
        fig.axes.set_title(title, fontsize = 14)

        fig.set_xlabel("Temperatures",fontsize = 12);
        fig.set_ylabel("Growth rates",fontsize = 12);
        plt.xticks(rotation = 50, fontsize = 12)
        plt.yticks(fontsize = 12)
        fig.legend()
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.show()