import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = "no-reply@gmail.com"
toaddr = "rmy1997@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
name="Ramya"
location="Bangalore"#get from cloud
msg['Subject'] = "EMERGENCY!! DANGER TO"+ name
body = "PERSON IS IN DANGER. PLEASE CLICK ON FOLLOWING LINK TO IDENTIFY HIS/ LOCATION" + location
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("throughoureyesarm@gmail.com", "xyzabc123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
