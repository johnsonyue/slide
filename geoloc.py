import sys

def main(argv):
	if (len(argv)<2):
		print "gunzip -cd db.gz | tail -n +2 | python geoloc.py caida"
		exit()

	db={}
	while True:
		try:
			line=raw_input()
			fields=line.split(',')
			country=fields[0].lower()
			city=fields[1].lower()
			lat=fields[5]
			lon=fields[6]
			if (not db.has_key(country)):
				db[country]={ city:{"lat":lat,"lon":lon} }
			else:
				db[country][city]={"lat":lat,"lon":lon}
			#print country,city,lat,lon
		except:
			break
	
	fp=open(argv[1])
	for line in fp.readlines():
		toponym=line.split('|')[1].split(',')
		city=toponym[0].lower()
		country=toponym[-1].lower().replace(' ','')
		lat=""
		lon=""
		
		if (db.has_key(country) and db[country].has_key(city)):
			lat = db[country][city]["lat"]
			lon = db[country][city]["lon"]
		elif (db.has_key(country)):
			lat = next(db[country].itervalues())["lat"]
			lon = next(db[country].itervalues())["lon"]
		
		print "%s|%s|%s" % (line.strip('\n').strip(' '), lat, lon)

if __name__ == "__main__":
	main(sys.argv)
