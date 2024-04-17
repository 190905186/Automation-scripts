"""
Downloads images from the web if you pass the key word
and limit

"""

# Importing the necessary module and function
from simple_image_download import simple_image_download as simp

# Creating a response object
Response = simp.simple_image_download

# Keyword
Keyword = "dog"

# Downloading images
try:
    Response().download(Keyword, 20)
    print("Images downloaded successfully.")
except Exception as e:
    print("An error occurred:", e)
