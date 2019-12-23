import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#a)Load dataset 
df=pd.read_csv("StudentsPerformance.csv")

#b)Data headers and description
print("Data Headers")
print(df.head(5))

print("Data Information")
print(df.info())
print(df.describe())


#c)Remove Unnecessary
data1 = df.drop(["lunch", "test preparation course"], axis=1)
print("Removal of Unnecessary columns")
print(data1.head())


#d)Manipulation

df["race/ethnicity"]=df["race/ethnicity"].map({
	"group A":"American",
	"group B":"Asian",
	"group C":"Afro-American",
	"group D":"African",
	"group E":"European"
	})
print(df["race/ethnicity"][:10])

print("********************************************************************************************")
df["parental level of education"]=df["parental level of education"].fillna("high school")
print(df["parental level of education"])


#e)
print("Data Visualisation")
ax=sns.countplot(data=df,x="test preparation course",hue="gender",palette="Set1")
ax.set(title="Test preparation",xlabel="Course",ylabel="Total")
plt.show()
