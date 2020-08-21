import pandas as pd
import matplotlib.pyplot as plt

business_madison = pd.read_csv("business_madison_with_groups.csv")

# #read in reviews and temp data
# temp = pd.read_csv("temperature_madison_dana_county_2005_03_to_2017_12.csv")
# reviews = pd.read_csv("reviews_madison.csv")
# weather_summary = pd.read_csv("weather_summary.csv")
#
# #merge reviews and temp data
# reviews_temp = reviews.merge(temp, how = 'left', left_on = "date", right_on = "DATE")
# reviews_temp = reviews_temp.merge(weather_summary[['DATE','PRCP', 'SNOW']], how = 'left', left_on = "date", right_on = "DATE", )
#
#
# snow_mean = reviews_temp.groupby('SNOW').mean()
# print(snow_mean.head())
#
# plt.bar(snow_mean.index, snow_mean['stars'])
# plt.xlabel('snow')
# plt.ylabel('stars')
# plt.title('stars vs snow', y=1.1)
# plt.grid()
# plt.show()
#
# snow_count = reviews_temp.groupby('SNOW').count()
# print(snow_count.head())
#
# plt.bar(snow_count.index, snow_count['stars'])
# plt.xlabel('snow')
# plt.ylabel('stars')
# plt.title('stars vs snow', y=1.1)
# plt.grid()
# plt.show()
#
# reviews_temp.pivot_table(values = "stars", index = "SNOW",  margins = True, aggfunc = 'count')
#




# import folium
#
#
# #create a map
# this_map = folium.Map(prefer_canvas=True)
#
# def plotDot(point):
#     '''input: series that contains a numeric named latitude and a numeric named longitude
#     this function creates a CircleMarker and adds it to your this_map'''
#     folium.CircleMarker(location=[point.latitude, point.longitude],
#                         radius=point['stars'],
#                         weight=3, fill = True, color = point['cuisine_grp'], clustered_marker = True).add_to(this_map)
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




from folium import FeatureGroup
import folium


#create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    rest_group = (point["cuisine_grp"])
    if rest_group == "american":
        color = "#E37222"  # tangerine
    elif rest_group == "latin american":
        color = "#FCE205"  # yellow
    elif rest_group == "asian":
        color = "#000080"  # blue
    elif rest_group == "european":
        color = "#552586"  # purple
    else:
        color = "#0A8A9F"  # teal
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=point['stars'],
                        weight=3, fill = True, color = color, clustered_marker = True).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
business_madison.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('map_cuisine.html')


this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    rest_group = (point["comfort"])
    if rest_group == "comfort":
        color = "#E37222"  # tangerine
    else:
        color = "#0A8A9F"  # teal
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=point['stars'],
                        weight=3, fill = True, color = color, clustered_marker = True).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
business_madison.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('map_comfort.html')















this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    rest_group = (point["zip_area"])
    if rest_group == "northeast":
        color = "#E37222"  # tangerine
    elif rest_group == "between lakes":
        color = "#FCE205"  # yellow
    elif rest_group == "southwest":
        color = "#000080"  # blue
    elif rest_group == "other":
        color = "#552586"  # purple
    else:
        color = "#0A8A9F"  # teal
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=point['stars'],
                        weight=3, fill = True, color = color, clustered_marker = True).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
business_madison.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('map_region.html')











import folium


#create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    color = "blue"
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=point['review_count']/50,
                        weight=3, fill = True, color = color, clustered_marker = True).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
business_madison.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('map_reviews.html')













from folium.plugins import HeatMap
this_map = folium.Map(prefer_canvas=True)
HeatMap(data=business_madison[['latitude', 'longitude', 'stars']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(this_map)
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('popular_areas.html')







from folium.plugins import HeatMap
this_map = folium.Map(prefer_canvas=True)
HeatMap(data=business_madison[['latitude', 'longitude', 'stars']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(this_map)
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('popular_areas.html')



from folium.plugins import HeatMap
this_map = folium.Map(prefer_canvas=True)
HeatMap(data=business_madison[['latitude', 'longitude', 'review_count']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(this_map)
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('review_count_heatmap.html')








reviews = pd.read_csv("reviews_madison.csv")

#merge reviews and businesses
merged = business_madison.merge(reviews, how = 'left', on = "business_id")




reviews = pd.read_csv("reviews_madison.csv")
reviews["year"] = reviews["date"].str[:4]
business_madison = pd.read_csv("business_madison_with_groups.csv")
#merge reviews and businesses
merged = business_madison.merge(reviews, how = 'left', on = "business_id")
merged.head()






merged_by_year = merged.groupby(['business_id', 'year']).mean()
stars = merged_by_year["stars_y"].unstack()
avg_stars = stars[['2016', '2017']]
avg_stars["diff"] = stars['2017'] - stars['2016']
avg_stars = avg_stars.merge(business_madison[['latitude', 'longitude', 'business_id']], on = "business_id")
avg_stars


import folium

#create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    color = "blue"
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=point['diff'],
                        weight=3, fill = True, color = color, clustered_marker = True).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
avg_stars.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())


#Save the map to an HTML file
this_map.save('diff_years.html')