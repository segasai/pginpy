"""Sqlutilpy module to access SQL databases
"""
from __future__ import print_function
import os
import tempfile
import subprocess
import psycopg2


class Server:
    def __init__(self, td, popen, port):
        self.td = td
        self.popen = popen
        self.port = port

    def getConnection(self):
        db = 'postgres'
        return psycopg2.connect(database=db, port=self.port, host='localhost')

    def __del__(self):
        self.popen.terminate()
        del self.td


def createServer(prefix=None, tmpdir=None, port=5444):
    td = tempfile.TemporaryDirectory(prefix=tmpdir)
    temppath = td.name
    if prefix is None:
        prefix = ''
    else:
        prefix = prefix + '/'
    dbpath = temppath + '/db'
    stat = os.system(f'{prefix}initdb -D {dbpath}')
    os.makedirs(temppath + '/log')
    if stat != 0:
        raise Exception('xx')
    P = subprocess.Popen([
        f'{prefix}postgres', '-r', temppath + '/log', '-p', f'{port}', '-D',
        dbpath
    ])

    return Server(td, P, port)


def stopServer():
    return 0
