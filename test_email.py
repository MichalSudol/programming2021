# send an email via gmail
# author Andrew Beatty
# used and tested by Michal Sudol G00398852@gmit.ie

import smtplib

username = 'Jameson8ond@gmail.com'
password = 'Pass'
toEmail = 'Jameson8ond@gmail.com'
message = 'hi there greetings, this is test email from G00398852@gmit.ie'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username, toEmail, message)
