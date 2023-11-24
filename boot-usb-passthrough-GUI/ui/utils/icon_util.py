import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from io import BytesIO

def get_image_from_url(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        pixmap = QPixmap()
        pixmap.loadFromData(image_data.getvalue())
        return pixmap
    else:
        return None
