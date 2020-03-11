import urllib.request
import matplotlib.pyplot as plt 

DataURL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'

# Download data
response = urllib.request.urlopen(DataURL)
data = response.read().decode("utf-8")

# Turn row data into series
rows = data.split("\n")
labels = rows[0].split(",")[2:]

# X axis value
x = []
# Y Values
series = [ [] for l in labels ]

# skip first raw (labels) ... and first two colums (x and constant 'ITA')
for r in range(1,len(rows)):
    values = rows[r].split(",")
    x.append(values[0][5:10])
    for v in range (2,len(values)):
        series[v-2].append(int(values[v]))

# Do the plot
with plt.style.context('dark_background'):
    plt.figure(num=None, figsize=(18, 16), dpi=80, facecolor='k', edgecolor='g')  
    # add plots
    for p in range(len(labels)-1):
        plt.plot(x, series[p], label=labels[p])
    plt.xlabel('Data') 
    plt.ylabel('Casi') 
    plt.title('COVID-19') 
    plt.legend() 
    
# show the plot 
plt.show() 