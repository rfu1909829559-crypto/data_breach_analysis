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