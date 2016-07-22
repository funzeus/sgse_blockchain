from OpenSSL import crypto
from Crypto.PublicKey import RSA
from Crypto import Random

'''
TODO:
    1. 데이터 주고 받을 때 퍼블릭키랑 같이 전송할 것.
    2. 리시브한 퍼블릭키로 복호화하는 기능 추가.
'''


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



    # def generateKeyPair(self, keyType, bits):
    #     pkey = crypto.PKey()
    #     pkey.generate_key(keyType, bits)
    #     open('PrivateKey.pem', 'w').write(crypto.dump_privatekey(crypto.FILETYPE_PEM), pkey)
    #     open('PublicKey.pem', 'w').write(crypto.dump_publickey(crypto.FILETYPE_PEM), pkey)

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


