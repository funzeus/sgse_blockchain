from OpenSSL import crypto
from Crypto.PublicKey import RSA

# git Test

class pkiModule:

    priKey = None
    pubKey = None
    recvPubKey = None

    def __init__(self):
        # type: () -> object
        self.recvPubKey = RSA.importKey()

    def __init__(self,  bits):
        self.check = True
        pkey = crypto.PKey()
        pkey.generate_key(crypto.TYPE_RSA, bits)
        open('PrivateKey.pem', 'w').write(crypto.dump_privatekey(crypto.FILETYPE_PEM,pkey))
        open('PublicKey.pem', 'w').write(crypto.dump_publickey(crypto.FILETYPE_PEM, pkey))
        self.priKey = RSA.importKey(open('PublicKey.pem').read())
        self.pubKey = RSA.importKey(open('PrivateKey.pem').read())

    def dataEncryption(self, msg):
        emsg = self.priKey.encrypt(msg, 'x')[0]
        return emsg

    def dataDecryption(self, encryptMsg):
        originMsg = self.pubKey.decrypt(encryptMsg)
        return originMsg

    def decryptByReceiver(self, encryptMsg, senderPubKey):
        self.recvPubKey = RSA.importKey(senderPubKey)
        dmsg = self.recvPubKey.decrypt(encryptMsg)
        return dmsg

# pki = pkiModule(1024)
# temp = str(pki.pubKey)
#
# print(temp)


