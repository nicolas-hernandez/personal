
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        if data=='SOY Fulano':
            self.transport.write('TABLERO 4 3')
        elif data=='CONFIRMO':
            self.transport.write('OK')
        elif data.startswith('CARTA 0'):
            self.transport.write('ERROR')
        elif data.startswith('CARTA'):
            self.transport.write('OK')
        elif data == 'UPDATE':
            self.transport.write('STATUS ----ddcp----')
        else:
            self.transport.write('Respuesta: ' + data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(5481,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
