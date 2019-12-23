import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#a)Load dataset
df=pd.read_csv("train.csv")

#b)data header and description
print(df.head(5))

print("Description")
print(df.info())
print(df.describe())


#c)Drop Unnecessary
df=df.drop(["Name","PassengerId","Cabin"],axis=1)
print(df.head())

#d)Manipulate
df["Age"]=df["Age"].fillna(18)
print(df.Age)

df["Embarked"]=df["Embarked"].map({
	"S":"Southampton",
	"Q":"Queensland",
	"C":"County"
	})
print(df.Embarked)

df["Survived"]=df["Survived"].map({
	0:"dead",
	1:"alive"
	})
print(df.Survived)

#e)Visulisation
print("Data Visulisation")
ax=sns.countplot(data=df,x="Survived",hue="Pclass",palette="Set2")
ax.set(title="Survived based on pclass",xlabel="Survived",ylabel="Count")
plt.show()