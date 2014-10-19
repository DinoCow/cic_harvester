from bs4 import BeautifulSoup
import urllib2

import csv

save_dir = "harvest_dir/Guides"
url_file = 'docs.csv'

f = open(url_file)
csv_f = csv.reader(f)

next(csv_f) #skip firstline
for row in csv_f:

	response = urllib2.urlopen(row[0])
	html = response.read()
	soup = BeautifulSoup(html)


	title = soup.title.string
	main = soup.find('main').get_text().encode('utf-8').strip()
	print(main)
	print(title)

	#save to file
	filename = save_dir + "/" + soup.title.string + ".html"
	
	outfile = open(filename, 'w')
	outfile.write("<html>\n")
	outfile.write("<body>\n")
	outfile.write(main)
	outfile.write("</body>\n")
	outfile.write("</html>")
	outfile.close()