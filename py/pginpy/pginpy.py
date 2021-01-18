"""Sqlutilpy module to access SQL databases
"""
from __future__ import print_function
import os
import tempfile
import subprocess
import psycopg2


class PGServer:
    def __init__(self, prefix=None, tmpdir=None, port=5444):
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
        self.popen = subprocess.Popen([
            f'{prefix}postgres', '-r', temppath + '/log', '-p', f'{port}',
            '-D', dbpath
        ])
        self.td = td
        self.port = port

    def getConnection(self):
        db = 'postgres'
        return psycopg2.connect(database=db,
                                port=self.port,
                                user=os.getlogin(),
                                host='localhost')

    def __del__(self):
        self.stop()
        self.td.cleanup()

    def stop(self):
        self.popen.terminate()
