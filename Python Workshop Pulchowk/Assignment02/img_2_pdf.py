# Importing modules
import os
import ssl
import img2pdf
import smtplib
import ssl
from email.message import EmailMessage

# Listing the image and storing in a list
photo_list = os.listdir(".")


finalPhoto = []  # Creating an Empty list

# Filtering the images
for image in photo_list:
    if image.endswith(".jpg"):
        finalPhoto.append(image)

# Converting to pdf in binary form
photo_pdf = img2pdf.convert(finalPhoto)

# Open Photos.pdf in wb format
with open("Photos.pdf", "wb") as f:
    f.write(photo_pdf)  # Writing the binary pdf to files
    f.close()


my_address = "077bct090.susheel@pcampus.edu.np"
my_pass = "qmjeoddrrpaljmee"

#Creating email list
email_list = ['broken.heart.24680@gmail.com','sushilthapa9844242743@gmail.com','pdsc.nepal@gmail.com']
for email in email_list:
    # Creating out message
    msg = EmailMessage()  # Create an instance of EmailMessage()
    msg['Subject'] = "Day 2 assignment"
    msg['To'] = email
    msg['from'] = my_address
    msg.set_content(
        'All document are attached in this mail for assignment of day 2.')

    # Opening files to grab data to email
    with open("Photos.pdf", "rb") as f:
        file_data = f.read()
        file_name = f.name

    # Adding attachment to our message
    msg.add_attachment(file_data, maintype='application',
                    subtype='octet.stream', filename=file_name)

    # Sending email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_address,
                my_pass)  # Login to our account
        smtp.send_message(msg)  # Basically send message
        pass

    print("All above progam run goods")























