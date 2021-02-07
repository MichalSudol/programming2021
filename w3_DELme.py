import smtplib
print('sanity3')

username = 'Jameson8ond@gmail.com'
password = 'Pass'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
'''
server.ehlo()
server.starttls()
server.ehlo()
'''
#Next, log in to the server
server.login(username, password)

#Send the mail
msg = "Hello! / How U Doin? # The /n separates the message from the headers"

server.sendmail(username, "Jameson8ond@gmail.com", msg)
