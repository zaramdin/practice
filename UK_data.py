import requests
import os
import pandas as pd
import requests
from tqdm import tqdm
import concurrent.futures
import numpy as np

def update_data():
#this will download the hmrc file
    def file_update(url,filename):
        response = requests.get(url)
        with open(filename, 'wb') as m:
         m.write(response.content)
        print('CSV file downloaded successfully!')
    file_update("https://data.api.trade.gov.uk/v1/datasets/uk-tariff-2021-01-01/versions/v4.0.19/tables/commodities-report/data?format=csv&download", "C:/Users/zaram/Desktop/python/hmrc_nomenclature.csv")

    commodities = []
    descriptions = []


 
    def merge_and_save_data(hmrc_path, simplified_path):
        # Read commodity data from hmrc.csv
        df = pd.read_csv(hmrc_path)
        df["commodity__code"] = df["commodity__code"].astype(str).apply(lambda x: '0' + x if len(x) < 10 else x)

        # Retrieve commodity information from API
        commodities = []
        descriptions = []

        for code in tqdm(df["commodity__code"]):
            url = f"https://www.trade-tariff.service.gov.uk/api/v2/commodities/{code}"
            response = requests.get(url)

            if response.status_code == 200:
                json_data = response.json()
                if json_data['data']['type'] == "commodity":
                    commodities.append(code)
                    desc = json_data['data']['attributes']['description']
                    descriptions.append(desc)

        # Create DataFrame with unique commodity codes and descriptions
        df_commodities = pd.DataFrame(commodities, columns=["hs-10"])
        df_descriptions = pd.DataFrame(descriptions, columns=["descriptions"])
        df_merge = pd.concat([df_commodities, df_descriptions], axis=1)
        unique_commodities = df_merge.drop_duplicates(subset=["hs-10"], keep='first')
        unique_commodities.to_csv("updated_hmrc_nomenclature.csv", index=False)

        # Read simplified data from Uk_simplified.csv
        simplified = pd.read_csv(simplified_path)

        # Read the previously updated HMRC nomenclature data
        updated_hmrc = pd.read_csv("updated_hmrc_nomenclature.csv")

        # Merge data with simplified information
        df = pd.merge(updated_hmrc, simplified, on='hs-10', how='left')

        # Uncomment the following lines if needed
        # df['descriptions-s'] = df['descriptions-s'].fillna(df['descriptions'])
        # df.drop('descriptions', axis=1, inplace=True)

        # Save the merged DataFrame to hmrc_nomenclat.csv
        df.to_csv("hmrc_nomenclat.csv", index=False)

    # Example usage
    merge_and_save_data("/content/hmrc.csv", "/content/Uk_simplified.csv")
update_data()