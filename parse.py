import sys
import HTMLParser

class CaidaTableParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.lines=[]
		self.line=[]
		self.is_body=False
		self.is_td=False
		self.td=""
	
	def handle_starttag(self, tag, attrs):
		if (not self.is_body and tag == "tbody"):
			self.is_body = True
		
		if (self.is_body and tag == "td"):
			self.is_td = True
	
	def handle_endtag(self, tag):
		if (self.is_body and tag == "tr"):
			name=self.line[0]
			toponym=self.line[5]
			asn=self.line[6]
			info=self.line[7]
			self.lines.append("%s|%s|%s|%s" % (name,toponym,asn,info))
			self.line=[]
		if (self.is_td and tag == "td"):
			self.is_td = False
			self.line.append(self.td)
			self.td=""
		
	def handle_data(self, data):
		if (self.is_td):
			self.td+=data

class IplaneTableParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.lines=[]
		self.line=[]
		self.is_body=False
		self.is_td=False
		self.td=""
	
	def handle_starttag(self, tag, attrs):
		if (not self.is_body and tag == "tbody"):
			self.is_body = True
		
		if (self.is_body and tag == "td"):
			self.is_td = True
	
	def handle_endtag(self, tag):
		if (self.is_body and tag == "tr"):
			name=self.line[1]
			lon=self.line[2]
			lat=self.line[3]
			self.lines.append("%s|%s|%s" % (name, lon, lat))
			self.line=[]
		if (self.is_td and tag == "td"):
			self.is_td = False
			self.line.append(self.td)
			self.td=""
		
	def handle_data(self, data):
		if (self.is_td):
			self.td+=data

def parse_caida():
	parser = CaidaTableParser()
	parser.feed(open("table_caida.html",'rb').read())
	for l in parser.lines:
		print l

def parse_iplane():
	parser = IplaneTableParser()
	parser.feed(open("table_iplane.html",'rb').read())
	for l in parser.lines:
		print l

def main(argv):
	if (len(argv) <2 ):
		print "python parse.py caida/iplane"
		exit()
	
	source = argv[1]
	if (source == "caida"):	
		parse_caida()
	elif (source == "iplane"):
		parse_iplane()

if __name__ == "__main__":
	main(sys.argv)
