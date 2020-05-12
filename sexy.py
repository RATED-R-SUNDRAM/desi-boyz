# location change kar lena aur isko hatana mat comment kar dena
import matplotlib.pyplot as plt
import pandas as pd
import statistics
a=pd.read_csv(r"C:\Users\Shivam Sundram\OneDrive\Desktop\FALTU K FOLDERS\shubham\time-series-19-covid-combined_csv.csv")
b=a.groupby("Date").Confirmed.sum()
d={}
for i in range(len(b)-1):
    if (b[i+1]-b[i]) in d:
        d[b[i+1]-b[i]]+=1
    else:
        d[b[i+1]-b[i]]=1
d.update((x,y/sum(d.values())) for x,y in d.items())
x=[k for k in d.keys()]
y=[k for k in d.values()]
expec=0
for i in range(len(x)):
    expec+=(x[i]*y[i])
print("the expected value is",expec)
print("the variance is", statistics.variance(x))
plt.scatter(x,y)
plt.show()