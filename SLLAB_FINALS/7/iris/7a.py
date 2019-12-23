import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#a)Load dataset
df=pd.read_csv("iris.csv",skipinitialspace=True)

#b)Data header and describe
print(df.head(5))
print("Desc:")
print(df.info())
print(df.describe())

#c)Clean data
df=df.drop(["Petal_Length"],axis=1)
print(df.head(5))

#d)Avg petal width of each category
print("----------------Avg----------------------------")
print(df[["variety","Sepal_Width"]].groupby(["variety"],as_index=True).mean())

#e)Visulaisation
print("--------------Visulaisation---------")
ax=sns.countplot(data=df,x="Sepal_Width",hue="variety",palette="Set2")
ax.set(title="Sepal width based on variety",xlabel="Sepal width",ylabel="Total")
plt.show()