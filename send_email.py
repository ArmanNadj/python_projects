#Resource used to aid in the creation of this project: https://realpython.com/python-send-email/
#Address to go to in order switch less secure setting to On -> https://www.google.com/settings/security/lesssecureapps
#The reason the less secure setting needs to be switched to On is 
#because Google does not allow smtplib to be used since it is classified as less secure

#program compiles & runs as python3 send_email.py

import sys, fileinput
import os
import smtplib, ssl

if __name__ == '__main__':
    port_number = 465 #used in SSL. options are 587, 465, and 25
    SMTP_Server = "smtp.gmail.com"
    sending_address = input("Enter your email address: ")
    print()
    sending_password = input("Enter your email password: ")
    print()
    receiving_address = input("Enter the receiving email address: ")
    print()
    email_body = input("Enter the body of the email: ")
    print()

    SSL_Context = ssl.create_default_context()
    try:
        smtplib.SMTP_SSL(SMTP_Server, port_number).login(sending_address, sending_password)
    except Exception as ex:
        print(f"Unable to login to {sending_address}")
        print(f"The exception given is -> {ex}")
        print("If unable to login, visit this link and turn the access to On -> https://www.google.com/settings/security/lesssecureapps")
        smtplib.SMTP_SSL(SMTP_Server, port_number, context=SSL_Context).quit()
        quit()   
    print(f"Successfully logged in to {sending_address}.\nSending email...")
    try:
        smtplib.SMTP_SSL(SMTP_Server, port_number, context=SSL_Context).sendmail(sending_address, receiving_address, email_body)
    except Exception as ex:
        print(f"Unable to send email from {sending_address} to {receiving_address}")
        print(f"The exception given is -> {ex}")
        smtplib.SMTP_SSL(SMTP_Server, port_number, context=SSL_Context).quit()
        quit()
    print(f"Email sent from {sending_address} to {receiving_address}\nClosing SMTP Server")
    smtplib.SMTP_SSL(SMTP_Server, port_number, context=SSL_Context).quit()
    