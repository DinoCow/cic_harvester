from bs4 import BeautifulSoup
import urllib2

import csv

save_dir = "harvest_dir/FAQ"
url = "http://www.cic.gc.ca/english/helpcentre/answer.asp?q=334&t=3"

total_text = ""
for q in range(1, 335):
	qurl = "http://www.cic.gc.ca/english/helpcentre/answer.asp?q=" + str(q) + "&t=3"
	print(qurl)
	response = urllib2.urlopen(qurl)
	html = response.read()
	soup = BeautifulSoup(html)

	title = soup.title.string
	main = soup.find('main')
	
	if main:
		main = main.find_all('p')

	if title == None or main == None:
		continue

	maintext = ""
	for p in main:
		maintext += p.get_text()

	maintext = maintext.encode('utf-8').strip().strip("All questions about this topic").strip().strip("For detailed information, see:Help Centre Home");
	title = title.encode('utf-8').strip()

	if q == 48:
		title = "how do I replace my lost citizenship card or certificate?"

	print(main)
	print(title)

	total_text += "<p>\n"
	total_text += maintext + "\n"
	total_text += "</p>\n"

#save to file
filename = save_dir + "/FAQ_answers.html"

outfile = open(filename, 'w')
outfile.write("<html>\n")
outfile.write("<body>\n")
outfile.write(total_text)
outfile.write("</body>\n")
outfile.write("</html>")
outfile.close()