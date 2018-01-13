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
bottom_value = 9   #/10000  0.0009   
top_value =  500   #/10000  0.05      
speedrange = (top_value-bottom_value)
Old_speed = 0

# Set all pins as output
for pinA in Set_motorA_pins:
  print "Setup pins A"
  GPIO.setup(pinA,GPIO.OUT)
  GPIO.output(pinA, False)
  
for pinB in Set_motorB_pins:
  print "Setup pins B"
  GPIO.setup(pinB,GPIO.OUT)
  GPIO.output(pinB, False)
 
# Define variables




# this function get the motor to turn
def motor_block(directionA, directionB,wheel_turns,speed_percent):
	global Seq_MPA
	global Seq_MPB
	global OldA			#old determines if the wheel has changed direction
	global OldB
	global Old_speed

	Wheel = 0
	
	
	# set speed_percent to zero if the wheel direction changes
	if (directionA != OldA or directionB != OldB):
		speed_percent = 0
	
	OldA = directionA
	OldB = directionB
	
	
	if (speed_percent < Old_speed):
		Speedup = 1
	else: 	
		Speedup = -1 # wheel slow down
		
	
	# wheel squence [0001]	
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
	
    #slow down  from 100%-0% in half a turn
	if (speed_percent > Old_speed):
		Speedup = -1
		ramp = (Old_speed - speed_percent)   #100-25 = 75 change speed in 4096/2 steps
		current_speed = Old_speed
		while Wheel <= wheel_turns and current_speed > speed_percent: #tagret speed
		    speed_value = (((100-speed_percent)*speedrange/100)+bottom_value)/10000
			turn_wheel(0.005)  #speed_value
			current_speed -=1
		Wheel +=1
	
	#speed up
	else: 	
		Speedup = -1 # wheel slow down	
	
	

	
	
	#constant speed

	
	
		
def turn_wheel(Delay_):
	StepCounter = 0	
	for pin in range(0, 4):
		xpinB = Set_motorB_pins[pin]
		if Seq_MPB[StepCounter][pin]!=0:
			print " BStep %i Enable %i" %(StepCounter,pin)
			GPIO.output(xpinB, True)
				  
		else:
			GPIO.output(xpinB, False)
			xpinA = Set_motorA_pins[pin]
			
		if Seq_MPA[StepCounter][pin]!=0:
			print " AStep %i Enable %i" %(StepCounter,pin)
			GPIO.output(xpinA, True)
		else:
			pass  
			GPIO.output(xpinA, False)
				
		StepCounter += 1
				
		time.sleep(Delay_)
		
		
	
	
	
	
	
	


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
# motor_block (A,B, turns, speed)
#motor_block(1,1,2,0.0009)
#motor_block(-1,-1,3,0.0009)
motor_block(1,1,2,100)
#motor_block(1,1,2,0.10)
#motor_block(1,-1,5,0.0009)
#motor_block(-1,1,5,0.0009)

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

    
