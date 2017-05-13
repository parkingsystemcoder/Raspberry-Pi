import RPi.GPIO as GPIO
import time 
import threading

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
def access_code(code):
	print('code :' + code)


def CarAvailableA(CarSlotA):
	print 'the Value of my_output1 is:' , CarSlotA 
	time.sleep(5)
	
	# key in the code 
	print ('Button1 Pressed')
	GPIO.output(27,True)
	
	SlotACode = raw_input('Key in the parking_slot code number')
	access_code(SlotACode)
	GPIO.output(27,False)
	


def CarAvailableB(CarSlotB):
	print 'the Value of my_output2 is:' , CarSlotB 
	time.sleep(5)
	
	# key in the code 
	GPIO.output(10,True)
	
	SlotBCode = raw_input('Key in the parking_slot code number')
	access_code(SlotBCode)
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
		time.sleep(0.5)
		if parking_A == False:
			parking_A = True
			print ('New Car A Come In')
			CarSlotA = 'True' 
			GPIO.output(17,True)
			CarAvailableA(CarSlotA)
		elif parking_A == True:
			print ('Car A is still parking')
				
		
	else : 
		time.sleep(0.5)
		if parking_A == True:
			parking_A = False
			GPIO.output(17,False)
			CarSlotA = 'False' 
			print ('Car A is moving out')
			GPIO.output(17,False)
		elif parking_A == False:
			print ('Parking A Available')
			GPIO.output(17,False)




	# Parking B 
	if input_state2 == False:
		time.sleep(0.5)
		if parking_B == False:
			parking_B = True
			print ('New Car B Come In')
			CarSlotB = 'True' 
			GPIO.output(22,True)
			CarAvailableB(CarSlotB)
		elif parking_B == True:
			print ('Car B is still parking')



	else : 
		
		time.sleep(0.5)
		if parking_B == True:
			parking_B = False
			GPIO.output(22,False)
			CarSlotB = 'False' 
			print ('Car B is moving out')
			GPIO.output(22,False)
		elif parking_B == False:
			print ('Parking B Available')
			GPIO.output(22,False)
