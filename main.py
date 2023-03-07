import csv
from send_email import send_email
from datetime import datetime


today = datetime.now()
dateDay = today.day

dateDay -= 2  # -2 because i wrote and used the code on the third of march LOL
# there is a better way of doing this, but this was done because i needed the code quickly to send mails
# from march 3rd to 13th, and not all days of the month are used.


with open('sheet1.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    dataList = []
    for row in data:
        dataList.append(row)

for i in range(10):  # 10 quotes
    if dateDay == i:
        tmpDay = dataList[i-1][0]
        tmpQuote = dataList[i-1][1]
        tmpDaysLeft = dataList[i-1][2]
        tmpAuthor = dataList[i-1][3]

# Change variables to your likings

if (dateDay <= 10):
    send_email(
        subject="enter subject of mail here",  # can also format to include the day
        receiver_email="the email which will receive the mail here",
        name="recipients name in the mail here",
        day=tmpDay,
        dagarKvar=tmpDaysLeft,
        quote=tmpQuote,
        author=tmpAuthor
    )
