import socket
import struct
import threading
import traceback
import time

def peerdebug(msg):
    print "[%s] %s" % (str(threading.currentThread().getName()), msg)

class Peer:
    def __init__(self, _maxpeers, _serverport, _myid=None, _serverhost=None):
        self.debug = 0
        self.maxPeers = int(_maxpeers)
        self.serverPort = int(_serverport)

        if _serverhost:
            self.serverHost = _serverhost
        else:
            self.myID = '%s:%d' % (self.serverHost, self.serverPort)
        self.peerLock = threading.Lock()

        self.peers = {}
        self.shutdown = False

        self.handlers = {}
        self.router = None

    def __initserverhost(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connet(("www.google.co.kr", 80))
        self.serverHost = sock.getsockname()[0]
        sock.close()

    def __debug(self, msg):
        if self.debug:
            peerdebug(msg)

    def __handlepeer(self,clientsock):
        self.__debug('New Child' + str(threading.currentThread().getName()))
        self.__debug('Connected' + str(clientsock.getpeername()))

        host, port = clientsock.getpeername()
        peerconn = PeerConnection(None, host, port, clientsock, debug=False)

        try:
            msgtype, msgdata = peerconn.recvdata()
            if msgtype:
                msgtype = msgtype.upper()
            if msgtype not in self.handlers:
                self.__debug('Not handled: %s: %s' % (msgtype, msgdata))
            else:
                self.__debug('Handling peer msg: %s: %s' % (msgtype, msgdata))
                self.handlers[msgtype](peerconn, msgdata)

        except KeyboardInterrupt:
            raise

        except:
            if self.debug:
                traceback.print_exc()
        self.__debug('Disconnecting' + str(clientsock.getpeername()))
        peerconn.close()

    def __runstabilizer(self, stabilizer, delay):
        while not self.shutdown:
            stabilizer()
            time.sleep(delay)

    def setmyid(self, _myid):
        self.myID = _myid

    def startstabilizer(self, stabilizer, delay):
        t = threading.Thread(target=self.__runstabilizer, args=[stabilizer, delay])
        t.start()

    def addhadler(self, msgtype, handler):
        assert len(msgtype) == 4
        self.handlers[msgtype] = handler

