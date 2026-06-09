import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/breaches_with_iso3_prefixed.csv")
df = df.drop_duplicates()


#Plot: Annual total leak amount
# Group by year
yearly = df.groupby("year")["records_lost"].sum().reset_index()


plt.figure(figsize=(10, 5))
plt.plot(yearly["year"], yearly["records_lost"], marker="o")
plt.title("Total Records Lost per Year")
plt.xlabel("Year")
plt.ylabel("Records Lost")
plt.grid(True)
plt.tight_layout()
plt.show()

#Annual leak inchident amount
year_count = df.groupby("year").size().reset_index(name="count")

plt.figure(figsize=(10, 5))
plt.plot(year_count["year"], year_count["count"], marker="o")
plt.title("Number of Breaches per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

#Leak by country and region
country = df.groupby("iso3")["records_lost"].sum().reset_index()
country = country.sort_values("records_lost", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(country["iso3"], country["records_lost"])
plt.title("Total Records Lost per Country/Region")
plt.xlabel("Country (ISO3)")
plt.ylabel("Records Lost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Leak by country and region (inchident))
country_count = df.groupby("iso3").size().reset_index(name="incident_count")
country_count = country_count.sort_values("incident_count", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(country_count["iso3"], country_count["incident_count"])
plt.title("Number of Breach Incidents per Country/Region")
plt.xlabel("Country (ISO3)")
plt.ylabel("Incident Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Leak amount by sector
sector_amount = df.groupby("sector")["records_lost"].sum().reset_index()
sector_amount = sector_amount.sort_values("records_lost", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(sector_amount["sector"], sector_amount["records_lost"])
plt.title("Total Records Lost per Sector")
plt.xlabel("Sector")
plt.ylabel("Records Lost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Leak by sector
sector = df["sector"].value_counts()

plt.figure(figsize=(12, 6))
plt.bar(sector.index, sector.values)
plt.title("Number of Breaches per Sector")
plt.xlabel("Sector")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






import pandas as pd
import matplotlib.pyplot as plt

import geopandas as gpd
import matplotlib.pyplot as plt


world = gpd.read_file("data/shapefiles/ne_110m_admin_0_countries.shp")

country_loss = df.groupby("iso3")["records_lost"].sum().reset_index()

world_merged = world.merge(country_loss, left_on="ISO_A3", right_on="iso3", how="left")

usa_row = world_merged[world_merged["ISO_A3"] == "USA"]
others = world_merged[world_merged["ISO_A3"] != "USA"]

plt.figure(figsize=(15, 8))

others.plot(
    column="records_lost",
    cmap="Reds",
    legend=True,
    missing_kwds={"color": "white"},
    edgecolor="black",
    linewidth=0.5,
    ax=plt.gca()
)

usa_row.plot(
    color="black",
    ax=plt.gca()
)

plt.title("Global Data Breach Records Lost (Country and Region, USA Highlighted in Black)")
plt.axis("off")
plt.show()



#Heatmap of Records Lost by Year and Sector
import seaborn as sns

pivot = df.pivot_table(index="year", columns="sector", values="records_lost", aggfunc="sum").fillna(0)
plt.figure(figsize=(12,8))
sns.heatmap(pivot, cmap="Reds", linewidths=0.5)
plt.title("Records Lost by Year and Sector")
plt.show()


#Sectoral Share of Records Lost Over Time
year_sector = df.groupby(["year","sector"])["records_lost"].sum().reset_index()
total_per_year = year_sector.groupby("year")["records_lost"].transform("sum")
year_sector["share"] = year_sector["records_lost"] / total_per_year


for sector in year_sector["sector"].unique():
    plt.plot(year_sector[year_sector["sector"]==sector]["year"],
             year_sector[year_sector["sector"]==sector]["share"],
             label=sector)
plt.legend()
plt.title("Sector Share of Records Lost Over Time")
plt.show()


# Sectoral Share of Incident Count Over Time
year_sector_incidents = df.groupby(["year","sector"]).size().reset_index(name="incident_count")
total_incidents_per_year = year_sector_incidents.groupby("year")["incident_count"].transform("sum")
year_sector_incidents["share"] = year_sector_incidents["incident_count"] / total_incidents_per_year

for sector in year_sector_incidents["sector"].unique():
    plt.plot(year_sector_incidents[year_sector_incidents["sector"]==sector]["year"],
             year_sector_incidents[year_sector_incidents["sector"]==sector]["share"],
             label=sector)
plt.legend()
plt.title("Sector Share of Incident Count Over Time")
plt.show()
