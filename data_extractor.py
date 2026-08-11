import pandas as pd


def data_extractor_func():

    data = []

    file = pd.read_csv("account.csv")

    for index, row in file.iterrows():

        name = row["Name"]
        profileLink = row["LinkedIn_Account"]

        data.append([name, profileLink])

    return data