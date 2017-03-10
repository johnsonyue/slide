from geoip import geoip

geoip = geoip.geoip_helper()
print geoip.query("202.118.236.229")
