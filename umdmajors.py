import urllib
from BeautifulSoup import BeautifulSoup
import csv

all_rows = []

headers = [u'majorName', u'school', u'webAddress']

all_rows.append(headers)

link = "http://www.admissions.umd.edu/academics/Majors.php?m=1"
f = urllib.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile)

content = soup.find("div", {'class':'chld3OneColContent'})

content1 = content.findAll('a', href=True)

for item in content1:
	row_content = []

	if (item['href'].find('http') != -1 and len(item.contents[0].split('&nbsp;')) > 1):
		row_content.append(item.contents[0].split('&nbsp;')[0])
		row_content.append(item.contents[0].split('&nbsp;')[1].replace('(', '').replace(')', ''))
		row_content.append(item['href'])

		all_rows.append(row_content)

print all_rows

handle = open('/Users/jiconf/Desktop/umdmajors.csv', 'w')
outfile = csv.writer(handle)

outfile.writerows(all_rows)
