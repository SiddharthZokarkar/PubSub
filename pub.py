import PubSub
from time import sleep
import keyboard

x = 0
try:	
	while(True):
		
		PubSub.publish_topic(1,"HelloWorld" + " " + str(x))  # PubSub.publish_topic(Topic number , Data) 
		
		#PubSub.subscribe_topic(1)

		x = x+1
		sleep(1)
    
    
except KeyboardInterrupt:
	PubSub.free_memory(1)
	

    	
    

