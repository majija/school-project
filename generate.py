#С помощью этих 3 строчек можно делать qr коды (для этого в функцию pyqrcode.create() кладем нужный id)


import pyqrcode

qr = pyqrcode.create('whatever')
qr.png('filename.png', scale=10)
