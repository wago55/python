import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import os

authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user("masaki","19990501","/Users/wago55/Desktop/Git",perm="elradfmw")

handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer

sever = pyftpdlib.servers.FTPServer(("10.0.0.1",10021), handler)
sever.serve_forever()
