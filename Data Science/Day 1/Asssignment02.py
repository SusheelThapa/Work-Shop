import pandas as pd


# Loading the csv file
data = pd.read_csv("Data.csv")

# To check the missing value
print(data.info())

# Filling the empty places
data = data.fillna(data.median)

# To check whether the empty space is filled or not
print(data.info())

# Searching the data in life expectancy greater than 80 and removing row with less than 80
for index in range(0, data["Life expectancy "].shape[0]):

    # A try except statement so that if any error occured will be handled
    try:
        if data["Life expectancy "][index] > 80:
            pass
        else:
            data = data.drop(index)

    except:
        pass

#Taking first 5 columns of data
count = 0
for items in data:
    count = count +1
    if count-1>=5:
        data.pop(items)

#Storing the data to csv files 
data.to_csv("Assignment02.csv",index = None)
