#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:56:40 2017

@author: ruixuandai
"""
import timeit
import time



def smallWithoutSharding(client,n=1000):
    #delete the test DB
    client.drop_database("exampleDB")
    
    db = client.exampleDB
    
    collection = db.testCollection
    
    startTime = timeit.default_timer()
    
    for i in range(n):
        dataEntry = {}
        dataEntry['_id']=time.time()
        dataEntry['x']=i
        dataEntry['y']=i
        dataEntry['z']=i
        collection.insert_one(dataEntry)
    
    elapseTime = timeit.default_timer() - startTime
    return elapseTime

def smallWithSharding(client,n=1000):
    print 'smallWithSharding...'
    #delete all entries
    delStartTime = timeit.default_timer()
    db = client.exampleDB   
    collection = db.testCollection
    delResult = collection.delete_many({})
    
    midTime = timeit.default_timer()
    delElapseTime = midTime - delStartTime
    
    for i in range(n):
        dataEntry = {}
        dataEntry['_id']=time.time()
        dataEntry['x']=i
        dataEntry['y']=i
        dataEntry['z']=i
        collection.insert_one(dataEntry)
    writeTime = timeit.default_timer() - midTime
    
    
    return delElapseTime, writeTime

def smallManyWithSarding(client,n=1000):
    print 'smallManyWithSharding...'
    #delete all entries
    delStartTime = timeit.default_timer()
    db = client.exampleDB   
    collection = db.testCollection
    delResult = collection.delete_many({})
    
    midTime = timeit.default_timer()
    delElapseTime = midTime - delStartTime
    
    dataSet = []
    
    for i in range(n):
        dataEntry = {}
        dataEntry['_id']=i
        dataEntry['x']=i
        dataEntry['y']=i
        dataEntry['z']=i
        dataSet.append(dataEntry)
#    print dataSet,13245664
    collection.insert_many(dataSet,ordered=True, bypass_document_validation=True)
    writeTime = timeit.default_timer() - midTime
    
    
    return delElapseTime, writeTime