'''
Created on 19 Feb 2012

@author: simon
'''
import sys
import os
import threading

class moduleMain( threading.Thread ):
    
    def runFileExist( self, filePath ):
        """
        fileexists module

	pass in a file name and path as the first paramater
	The module returns true if the file exists and false if it does not
        """
        self.argument = sys.argv[1]
        if os.path.exists(filePath):
            return {'status': True, 'message': "The file exists"}
        else:
            return {'status': False, 'message': "The file does not exist"}

    def runFileSize(self, minSize=None, maxSize=None):
	pass

class createTask(object):
    filePath = ""
    minSize = 0
    maxSize = 0
    frequency = 0
    def fileExist(self):
	self.getFilePath()
	self.getFrequency()
	return ["FileExist('" + self.filePath + "')",self.frequency]

    def minSize(self):
	self.getMinSize()
        self.getFilePath()
	self.getFrequency()
	return ["minSize('" + self.filePath + "', " + self.minSize + ")",self.frequency]

    def maxSize(self):
	self.getMaxSize()
        self.getFilePath()
	self.getFrequency()
	return ["maxSize('" + self.filePath + "', " + self.maxSize + ")",self.frequency]

    def getNotificationOptions():
	#ToDo: Use this function to get the list of available notification methods.
	#Present the user with the option to choose one as part of creating the task.	
	pass
   

    def getFilePath(self):
	self.filePath = raw_input("Enter full path of file to monitor (not a relative path): ")

    def getMinSize(self):
        self.minSize = raw_input("Enter min size of file (end with b, k, m, g) to trigger alarm: ")

    def getMaxSize(self):
        self.maxSize = raw_input("Enter max size of file (end with b, k, m, g) to trigger alarm: ")

    def getFrequency(self):
	self.frequency = raw_input("Enter frequency (seconds) to run this task: ")
