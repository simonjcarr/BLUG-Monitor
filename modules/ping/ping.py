import sys
import subprocess
import threading

class moduleMain( threading.Thread ):
    def run(self, parameter=None):
	"""
	ping module
	accepts hostname or IP address as first paramater.
	Module will ping host and return true if a response is returned or false if no response
	"""
        
        
        ping = subprocess.Popen(["ping","-c","4", parameter],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        result, error = ping.communicate()
        return {"status": 1,"message": result}

    
