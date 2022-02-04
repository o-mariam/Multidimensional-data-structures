import pandas as pd



data=pd.read_csv('dataset.csv')
data.drop('Poster_Link','Released_Year','Certificate','Runtime','Genre',IMDB_Rating,Overview,Meta_score,Director,Star1,Star2,Star3,Star4,No_of_Votes,Gross)