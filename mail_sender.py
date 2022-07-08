import sys
  
from_ = str(sys.argv[1])  
print("De:", from_)
from_pass = str(sys.argv[2])  
print("Senha:", from_pass)
to = str(sys.argv[3])  
print("Para:", to)
message_k = str(sys.argv[4])  
print("Mensagem:", from_pass)




from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = message_k
 
# setup the parameters of the message
password = from_pass #"vpicigirzpglsxfj"
msg['From'] = from_
msg['To'] = to
msg['Subject'] = message
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To']))
