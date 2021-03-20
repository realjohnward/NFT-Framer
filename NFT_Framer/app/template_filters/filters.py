import jinja2 
import requests 
from time import sleep 
from PIL import Image 
import urllib.request 
import qrcode 
from io import BytesIO 
from base64 import b64encode 

ENV = jinja2.Environment(extensions=['jinja2.ext.loopcontrols'])

class NFT:
    def __init__(self, contract_addr, id):
        self.contract_addr = contract_addr
        self.id = id 
        self.url = f'https://opensea.io/assets/{contract_addr}/{id}'

    def qrc(self, w=100, h=100):
        qr = qrcode.QRCode(version=1, box_size=15, border=5)
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buf = BytesIO()
        img.save(buf)
        qrc_html = f'<img width={w} height={h} src="data:image/png;base64,{b64encode(buf.getvalue()).decode()}" />'
        return qrc_html 

    def img(self, classes='', w=100, h=100):
        sleep(0.5)
        req = requests.get(f'https://api.opensea.io/api/v1/asset/{self.contract_addr}/{self.id}/', headers={'User-Agent': 'Mozilla/5.0'})
        data = req.json()
        try:
            img_path = data['image_url']
        except KeyError:
            print(data)
            return f'<img src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" width="{w}" height="{h}" alt="" />'

        if img_path.startswith("http"):
            req = urllib.request.Request(img_path, headers={'User-Agent': 'Mozilla/5.0'})
            img_bytes = urllib.request.urlopen(req).read()
        else:
            img_bytes = Image.open(img_path)
        img_html = f'<img class="{classes}" width={w} height={h} src=\"data:image/png;base64,{b64encode(img_bytes).decode()}\" />'
        return img_html

ENV.filters = {
        'NFT': NFT,
        }