import os, fiona

# make output folder if required
if not os.path.exists('merge-output'):
    os.makedirs('merge-output')

# open an output file
with fiona.open('merge-output/merged.shp', 'w', 
	driver='ESRI Shapefile', 
	crs='+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +towgs84=446.448,-125.157,542.06,0.15,0.247,0.842,-20.489 +units=m +no_defs ', 
	schema={'geometry': 'MultiPolygon', 'properties': {'source': 'str'}} ) as o:

	# loop through all files in the current directory
	for subdir, dirs, files in os.walk('./'):
		for file in files:
		
			# only use the shapefiles
			if os.path.splitext(file)[-1].lower() == '.shp':

				# assemble the paht to the shapefile
				path = os.path.join(subdir, file)

				# print the path
				print (path)
				
				# load the shapefile
				with fiona.open(path) as input:

					# loop through each feature in this case
					for feature in input:
							
						# write the feature geometry and file path to the new shapefile
						o.write({'geometry': feature['geometry'],'properties': {'source': path}})

print("done!")