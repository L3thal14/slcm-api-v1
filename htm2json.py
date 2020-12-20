from bs4 import BeautifulSoup
from json import dumps


def Attendance2JSON():
    attendanceJson = list()
    headers = list()
    url = r'attendance.html'
    soup = BeautifulSoup(open(url).read(), features='lxml')
    table = soup.find_all('table')[0]
    # Get Table Headers
    header = table.find_all('tr')[0]
    for h in header.find_all('th'):
        headers.append(h.text.strip())
    data = table.find_all('tr')[1:]
    for row in data:
        cells = row.find_all('td')
        temp = dict()
        for i in range(0, len(headers)):
            temp[headers[i]] = cells[i].text.strip()
        attendanceJson.append(temp)
    toret = {"attendance": attendanceJson}
    return toret


def Internals2JSON():
    subjectsJSON = dict()
    headers = list()
    marksJSON = list()
    url = r'marks.html'
    finalstr = ''
    soup = BeautifulSoup(open(url).read(), features='lxml')
    maindiv = soup.find("div", {"id": "accordion1"})
    subjects = maindiv.find_all_next("div", {"class": "panel panel-default"})
    i = 0
    while(i < 8):
        tables = subjects[i].find_all("table")
        sub_name = subjects[i].find("a").text
        sub_name = sub_name.strip().strip("Subject Code:").strip()
        if(len(tables) == 2):
            finalstr += '<p>' + sub_name + '</p>' + \
                str(tables[0]) + str(tables[1])
        else:
            finalstr += '<p>' + sub_name + '</p>'
        i += 1
    internal2JSON = {"marks": finalstr}
    return internal2JSON


def Calendar2JSON():
    url = r'calendar.html'
    soup = BeautifulSoup(open(url).read(), features='lxml')
    textheader = soup.find_all(
        'div', {'class': 'event-header-odd table-responsive'})
    calendarJson = list()
    # Get Table Headers
    headers = list()
    headers = ['Date', 'Notice', 'Start Date', 'End Date', 'Total Days']
    i = 1
    while(i < 3):
        span = textheader[i].find_all('span')
        j = 0
        temp = dict()
        for k in range(0, len(headers)):
            temp[headers[k]] = span[k].text
        calendarJson.append(temp)
        i += 1
    calendar2JSON = {"calendar": calendarJson}
    return calendar2JSON


def name_scrape():
    urlname = r'homepage.html'
    soup = BeautifulSoup(open(urlname).read(), features='lxml')
    namefinal = soup.find('span', {'id': 'lblUserName'})
    name = namefinal.text
    return name


def image_scrape():
    urlname = r'homepage.html'
    soup = BeautifulSoup(open(urlname).read(), features='lxml')
    image = soup.find('img', {'id': 'Repeater1_Image2_0'})
    url = image['src']
    urlfinal = 'https://slcm.manipal.edu/' + url
    return urlfinal


if __name__ == "__main__":
    attendanceJSON = Attendance2JSON('AttendanceHTML')
    subjectJSON, marksJSON = Internals2JSON('MarksHTML')
    calendar2JSON = Calendar2JSON('calendarHTML')
