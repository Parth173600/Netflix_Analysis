import pandas as pd 
import matplotlib.pyplot as plt

# Load the data using pandas 

df=pd.read_csv("netflix_titles.csv")

# cleaning the data like dropna function is used for remove nan value 

df=df.dropna(subset=["show_id","type","title","director","cast","country","date_added","release_year","rating","duration","listed_in"])

# Movies_vs_Tvshows bar graph

type_counts = df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index , type_counts.values , color = ["skyblue" , "orange"])
plt.title("Number of movies vs tv shows on netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Movies_vs_Tvshows.png")
plt.show() 

# Percentage of content rating

rating_counts = df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts , labels  = rating_counts.index , autopct="%1.1f%%",startangle=90 )
plt.title("Percentage of content rating")
plt.tight_layout()
plt.savefig("Content_rating.png")
plt.show()

# Distrubition of movies duration

movie_df = df[df["type"] == "Movie"].copy()
movie_df["duration_int"] = movie_df["duration"].str.replace(" min","").astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df["duration_int"] , bins=30 , color = "purple" , edgecolor = "black")
plt.title("Distrubition of movies duration")
plt.xlabel("Duration (in minutes)")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig("Movies_duration_histogram.png")
plt.show() 

# Release year vs number of shows

release_count = df["release_year"].value_counts().sort_index()
plt.figure(figsize = (10,6))
plt.scatter(release_count.index , release_count.values , color = "red")
plt.title("Release year vs number of shows")
plt.xlabel("Release year")
plt.ylabel("Number of shows")
plt.tight_layout()
plt.savefig("Releaseyear_vs_numberofshows_scatter.png")
plt.show() 

# Top 10 coountries by number of shows

country_count = df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index , country_count.values , color = "green" )
plt.title("Top 10 coountries by number of shows")
plt.xlabel("Number of shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("Top_10_countries.png")
plt.show() 

content_by_year = df.groupby(["release_year" , "type"]).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2, figsize=(12,5))

#fisrs subplot movies 

ax[0].plot(content_by_year.index , content_by_year["Movie"] , color = "blue")
ax[0].set_title("Top 10 coountries by number of shows")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of movies")

#second subplot tvshows

ax[0].plot(content_by_year.index , content_by_year["TV Show"], color = "orange")
ax[0].set_title("Tv shows release per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of tv shows")

fig.suptitle("comparision of movies and tv shows released over years")

plt.tight_layout()
plt.savefig("movies_tvshows_comparison.png")
plt.show()