import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Fifa.csv")

df["category"]=df["Position"].map({"GK":"GK", "CB":"DEF", "RB":"DEF", "LB":"DEF", "RWB":"DEF", "LWB":"DEF", "SW":"DEF", "CDM":"MID", "CM":"MID", "CAM":"MID", "LM":"MID", "RM":"MID", "RW":"FWD", "LW":"FWD", "ST":"FWD", "CF":"FWD", "RF":"FWD"})





ages = df["Age"]
Future_Potential = df["Future Potential"]



print(df["category"].isna().sum())
print(df.groupby("Team").size()["Netherlands"])
print(df.groupby("Team")["Overall_Rating"].mean().sort_values(ascending=False).head(10))
print(df.groupby("category")["Overall_Rating"].mean())
print(df.shape)

plt.hist(df["Age"], bins=10, edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Number of players")
plt.title("Age Distribution")
plt.show()

plt.scatter(df["Age"], df["Overall_Rating"], alpha=0.05)
plt.xlabel("Age")
plt.ylabel("Overall Rating")
plt.title("Age vs Overall Rating")
plt.show()

plt.scatter(ages, Future_Potential, alpha=0.05)
plt.xlabel("Age")
plt.ylabel("Future Potential")
plt.title("Age vs Future Potential")
plt.show()

