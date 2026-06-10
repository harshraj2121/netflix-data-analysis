import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv('./dataset/netflix_titles.csv')

#missing values handling
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
#ab dekho duration me minutes and sesons dono hai to agar sare missing values pe same kaam karenge to data galat ho jayega to hum
#to hum kya karenge ki agar type "movie" hai to duration me median fill karenge (kyuki median outliers pe kam effect karta hai) aur agar type "tv show" hai to duration me mode fill karenge
#movies = df[df['type'] == 'Movie']
#shows = df[df['type'] == 'TV Show']

#median ko sidha aaise use kar sakte hai and fillna kar sakte hai
# median_duration = (
#     df['duration']
#     .str.extract(r'(\d+)')[0]
#     .astype(float)
#     .median()
# )

#waise in sab chhote dataset me pandas aur numpy same hi kaam karenge but agar bada dataset hota to numpy jyada efficient hota hai
#numpy array me convet karna
numpy_duration_arr = (
    df['duration']
    .str.extract(r'(\d+)')[0]
    .dropna()
    .astype(int)
    .to_numpy()
)
median_duration = np.median(numpy_duration_arr)
df['duration'] = df['duration'].fillna(median_duration)



# chart 1 (Movies vs Tv shows)
# categories = df['type'].value_counts().index
# values = df['type'].value_counts().values

# plt.bar(categories, values)
# plt.title('Distribution of Movies and TV Shows on Netflix')
# plt.xlabel('Type')
# plt.ylabel('Count')

# chart 2 (Top 10 countries with most movies and tv shows)
# countries = (
#     df['country']
#     .str.split(',')
#     .explode()
#     .str.strip()
#     .value_counts()
#     .head(10)
# )
# plt.figure(figsize=(10, 6))
# plt.barh(countries.index, countries.values)
# plt.gca().invert_yaxis()  # Reverse the y-axis to have the highest count at the top
# plt.title('Top 10 Countries with Most Movies and TV Shows on Netflix')
# plt.xlabel('Count')
# plt.ylabel('Countries')
# plt.tight_layout()


#chart 3 (content Release trend on Netflix release_year)
# plt.figure(figsize=(12,6))
# plt.plot(
#     df['release_year'].value_counts().sort_index().index,
#     df['release_year'].value_counts().sort_index().values
# )

# plt.xlabel("Release Year")
# plt.ylabel("Number of Titles")
# plt.title("Netflix Content Released by Year")



# chart 4 (Distribution of TV Shows and Movies by Genre on Netflix top genres)
# listed_in = df['listed_in'].str.split(',').explode().str.strip().value_counts()
# tv_shows = listed_in[listed_in.index.str.contains('TV')]
# not_tv_shows = listed_in[~listed_in.index.str.contains('TV')]

# plt.figure(figsize=(15, 10))
# plt.barh(tv_shows.index, tv_shows.values, label='TV Shows', color='blue')
# plt.barh(not_tv_shows.index, not_tv_shows.values, label='Movies', color='orange')
# plt.gca().invert_yaxis()
# plt.xlabel('Count')
# plt.title('Distribution of TV Shows and Movies by Genre on Netflix')
# plt.legend()
# plt.tight_layout()



# chart 5 (Distribution of content rating on Netflix)
# ratings = df['rating'].value_counts().head(10)
# plt.barh(ratings.index, ratings.values)
# plt.gca().invert_yaxis()
# plt.xlabel('count')
# plt.ylabel('Rating')
# plt.title('Distribution of Content rating on Netflix')
# plt.tight_layout()



#chart 6 (Diatrubition of duration on Netflix)
# movies_duration = df[df['type'] == 'Movie']['duration'].dropna().str.extract(r'(\d+)')[0].dropna().astype(int).sort_values()
# bins = np.arange(
#     0,
#     movies_duration.max() + 20,
#     20
# )
# plt.figure(figsize=(10, 4))
# counts, bins, patches = plt.hist(
#     movies_duration,
#     bins=bins,
#     edgecolor='black'
# )
# plt.yscale('log')
# plt.ylim(1,max(counts) * 6)
# plt.xticks(bins)
# plt.yscale('log')
# plt.title("Movie Duration Distribution")
# plt.xlabel("Duration (Minutes)")
# plt.ylabel("Frequency")




#chart 7 (Top Directors on Netflix)
# directors = df['director'].str.split(',').explode().str.strip().value_counts().head(11)
# top_directors = directors[directors.index != 'Unknown']
# plt.figure(figsize=(10, 6))
# plt.barh(top_directors.index, top_directors.values)
# plt.gca().invert_yaxis()
# plt.xlabel('No. of Movies')
# plt.ylabel('Director')
# plt.title('Top Directors on Netflix')





# chart 8 (Top Actors on Netflex)
# actors = df['cast'].str.split(',').explode().str.strip().value_counts().head(11)
# top_actors = actors[actors.index != 'Unknown']
# plt.figure(figsize=(10, 6))
# plt.subplots_adjust(
#     left=0.20,
#     right=0.97,
#     top=0.90,
#     bottom=0.12
# )
# plt.barh(top_actors.index, top_actors.values)
# plt.tight_layout()
# plt.gca().invert_yaxis()
# plt.xlabel('No. of Movies')
# plt.ylabel('Actor')
# plt.title('Top Actors on Netflix')




#part 2
# chart 1 (Movies vs TV Shows Over Time in past 10 years)
# yearly_content = df.groupby(['release_year', 'type']).size().unstack(fill_value=0).tail(10)
# yearly_content.plot(
#     kind='bar',
#     stacked=True,
#     figsize=(14,6)
# )


# chart 2 ( top geners by type )
listed_in = df['listed_in'].str.split(',').explode().str.strip().value_counts()
tv_shows = listed_in[listed_in.index.str.contains('TV')]
not_tv_shows = listed_in[~listed_in.index.str.contains('TV')]
# top_genres = df.groupby(['type', 'listed_in']).size().unstack(fill_value=0)
# print(top_genres)









plt.show()