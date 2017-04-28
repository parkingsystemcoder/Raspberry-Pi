import RPi.GPIO as GPIO
import time 
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(06,GPIO.OUT)

#close all led 
GPIO.output(26,True)
GPIO.output(19,False)
GPIO.output(13,False)
parking_A = False
parking_B = False

def access_correct(code):
	print('Code is correct')

	GPIO.output(13,False)
	my_output3 = 'False'



# send code to the database
def access_code(code):
	print('code :' + code)


def passes1(my_output):
	print 'the Value of my_output1 is:' , my_output 
	time.sleep(5)
	
	# key in the code 
	print ('Button1 Pressed')
	GPIO.output(13,True)
	
	# user input (PASS CODE Parking A)
	parking_slot = raw_input('Key in the parking_slot code number')
	access_code(parking_slot)
	GPIO.output(13,False)
	


def passes2(my_output):
	print 'the Value of my_output2 is:' , my_output 
	time.sleep(5)
	
	# key in the code 
	GPIO.output(06,True)
	
	#user B input (PASS CODE Parking B)
	parking_slot = raw_input('Key in the parking_slot code number')
	access_code(parking_slot)
	GPIO.output(06,False)

#============================================
#always loop (main loop)
while True:
	#initialization 
	input_state1 = GPIO.input(2)
	input_state2 = GPIO.input(3)
	input_state3 = GPIO.input(4)
	my_output1 = False;
	my_output2 = False;
	my_output3 = False;

	# Parking A (check whether have car or not)
	# my_output1 => indicator => variable pass to Yi Wei
	# go to passess1 function

	if input_state1 == False:
		
		if parking_A == False:
			parking_A = True
			print ('New Car A Come In')
			my_output1 = 'True' 
			GPIO.output(26,True)
			passes1(my_output1)
		elif parking_A == True:
			print ('Car A is still parking')
				
		
	else : 
		
		if parking_A == True:
			parking_A = False
			GPIO.output(26,False)
			my_output1 = 'False' 
			print ('Car A is moving out')
			GPIO.output(26,False)
		elif parking_A == False:
			print ('Parking A Available')
			GPIO.output(26,False)
	# Parking B
	#my_output2 => indicator => variable pass to Yi Wei
	# go to passess2 funciton

	if input_state2 == False:
		
		if parking_B == False:
			parking_B = True
			print ('New Car B Come In')
			my_output2 = 'True' 
			GPIO.output(19,True)
			passes1(my_output2)
		elif parking_B == True:
			print ('Car B is still parking')



	else : 
		

		if parking_B == True:
			parking_B = False
			GPIO.output(19,False)
			my_output1 = 'False' 
			print ('Car B is moving out')
			GPIO.output(19,False)
		elif parking_A == False:
			print ('Parking B Available')
			GPIO.output(19,False)

	



