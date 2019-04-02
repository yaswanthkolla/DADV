import requests
from bs4 import BeautifulSoup
import csv


code = ["53", "67", "33", "10", "79", "52", "3", "45", "40", "85", "31", "69", "80", "1", "46", "5", "65", "89", "43",
        "30", "29", "55", "36", "87", "88", "58", "19", "47", "60", "76", "74", "64","63", "61", "86", "37", "34", "12",
        "81", "44", "22", "72", "82", "73", "41", "18", "77", "83", "90", "21", "25", "13", "57", "15", "26", "9",
        "42", "2", "24", "32", "78", "27", "84", "70", "23", "38", "71", "62", "14", "6", "4", "16", "48", "50",
        "51", "49", "54", "75", "7", "20", "68", "35", "8", "59", "39", "17", "56", "11", "28", "66"]

for i in code:
    #var=str(j);
    page = requests.get("http://eciresults.nic.in/ConstituencywiseS26"+i+".htm?ac="+i)
    soup = BeautifulSoup(page.content,'html.parser');
    table = soup.find('table', border="1");
    print(table)
    t_rows = table.find_all('tr', style="font-size:12px;");
    #print(t_rows)
    with open("Chhattisgarh"+i+".csv", 'w') as f:

        for row in t_rows:
            result = row.findAll('td');
            # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            data_writer.writerow(['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()),
                                      '%s' % (result[2].text.strip())]);
            #print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));



"""""
for j in range(1,231):
    page = requests.get("http://eciresults.nic.in/ConstituencywiseS12" + str(j) + ".htm?ac="+str(j))
    soup = BeautifulSoup(page.content, 'html.parser');
    table = soup.find('table', border="1");
    # print(table)
    t_rows = table.find_all('tr', style="font-size:12px;");
    # print(t_rows)
    with open("Madhya Pradesh" + str(j) + ".csv", 'w') as f:

        for row in t_rows:
            result = row.findAll('td');
            # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            data_writer.writerow(['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()),
                                   int(result[2].text.strip())]);


for k in range(1,41):
    page = requests.get("http://eciresults.nic.in/ConstituencywiseS16" + str(k) + ".htm?ac="+str(k))
    soup = BeautifulSoup(page.content, 'html.parser');
    table = soup.find('table', border="1");
    # print(table)
    t_rows = table.find_all('tr', style="font-size:12px;");
    # print(t_rows)
    with open("Mizoram" + str(k) + ".csv", 'w') as f:

        for row in t_rows:
            result = row.findAll('td');
            # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            data_writer.writerow(['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()),
                                   int(result[2].text.strip())]);

for l in range(1,201):
    page = requests.get("http://eciresults.nic.in/ConstituencywiseS20" + str(l) + ".htm?ac="+str(l))
    soup = BeautifulSoup(page.content, 'html.parser');
    table = soup.find('table', border="1");
    # print(table)
    t_rows = table.find_all('tr', style="font-size:12px;");
    # print(t_rows)
    with open("Rajasthan" + str(l) + ".csv", 'w') as f:

        for row in t_rows:
            result = row.findAll('td');
            # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            data_writer.writerow(['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()),
                                   int(result[2].text.strip())]);

for t in range(1,120):
    page = requests.get("http://eciresults.nic.in/ConstituencywiseS29" + str(t) + ".htm?ac="+str(t))
    soup = BeautifulSoup(page.content, 'html.parser');
    table = soup.find('table', border="1");
    # print(table)
    t_rows = table.find_all('tr', style="font-size:12px;");
    # print(t_rows)
    with open("Telangana" + str(t) + ".csv", 'w') as f:

        for row in t_rows:
            result = row.findAll('td');
            # print("<p>%s%s%s</p>" %(result[0].text.strip(),result[1].text.strip(),result[2].text.strip()));
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            data_writer.writerow(['%s' % (result[0].text.strip()), '%s' % (result[1].text.strip()),
                                   int(result[2].text.strip())]);
"""""



