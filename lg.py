import sys
import re

from geoip import geoip

def usage():
	print "cat ip-server | python lg.py"

def main(argv):
	geoip_helper = geoip.geoip_helper()
	ip_list=[]
	while True:
		try:
			line = raw_input().strip('\n')
			if (re.findall("---",line) and len(ip_list)!=0):
				for i in range(len(ip_list)):
					ip=ip_list[i]
					geo = geoip_helper.query(ip)
					country = geo["mmdb"]["country"]
					if (country != "*"):
						break
				if (country == "*"):
					country = geo["bgp"]["country"]
				asn = geo["bgp"]["asn"]
				city = geo["mmdb"]["city"]
				lon = geo["mmdb"]["longitude"]
				lat = geo["mmdb"]["latitude"]
				print "%s|%s|%s|%s|%s" % (asn, city.encode('utf-8') , country.encode('utf-8'), lon, lat)
				ip_list = []
				continue
			if (re.match(r"((2[0-4]\d|25[0-5]|1\d\d|[1-9]\d|\d)\.){3}((2[0-4]\d|25[0-5]|1\d\d|[1-9]\d|\d))",line)):
				ip_list.append(line)
		except EOFError:
			break
		except Exception,e:
			print type(city)
			print ip
			print e
			break

if __name__ == "__main__":
	main(sys.argv)
