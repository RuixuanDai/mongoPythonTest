import pymongo  
import test


hostAndPortRemote = '54.165.246.186:27017'
hostAndPortLocal = 'mongo-query-router:27017'
client = pymongo.MongoClient(host=['54.165.246.186:27017'], \
                             username="mongo-admin", password="password", authSource='admin')


writeTime = []
delTime = []

test.test(client, writeTime,delTime,5)

print delTime
print writeTime