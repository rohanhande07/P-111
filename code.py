import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)
print("The mean is ", mean)
print("The standard deviation is ", std)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

s_mean = statistics.mean(mean_list)
s_std = statistics.stdev(mean_list)
print("The sample mean is ", s_mean)
print("The sample standard dev is ", s_std)

def show_fig(mean_list):
    df = mean_listfig = ff.create_distplot([df],["reading time"], show_hist=False)
    fig.show()

first_std_start, first_std_end = s_mean-s_std, s_mean+s_std
second_std_start, second_std_end = s_mean-(s_std*2), s_mean+(s_std*2)
third_std_start, third_std_end = s_mean-(s_std*3), s_mean+(s_std*3)

z_score = (mean-s_mean)/s_std
print("The z score of sample 3 is ", z_score)

fig = ff.create_distplot([mean_list],["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.8], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.7],mode="lines",name="First std start"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.7],mode="lines",name="First std end"))
fig.add_trace(go.Scatter(x=[second_std_start,second_std_start],y=[0,0.7],mode="lines",name="Second std start"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.7],mode="lines",name="Second std end"))
fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.7],mode="lines",name="Third std start"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.7],mode="lines",name="Third std end"))
fig.show()



