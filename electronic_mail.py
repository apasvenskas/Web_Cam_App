import imghdr
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("PASSWORD")
email_addr = "audrius13toto@gmail.com"
receiver = "audrius13toto@gmail.com"

def send_email(image_path):
    print("send_email function starts")
    email_message = EmailMessage()
    email_message["Subject"] = "New object detected"
    email_message.set_content("Hello, the following object was detected")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype = "image", subtype = imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_addr, password)
    gmail.sendmail(email_addr, receiver, email_message.as_string())
    gmail.quit()
    print("Send email function ended.")

if __name__ == "__main__":
    send_email(image_path="images/19.png")