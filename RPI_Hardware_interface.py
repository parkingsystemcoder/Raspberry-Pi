import RPi.GPIO as GPIO
import time 
import threading
import urllib2
import urllib

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

#close all led 
GPIO.output(17,False)
GPIO.output(22,False)
GPIO.output(27,False)
GPIO.output(10,False)
parking_A = False
parking_B = False


# send code to the database
def access_code1(code):
        url = "http://61.6.80.234:8080/Code_Status_Post.php"
        data = urllib.urlencode({"code":code,"status":"0","id":"1"})
        result = urllib2.urlopen(url, data)
        print ('Done')

def access_code2(code):
        url = "http://61.6.80.234:8080/Code_Status_Post.php"
        data = urllib.urlencode({"code":code,"status":"0","id":"2"})
        result = urllib2.urlopen(url, data)
        print ('Done')


def passes1(my_output):
	print 'the Value of my_output1 is:' , my_output 
	time.sleep(1)
	
	# key in the code 
	print ('Button1 Pressed')
	GPIO.output(27,True)
	
	parking_slot = int(raw_input('Key in the parking_slot code number')) 
	access_code1(parking_slot)
	GPIO.output(27,False)
	


def passes2(my_output):
	print 'the Value of my_output2 is:' , my_output 
	time.sleep(1)
	
	# key in the code 
	GPIO.output(10,True)
	
	parking_slot = int(raw_input('Key in the parking_slot code number'))
	access_code2(parking_slot)
	GPIO.output(10,False)

#============================================

while True:
	input_state1 = GPIO.input(2)
	input_state2 = GPIO.input(3)
	input_state3 = GPIO.input(4)
	my_output1 = False;
	my_output2 = False;
	my_output3 = False;

	
	#parking A
	if input_state1 == False:
		time.sleep(0.1)
		if parking_A == False:
			parking_A = True
			print ('New Car A Come In')
			my_output1 = 'True' 
			GPIO.output(17,True)
			passes1(my_output1)
		elif parking_A == True:
			print ('Car A is still parking')

		
	else : 
		time.sleep(0.1)
		if parking_A == True:
			parking_A = False
			GPIO.output(17,False)
			my_output1 = 'False' 
			print ('Car A is moving out')
			GPIO.output(17,False)
		elif parking_A == False:
			print ('Parking A Available')
			GPIO.output(17,False)
			#status available update
			url = "http://61.6.80.234:8080/Code_Status_Post.php"
			data1 = urllib.urlencode({"code":"NULL","status":"1","id":"1"})
			result = urllib2.urlopen(url, data1)
			print ('Done')




	# Parking B 
	if input_state2 == False:
		time.sleep(0.1)
		if parking_B == False:
			parking_B = True
			print ('New Car B Come In')
			my_output2 = 'True' 
			GPIO.output(22,True)
			passes2(my_output2)
		elif parking_B == True:
			print ('Car B is still parking')


	else : 
		
		time.sleep(0.1)
		if parking_B == True:
			parking_B = False
			GPIO.output(22,False)
			my_output1 = 'False' 
			print ('Car B is moving out')
			GPIO.output(22,False)
		elif parking_B == False:
			print ('Parking B Available')
			GPIO.output(22,False)
			#status available update
			url = "http://61.6.80.234:8080/Code_Status_Post.php"
			data2 = urllib.urlencode({"code":"NULL","status":"1","id":"2"})
			result = urllib2.urlopen(url, data2)
			print ('Done')
