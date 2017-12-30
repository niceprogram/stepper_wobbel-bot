#-----------------------------------
# Name: wobbelbot
#
# Author: niceprogram
#
# Created: 27-12-2017
#-----------------------------------
#!/usr/bin/env python

# Import required libraries
import time
#import RPi.GPIO as GPIO

# GPIO references
#GPIO.setmode(GPIO.BCM)

# Define the GPIO pins
Set_motorA_pins = [6,13,19,26]
Set_motorB_pins= [12,16,20,21]
OldA = 0;
OldB = 0;

# Set all pins as output
for pinA in Set_motorA_pins:
  print "Setup pins A"
  #GPIO.setup(pinA,GPIO.OUT)
  #GPIO.output(pinA, False)
  
for pinB in Set_motorB_pins:
  print "Setup pins B"
  #GPIO.setup(pinB,GPIO.OUT)
  #GPIO.output(pinB, False)
 
# Define variables
# StepCounter= 0
#Delay_ = 0.002  # for 4 sequence

Delay_ = 0.05 # for 8 sequence .0009

# this function...
def motor_block(directionA, directionB,wheel_turns,speed):
	global Delay_
	global OldA
	global OldB
	StepCounter = 0
	StepCount = 8
	
	# set speed to zero if the wheel direction changes
	if (directionA != OldA or directionB != OldB):
		Delay_ =0.05
	OldA = directionA
	OldB = directionB
	
	
	if (speed < Delay_):
		Delay_ = 0.05 #wheel needs to speed up 
		Speedup = -1
	else: 	
		Delay_ = speed # wheel slow down
		Speedup = 1
	
	# wheel squece	
	if  (directionA == -1):
		Seq_MPA = Seq[::-1]
	elif (directionA == 1):
		Seq_MPA = Seq
	else: 	
		Seq_MPA = stepper_off
		
	
	if  (directionB == -1):
		Seq_MPB = Seq[::-1]
	elif (directionB == 1):
		Seq_MPB = Seq
	else: 	
		Seq_MPB = stepper_off
	
		
		
	while wheel_turns <= 8*2000:
		for pin in range(0, 4):
			xpinB = Set_motorB_pins[pin]
			if Seq_MPB[StepCounter][pin]!=0:
			  print " BStep %i Enable %i" %(StepCounter,pin)
			  #GPIO.output(xpinB, True)
			else:
			  #GPIO.output(xpinB, False)
			  xpinA = Set_motorA_pins[pin]
			if Seq_MPA[StepCounter][pin]!=0:
			  print " AStep %i Enable %i" %(StepCounter,pin)
			  #GPIO.output(xpinA, True)
			else:
			  pass  
			  #GPIO.output(xpinA, False)
			
    		StepCounter += 1
    		
    		if (StepCounter==StepCount):
    			StepCounter = 0
    		if (StepCounter<0):
    			StepCounter = StepCount
    		
    		if (Speedup == -1 and Delay_>speed): # speed up
    			Delay_ = Delay_ + (Speedup*0.001)
    		elif (Speedup == 1 and  speed>Delay_): # speed slow down
    			Delay_ = Delay_ + (Speedup*0.001)
    		else:
    			Delay_ = speed
    			Speedup = 0
    			
    		if Delay_ < 0.05:
    		  Delay_ = speed
    		  Speedup = 0
    		print Speedup	
    		print Delay_
    		time.sleep(Delay_)
	
	
	wheel_turns +=1
	
	
	wheel_turns +=1
	
	


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





# Start main loop
#while 1==1:

motor_block(1,1,3,0.0005)
 # for pinB in range(0, 4):
  #  xpin = Set_motorB_pins[pinB]
  #  if Seq[StepCounter][pinB]!=0:
    #print " Step %i Enable %i" %(StepCounter,xpin)
   #   GPIO.output(xpin, True)
   # else:
   #   GPIO.output(xpin, False
 # StepCounter += 1

  # If we reach the end of the sequence
  # start again
  #if (StepCounter==StepCount):
   # StepCounter = 0
  #if (StepCounter<0):
  #  StepCounter = StepCount

  # Wait before moving on
  #time.sleep(Delay_)


#GPIO.cleanup()

    
