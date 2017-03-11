from geoip import geoip

geoip = geoip.geoip_helper()
print geoip.query("105.103.45.175")
