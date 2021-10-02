import smtplib

sender = 'avatolzhobaeva@gmail.com'
recipient = 'kannisy1@gmail.com'
password = input(str('Enter your password: '))
message = 'Hello world'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print('Login success')

server.sendmail(sender, recipient, message)
print(f'Email has been sent to {recipient}')