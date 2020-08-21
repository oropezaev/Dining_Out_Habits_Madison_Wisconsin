import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

business = pd.read_csv("yelp_business.csv")
# business.loc[business['city'] ]
business_madison = business[business['city'].str.contains("madison", case = False) == True]
business_madison = business_madison[business_madison['categories'].str.contains("restaurant", case = False) == True]
print("businesses", len(business))
# print(len(business_madison))
# print(list(business_madison['business_id']))
id = list(business_madison['business_id'])
business_madison.to_csv("business_madison.csv")

reviews = pd.read_csv("yelp_review.csv")
# print(len(reviews))
reviews_madison = reviews[reviews["business_id"].isin(id)]
print(len(reviews_madison))
reviews_madison.to_csv("reviews_madison.csv")

business_at = pd.read_csv("yelp_business_attributes.csv")
business_at_madison = business_at[business_at["business_id"].isin(id)]
# print(len(business_at_madison))
business_at_madison.to_csv("business_attributes_madison.csv")

checkin = pd.read_csv("yelp_checkin.csv")
checkin_madison = checkin[checkin["business_id"].isin(id)]
# print(len(checkin_madison))
checkin_madison.to_csv("checkin_madison.csv")



reviews = pd.read_csv("reviews_madison.csv")
reviews.plot.bar(stacked=True)


# import folium
# import pandas as pd
#
# #create a map
# this_map = folium.Map(prefer_canvas=True)
#
# def plotDot(point):
#     '''input: series that contains a numeric named latitude and a numeric named longitude
#     this function creates a CircleMarker and adds it to your this_map'''
#     folium.CircleMarker(location=[point.latitude, point.longitude],
#                         radius=3,
#                         weight=3).add_to(this_map)
#
# #use df.apply(,axis=1) to "iterate" through every row in your dataframe
# business_madison.apply(plotDot, axis = 1)
#
#
# #Set the zoom to the maximum possible
# this_map.fit_bounds(this_map.get_bounds())
#
# #Save the map to an HTML file
# this_map.save('map.html')
#
