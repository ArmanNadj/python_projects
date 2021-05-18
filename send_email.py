#Sending emails via CLI by implementing smtplib (Simple Mail Transfer Protocol)
    #by: Arman Nadjarian
    #date of completion: 05/18/2021

#URL to visit in order switch Less Secure App setting to On -> https://www.google.com/settings/security/lesssecureapps
    #The reason the Less Secure App setting needs to be switched to On is 
    #because Google does not allow smtplib to be used since it is classified as a Less Secure App

#Program compiles & runs as ------->   python3 send_email.py

import sys, fileinput
from os import system, name #system and name used in clearing screen
import smtplib, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pathlib import Path
import getpass


#Windows name = 'nt'
#Mac and Linux name = 'posix'
def clr():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


#program begins here
if __name__ == '__main__':
    clr()
    port_number = 465 #used in SSL
    SMTP_Server = "smtp.gmail.com"
    SSL_Context = ssl.create_default_context()
    #server = smtplib.SMTP_SSL(SMTP_Server, port_number, SSL_Context)
    server = smtplib.SMTP_SSL(SMTP_Server, port_number)
    print("*** This Python Program Allows You To Send An Email via CLI ***\n\n")

    try:
        sending_address = input("Enter your email address: ")
        print()
        print("For added security, no characters are displayed as you type your password.")
        sending_password = getpass.getpass() #gets the password, does not show characters while typing
        print()
        clr()
        print(f"Attempting to login to {sending_address}\n")
        server.login(sending_address, sending_password) #logs user in
    except Exception as ex:
        print(f"\n*** Unable to login to {sending_address} ***\n")
        print(f"The exception given is -> {ex}\n")
        print("If unable to login, visit this link and turn the access to On -> https://www.google.com/settings/security/lesssecureapps")
        quit()   
    print(f"\nSuccessfully logged in to {sending_address} \nPreparing to send an email...\n")
    try:
        receiving_address = input("Enter the receiving email address: ")
        print()
        email_subject = input("Enter the email subject: ")
        print()        
        email = MIMEMultipart()
        email['Subject'] = email_subject
        email['From'] = sending_address
        email['To'] = receiving_address
        email_body = input("Enter the body of the email: ")
        email.attach(MIMEText(email_body, 'plain'))
        print()

        attach_file_name = input("Enter a file pathway. The given file will be attached to the email (or enter 0 (zero) to not attach a file): ")
        try:
            if attach_file_name != '0' and attach_file_name.lower() != "zero":
                attach_file_name = Path(attach_file_name)
                attach = MIMEApplication(open(attach_file_name, 'rb').read(), Name=basename(attach_file_name.name)) #gathers file for attachment
                attach['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(attach_file_name)) #assesses formatting of the file
                email.attach(attach) #attaches the file
                server.sendmail(sending_address, receiving_address, email.as_string()) #sends the email
            else:
                server.sendmail(sending_address, receiving_address, email.as_string()) #sends the email   
        except Exception as ex2:
            print("\n*** Unable to attach the given file. Aborting email. ***\n")
            print(f"Error: {ex2} \n")
            quit()

    except Exception as ex:
        print(f"\n*** Unable to send email from {sending_address} to {receiving_address} ***\n")
        print(f"The exception given is -> {ex}\n")
        quit()

    print(f"\nEmail sent from {sending_address} to {receiving_address}\n")

    
