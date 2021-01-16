import ssl, smtplib
#smtplib is the module used by python to send emails through SMTP.
#The ssl module is used to access the Operating System Socket.

port = 465
#This port will be required later.

email = input("Enter your email: ")
#You key in the email address you want to send an email with.
password = input("Enter your password: ")
#This is the password to the email inputed before

recipient = input("Enter the email address to send the email to: ")
#This is the email address which the emai is being sent to.
subject = input("What is the subject of the email: ")
#This is the subject head of the email
text = input("Type your email here: ")
#This is the body of the email.
#We combine the subject and the text to form the subject head and the body.
message = "Subject: {}\n\n{}".format(subject, text)

context = ssl.create_default_context()
#This method just creates a new class instance for implemenmtation of a secure protocol.

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as servers:
    #This syncs the local smtp server in the localhost with Gmail's server
        server.login(email,password)
        #This is the login credentials being checked.
        server.sendmail(email, recipient,message)
        #The server is initialized to send an email with the three parameters 
