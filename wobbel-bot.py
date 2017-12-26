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
import RPi.GPIO as GPIO

# GPIO references
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins
Set_motorA_pins = [6,13,19,26]
Set_motorB_pins= [12,16,20,21]


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
# StepCounter= 0
#Delay_ = 0.002  # for 4 sequence

Delay_ = 0.5 # for 8 sequence .0009

# this function...
def motor_block():
	StepCounter= 0
	Four_or_eight_steps=0
	while Four_or_eight_steps <= 8:
		for pinB in range(0, 4):
			xpin = Set_motorB_pins[pinB]
			if Seq[StepCounter][pinB]!=0:
			  print " Step %i Enable %i" %(StepCounter,xpin)
			  GPIO.output(xpin, True)
			else:
			  GPIO.output(xpin, False)
		StepCounter += 1
		if (StepCounter==StepCount):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = StepCount
		time.sleep(Delay_)
	Four_or_eight_steps+=1
	
	


# stepper_code8 sequence
stepper_code8= []
stepper_code8= range(0, 8)
stepper_code8[0] = [1,0,0,0]
stepper_code8[1] = [1,1,0,0]
stepper_code8[2] = [0,1,0,0]
stepper_code8[3] = [0,1,1,0]
stepper_code8[4] = [0,0,1,0]
stepper_code8[5] = [0,0,1,1]
stepper_code8[6] = [0,0,0,1]
stepper_code8[7] = [1,0,0,1]
stepper_off = [0,0,0,0]

# stepper_code4 sequence
stepper_code4= []
stepper_code4= range(0, 4)
stepper_code4[0] = [1,0,0,0]
stepper_code4[1] = [0,1,0,0]
stepper_code4[2] = [0,0,1,0]
stepper_code4[3] = [0,0,0,1]

# Choose a sequence to use
Seq = stepper_code8
#Seq.reverse()
StepCount = 8



# Start main loop
#while 1==1:

motor_block()
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
