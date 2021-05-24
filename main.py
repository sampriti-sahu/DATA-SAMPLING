import pandas as  pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random
dataset = []
df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
def randomsetofdata(counter):
    for i in range(0,counter):
        random_index = random.randint(0,(len(data) - 1))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ['Result'], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,25], mode = 'lines', name = 'Mean'))
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofdata(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print('mean of sampling distribution' ,mean)
    sd = statistics.stdev(data)
    print(sd)

setup()

