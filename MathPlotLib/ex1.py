import urllib.request
import csv
import sys
import matplotlib.pyplot as plt 

DataURL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
'''
['ricoverati_con_sintomi', 'terapia_intensiva', 'totale_ospedalizzati', 
'isolamento_domiciliare', 'totale_attualmente_positivi', 'nuovi_attualmente_positivi', 
'dimessi_guariti', 'deceduti', 'totale_casi', 
'tamponi']
'''

Show = [True,True,True,True,True,True,True,True,True,False]
Colors = ['y:','y--','y-','c:','b-','b--','w--','mo-','r-','b,']

# Download data
response = urllib.request.urlopen(DataURL)
data = response.read().decode("utf-8")

# Turn row data into series
rows = data.split("\n")
labels = rows[0].split(",")[2:]

# X axis value
x = []
# Y Values
series = []
for l in labels:
    series.append([])
# skip first raw ... 
for r in range(1,len(rows)):
    values = rows[r].split(",")
    x.append(values[0][5:10])
    # ...and first two colums
    for v in range (2,len(values)):
        series[v-2].append(int(values[v]))

# Do the plot
with plt.style.context('dark_background'):
    plt.figure(num=None, figsize=(18, 16), dpi=80, facecolor='k', edgecolor='g')  
    # add plots
    for p in range(len(labels)):
        if Show[p]:
            plt.plot(x, series[p], Colors[p], label=labels[p])

    # naming the axis 
    plt.xlabel('Data') 
    plt.ylabel('Casi') 
    # giving a title to my graph 
    plt.title('COVID-19') 
    # show a legend on the plot 
    plt.legend() 
    
# function to show the plot 
plt.show() 

## Part 2 : show percentages of series[8]
for s in range(len(series)):
    if s == 8:
        continue
    #for i in range(len(series[s])):
        #series[s][i] = float(series[s][i]*100.0/series[8][i])
    series[s] = [float(series[s][i]*100.0/series[8][i]) for i in range(len(series[s]))]

for s in range(len(series[8])):
    series[8][s]=100
        
# Do the plot
with plt.style.context('dark_background'):
    plt.figure(num=None, figsize=(18, 16), dpi=80, facecolor='k', edgecolor='g')  
    # add plots
    for p in range(len(labels)):
        if Show[p]:
            plt.plot(x, series[p], Colors[p], label=labels[p])

    # naming the axis 
    plt.xlabel('Data') 
    plt.ylabel('Casi %% rapporto ai casi totali') 
    # giving a title to my graph 
    plt.title('COVID-19') 
    # show a legend on the plot 
    plt.legend() 
    
# function to show the plot 
plt.show() 