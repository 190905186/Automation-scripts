"""
This script helps in sending email to the multiplw recipents

"""


import smtplib
import ssl

# SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 465

# Sender and recipient details
from_address = 'Winzo Shop'
to_address = ['']  # Recepients List

# Authentication details
username = ''  # Sender Email
password = ''  # Sender Password


# Email message details
subject = '🎉 Exclusive Offer Inside! Get 10% Off Your Next Purchase'
body = '''\
Dear Customer,

We are thrilled to offer you an exclusive discount on your next purchase as a token of our appreciation for being a valued customer. Use the coupon code below during checkout to enjoy a 10% discount on your order:

Coupon Code: DISCOUNT10

Whether you're looking for stylish apparel, trendy accessories, or high-quality products, now is the perfect time to shop and save! Explore our latest collection and treat yourself to something special.

Hurry! This offer is valid for a limited time only. Don't miss out on the chance to save on your favorite items.

Shop now: https://xyz.com

Thank you for choosing WinzoShop. We look forward to serving you again soon!

Best regards,
Winzo Shop
'''


# Create an SSL/TLS context
context = ssl.create_default_context()

# Connect to the SMTP server using SSL/TLS
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    # Enable debugging to print the server's responses
    server.set_debuglevel(1)

    # Login to the SMTP server
    server.login(username, password)

    # Create the email message
    message = f'From: {from_address}\r\nSubject: {subject}\r\nTo: {to_address}\r\n\r\n{body}'
    message = message.encode()  # Convert the message to bytes

    # Send the email
    server.sendmail(from_address, to_address, message)
