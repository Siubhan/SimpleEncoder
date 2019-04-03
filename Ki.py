from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import wx

from Uppr import UpprP


class Ki_RSA():
    def __init__(self, mode, data,public=None):
        self.pub=public
        data = data.encode('utf-8')
        if mode == 'encrypt':
            self.val = self.encrypt(data)
        else:
            self.val = self.decrypt(data)

    def encrypt(self, txt):
        #private_key = RSA.generate(2048)
        #with open('privatekey', 'wb') as f:  # dialog + name file key
        #    f.write(private_key.export_key('PEM'))

        #public_key = private_key.publickey()

        #with open('publickey', 'wb') as f: # dialog + name file key
        #   f.write(public_key.export_key())

       # with open('privatekey', 'rb') as f:
        #    private_key = RSA.import_key(f.read())

        with open(self.pub, 'rb') as f:
            public_key = RSA.import_key(f.read())

        session_key = get_random_bytes(16)

        cipher = PKCS1_OAEP.new(public_key)
        enc_session_key = cipher.encrypt(session_key)

        cipher_AES = AES.new(session_key, AES.MODE_EAX)
        cipher_text, tag = cipher_AES.encrypt_and_digest(txt)

        upp = UpprP(None, title='Запис до файлу', style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.CAPTION)
        upp.ShowModal()
        upp.Destroy()
        with open(upp.a, 'wb') as f: #dialog + name file data
            [f.write(x) for x in (enc_session_key, cipher_AES.nonce, tag, cipher_text)]

        return 'Успiшно зашифровано!'

    def decrypt(self, txt):

        with open('privatekey', 'rb') as f:
            private_key = RSA.import_key(f.read())
        up = UpprP(None, title='Зчитування шифру RSA', style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.CAPTION)
        up.ShowModal()
        up.Destroy()
        with open(up.a, 'rb') as f:
            enc_session_key, nonce, tag, cipher_text = [f.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

        cipher_RSA = PKCS1_OAEP.new(private_key)
        session_key = cipher_RSA.decrypt(enc_session_key)

        cipher_AES = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_AES.decrypt(cipher_text)
        return data.decode('utf-8')

    def getVal(self):
        return self.val









