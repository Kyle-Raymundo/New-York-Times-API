'''
Purpose: to grab certain articles and organize it into metadata in the form of csv files.
The data is from the New York Times related to the query and inputed time interval.
However requests  perhaps may not exist.
'''

import requests
import json
import pandas as pd

api_key = "7gLb6BmtwBZjFqVUxEmfMVT7PlLsIRQM" #api key is to my app which as the archive key
url = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}"

# range of years and months
years = range(2022, 2023)  
months = range(1, 13) #if the API does not work all the way through, change the range to the next integer.

# Query feel free to change to whatever query you would like.
query = "Artificial Intelligence"

for year in years:
    for month in months:
        params = {"api-key": api_key, "q": query, "year": year, "month": month}
        current_url = url.format(api_key=api_key, year=params["year"], month=params["month"])
        r = requests.get(current_url, params=params)
        data = r.json()["response"]["docs"]

        df = pd.DataFrame(data)
        df = df[["headline", "pub_date", "keywords"]]  # relevant columns
        df["pub_date"] = pd.to_datetime(df["pub_date"])  #datetime
        df["year"] = df["pub_date"].dt.year  # year

        # Filter
        df_filtered = df[df["headline"].str.contains(query, case=False, na=False) |
                         df["keywords"].apply(lambda x: any(keyword.get("value", "").lower() == query.lower() for keyword in x))]

        # Saving data to file
        df_filtered.to_csv(f"output_data_{year}_{month}.csv", index=False)
