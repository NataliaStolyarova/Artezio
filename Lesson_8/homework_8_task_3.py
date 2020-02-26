"""Function send file HTTP POST and returns the size of file,
which was received n response from server."""
from base64 import b64decode
import os
import requests


def echo(path: str, filename: str):
    """Sends request to the server and gets back
    the jpeg file as octet-stream. Decodes it."""
    url = "https://postman-echo.com/post"
    my_file = os.path.basename(path)
    with open(path, 'rb') as f_to_send:
        with open(filename, 'wb') as f_to_get:
            response = requests.post(url, files={'ImageFile': f_to_send}).json()
            data = response.get('files').get(my_file)
            file = b64decode(data.split(",", 1)[1])
            f_to_get.write(file)
    print(len(file))


echo(r'c:\users\admin\Desktop\1497.JPG', 'newfile.jpg')
