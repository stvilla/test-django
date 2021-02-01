import pandas as pd
import sklearn.datasets as ds
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn

d = ds.load_iris(as_frame=True)
data = pd.concat([d.data,d.target],axis=1)
data.columns = [i.replace(" (cm)","").replace(" ","_") for i in data.columns]

for t in data.target.unique():
    cur_data = data.loc[data.target == t]
    plt.plot(cur_data['sepal_length'], cur_data['sepal_width'],'.',label = t)
plt.legend()
#plt.show()
plt.close()

lr = LinearRegression()
lr.fit(data.iloc[:,0:4],data.iloc[:,4])
y = lr.predict(data.iloc[:,0:4])

seaborn.countplot(data = data, x ='sepal_length')
#plt.show()
plt.close()

seaborn.barplot(data = data, x = 'target', y = 'sepal_length')
#plt.show()
plt.close()

seaborn.scatterplot(data = data, x = 'sepal_length', y = 'sepal_width',hue = 'target')
plt.show()
