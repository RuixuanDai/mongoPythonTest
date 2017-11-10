#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:30:45 2017

@author: ruixuandai
"""
import testMethod



def test(client, writeTime, delTime, times):
    for i in range(times):
        delEach,storeTimeEach = testMethod.smallManyWithSarding(client,10000)
        print  i, ':  delTime(s):', delEach, ',  writeTime(s):', storeTimeEach
        writeTime.append(storeTimeEach)
        delTime.append(delEach)