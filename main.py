import requests  # http requests
from bs4 import BeautifulSoup  # web scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime


now = datetime.datetime.now()
# email content placeholder
content = ''
# extracting Hacker News Stories
def extract_news(url):
    print('Extracting CoinDesk Titles...')
    cnt = ''
    cnt += ('<b><a href="https://www.coindesk.com/">CoinDesk </a > <a style="color:red;"> Top Crypto News : </a> </b>' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + '\n' + '<br>' + '-' * 100 + '\n'+ '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    tags = {tag.text for tag in soup.find_all('a', attrs={'class':'headline'})}
    # iterate all tags
    for i , tag in enumerate(tags):
        cnt += ('<b >' + str(i+1) + ' : ' + '</b>' + tag + "\n" + '<br>')
    return (cnt)


cnt = extract_news('https://www.coindesk.com')
content += cnt
content += ('<br>' + '-' * 100 + '\n' + '<br>')
content += ('<br><br>End of The News for today')

# lets send the email

print('Composing Email...')

# update your email details
# make sure to update the Google Low App Access settings before

SERVER = 'smtp.gmail.com'  # "your smtp server"
PORT = 587  # your port number
FROM = 'llol1231235@gmail.com'  # "your from email id"
TO = 'llol1231235@gmail.com'  # "your to email ids"  # can be a list
PASS = '1235llol'  # "your email id's password"

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top CoinDesk News [Automated Email]' + ' ' + str(now.day) + '/' + str(now.month) + '/' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()