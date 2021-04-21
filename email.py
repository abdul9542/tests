import smtplib
conn = smtplib.SMTP("smtp.gmail.com", 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('jackshew9542@icloud.com', "Jack.9542")
conn.sendmail("jackshew9542@icloud.com","abdulrub9542@gmail.com", "Subject: So long...... \n\n Dear all")
conn.quit()