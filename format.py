import sys
import json

node_index={
	"lon":0,
	"lat":1,
	"info":2
}

info_index={
	"name":0,
	"asn":1,
	"country":2,
	"city":3,
	"comment":4
}

def caida():
	nodes=[]
	while True:
		try:
			line=raw_input()
			fields=line.split('|')
			lon=fields[4]
			lat=fields[5]
			if (lon=="" or lat==""):
				continue
			name=fields[0]
			asn=fields[2]
			country=fields[1].split(", ")[1]
			city=fields[1].split(", ")[0]
			comment=fields[3]
			info={
				"name":name,
				"asn":asn,
				"country":country,
				"city":city,
				"comment":comment
			}
			node={
				"lon":lon,
				"lat":lat,
				"info":info
			}
			nodes.append(node)
		except EOFError:
			print json.dumps(nodes)
			break
		except Exception, e:
			sys.stderr.write("%s\n"%(e))
			exit()

def iplane():
	nodes=[]
	while True:
		try:
			line=raw_input()
			fields=line.split('|')
			lon=fields[1]
			lat=fields[2]
			if (lon=="" or lat=="" or lon=="*" or lat==""):
				continue
			name=fields[0]
			info={
				"name":name,
				"asn":"*",
				"country":"*",
				"city":"*",
				"comment":"*"
			}
			node={
				"lon":lon,
				"lat":lat,
				"info":info
			}
			nodes.append(node)
		except EOFError:
			print json.dumps(nodes)
			break
		except Exception, e:
			sys.stderr.write("%s\n"%(e))
			exit()

def lg():
	nodes=[]
	while True:
		try:
			line=raw_input()
			fields=line.split('|')
			lon=fields[3]
			lat=fields[4]
			if (lon=="" or lat=="" or lon=="*" or lat=="*"):
				continue
			name=fields[0]
			asn=fields[0]
			country=fields[1]
			city=fields[2]
			info={
				"name":name,
				"asn":asn,
				"country":country,
				"city":city,
				"comment":"*"
			}
			node={
				"lon":lon,
				"lat":lat,
				"info":info
			}
			nodes.append(node)
		except EOFError:
			print json.dumps(nodes)
			break
		except Exception, e:
			sys.stderr.write("%s\n" %(e))
			exit()

def usage():
	print "cat caida/iplane/lg | python format.py caida/iplane/lg"

def main(argv):
	if (len(argv) <2):
		usage()
		exit()
	source = argv[1]
	if (source == "caida"):
		caida()
	elif (source == "iplane"):
		iplane()
	elif (source == "lg"):
		lg()

if __name__ == "__main__":
	main(sys.argv)
