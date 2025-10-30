#Be able to display the world map
import pandas
from track_iss import IssPosition
from image import Map

#Create a csv file for the world map with the coordinates
file = pandas.read_csv('world_coordinates.csv')
data_dict = file.to_dict(orient='records')
iss_position = IssPosition()
world_img = Map(iss_position)


#Get the iss to move on the canvas as it's on the low geographical zone
#Be able to display an image and zoom in to the particular spot of the iss in the world map
#Find me in the map and email me telling me the distance from me to the iss