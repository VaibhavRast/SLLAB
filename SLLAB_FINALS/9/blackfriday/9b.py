import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#a)Load dataset
df=pd.read_csv("blackfri.csv",skipinitialspace=True)

#b)Data header and describe
print(df.head(5))
print("Desc:")
print(df.info())
print(df.describe())

#c)Clean data
df["City_Category"]=df["City_Category"].fillna("A")
print(df["City_Category"])

#d)Map
df["City_Category"]=df["City_Category"].map({
	"A":"Metro City",
	"B":"Small Town",
	"C":"Village"
	})
print(df["City_Category"])

#e)Visulaisation
print("--------------Visulaisation---------")
ax=sns.countplot(data=df,x="Gender",hue="City_Category",palette="Set2")
ax.set(title="Male and females in particular city category",xlabel="Gender",ylabel="Total")
plt.show()
