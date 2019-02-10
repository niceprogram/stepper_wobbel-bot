#-----------------------------------
# Name: wobbelbot
#
# Author: niceprogram
#
# Created: 27-12-2017
#-----------------------------------
#!/usr/bin/env python

#Import required libraries
import time
import RPi.GPIO as GPIO

#GPIO references
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins
Set_motorA_pins = [6,13,19,26]
Set_motorB_pins= [12,16,20,21]
OldA = 0;
OldB = 0;
#speed 
bottom_value = 10   #/10000  0.0009   
top_value =  40   #/10000  0.05      
speedrange = (top_value-bottom_value)
Old_speed = 0

# Set all pins as output
for pinA in Set_motorA_pins:
  print ("Setup pins A")
  GPIO.setup(pinA,GPIO.OUT)
  GPIO.output(pinA, False)
  
for pinB in Set_motorB_pins:
  print ("Setup pins B")
  GPIO.setup(pinB,GPIO.OUT)
  GPIO.output(pinB, False)
 
# Define variables




# this function gets the motor to turn
def motor_block(directionA, directionB,wheel_turns,speed_percent):
	global Seq_MPA
	global Seq_MPB
	global OldA			#old determines if the wheel has changed direction
	global OldB
	global Old_speed
	Wheel = 0
	print (" turns %i speed %i" %(wheel_turns,speed_percent))
	wheel_turns=wheel_turns*4096/8
	
	# set speed_percent to zero if the wheel direction changes
	if (directionA != OldA or directionB != OldB):
		Old_speed = 0
	
	OldA = directionA
	OldB = directionB
	
	
	if (speed_percent > Old_speed):
		Speedup = 1
		print (" SpeedUP")
	else: 	
		Speedup = -1 # wheel slow down
		print (" SlowDOWN")
	
	# wheel squence [0001]	
	if  (directionA == -1):
		Seq_MPA = Seq[::-1]
		print (" A forward")
	elif (directionA == 1):
		Seq_MPA = Seq
		print (" A backward")
	else: 	
		Seq_MPA = stepper_off
		print (" A stop")
		
	
	if  (directionB == -1):
		Seq_MPB = Seq[::-1]
		print (" B forward")
	elif (directionB == 1):
		Seq_MPB = Seq
		print (" B backward")
	else: 	
		Seq_MPB = stepper_off
		print (" B stop")
		
	print (" OLD Speed =  %i " %(Old_speed))
	current_speed = Old_speed
    #slow down  from 100%-0% in half a turn
	if (speed_percent < Old_speed):
		while Wheel <= wheel_turns and current_speed > speed_percent: #tagret speed
		  speed_value = speedrange-((current_speed * speedrange) / 100) + bottom_value 
		  print (" Slow Down %i from %i" %(current_speed,speed_value))
		  turn_wheel(speed_value)
		  current_speed = current_speed - 1
		  Wheel = Wheel + 1
	
	#speed up
	elif (speed_percent > Old_speed):
		while Wheel <= wheel_turns and current_speed < speed_percent:
		  speed_value = speedrange-((current_speed * speedrange) / 100) + bottom_value 
		  print (" Speed UP %i from %i" %(current_speed,speed_value))
		  turn_wheel(speed_value)
		  current_speed = current_speed + 1
	
	#contant speed
	else:
		pass
		
	Speedup = 0
	
	speed_value = speedrange-((current_speed * speedrange) / 100) + bottom_value 
	print ("contanst Speed @ %i wheels need to turn %i " %(speed_value,(wheel_turns-Wheel)))
	while Wheel <= wheel_turns:
		
		  
		turn_wheel(speed_value)
		Wheel = Wheel + 1
	print (" Done ")
	Old_speed = speed_percent

	
	
	#constant speed

	
	
		
def turn_wheel(Delay_):
	Step8Counter = 0	
	Delay_ = Delay_/float(10000)
	while Step8Counter < 8:
		
		for pin in range(0, 4):
			
			xpinB = Set_motorB_pins[pin]#Get GPIO
			if Seq_MPB[Step8Counter][pin]!=0:
				#print " BStep %i Enable %i" %(Step8Counter,xpinB)
				GPIO.output(xpinB, True)
			else:
				GPIO.output(xpinB, False)
			
			xpinA = Set_motorA_pins[pin]
			if Seq_MPA[Step8Counter][pin]!=0:
				#print " AStep %i Enable %i" %(Step8Counter,xpinA)
				GPIO.output(xpinA, True)
			else:
				GPIO.output(xpinA, False)
				
						
		
		time.sleep(Delay_)
		Step8Counter += 1	
		
		
	
	
	
	
	
	


# stepper_code8 sequence
Seq= []
Seq= range(0, 8)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

stepper_off = [0,0,0,0]*8
#
#
# start the stepper program
#
#
#
#

for count in range(10):
  motor_block(1,-1,2,100)
  motor_block(-1,1,0.1,0)
  motor_block(-1,1,1,50)
  motor_block(1,-1,0.1,0)
  motor_block(-1,1,1,0)
  pass

#motor_block(1,-1,2,100)
#motor_block(-1,1,0.1,0)
#motor_block(-1,1,1,50)
#motor_block(1,-1,0.1,0)
#motor_block(-1,1,1,0)





#GPIO.cleanup()

    
