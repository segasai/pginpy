
# pginpy

Python module to start a temporary instance of postgres to run queries against

Author: Sergey Koposov (Uni of Cambridge/CMU/Uni of Edinburgh)

## Installation
To install the package you just need to do pip install pginpy

```
pip install pginpy
```

After installing my suggestion is to use sqlutilpy to query the database, but you
can use standard psycopg2


```python
import pginpy
import sqlutilpy 
# start server in the temp directory, we specifiy the prefix to PG binaries if needed
S = pginpy.PGServer(prefix='/home/koposov/bighome/soft/pginstall13/bin/')
# get the connection
conn=S.getConnection()
# upload stuff in PG using sqlutilpy
sqlutilpy.upload('tab',{'id':np.arange(100),'y':np.arange(100)**.4},conn=conn)
# Run arbitrary queries against it
ID,avgy=sqlutilpy.get(''' select id, avg(y) from tab group by id''',conn=conn)
# stop the server if needed
S.stop()
```
