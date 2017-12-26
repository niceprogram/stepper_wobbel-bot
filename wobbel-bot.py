j = None
motorA_pins = None
motorB_pins = None
pin = None
Stepcounter = None
Delay_ = None
i = None
stepper_code8 = None
stepper_off = None
stepper_code4 = None

# this function moves motorA_forward
def motorA_forward():
  global j
  for j in []:
    pass

# this function moves motorA_backwards
def motorA_backwards():
  pass

# Describe this function...
def motorB_forward():
  pass

# Describe this function...
def motorB_backwards():
  pass


# Import libraries
print(str('import time') + str('import RPi.GPIO as GPIO'))
# GPIO reference
print(str('GPIO.setmode(GGPIO.setmode(GPIO.BCM)'))
print('import time')
# Define the GPIO pins
motorA_pins[0] = '6,13,19,26'
motorB_pins[0] = '12,16,20,21'
#   print "Setup pins"
#   GPIO.setup(pin,GPIO.OUT)
#   GPIO.output(pin, False)
for pin in motorA_pins:
  print(pin)
#   print "Setup pins"
#   GPIO.setup(pin,GPIO.OUT)
#   GPIO.output(pin, False)
for pin in motorB_pins:
  print(pin)
# Define variables
Stepcounter = 0
Delay_ = 0.01
i = 1
# stepper_code8 sequence
stepper_code8[int(i + 1 - 1)] = '1,0,0,0'
stepper_code8[int(i + 1 - 1)] = '1,1,0,0'
stepper_code8[int(i + 1 - 1)] = '0,1,0,0'
stepper_code8[int(i + 1 - 1)] = '0,1,1,0'
stepper_code8[int(i + 1 - 1)] = '0,0,1,0'
stepper_code8[int(i + 1 - 1)] = '0,0,1,1'
stepper_code8[int(i + 1 - 1)] = '0,0,0,1'
stepper_off[0] = '0,0,0,0'
i = 1
# stepper_code4 sequence
stepper_code4[int(i + 1 - 1)] = '1,0,0,0'
stepper_code4[int(i + 1 - 1)] = '0,1,0,0'
stepper_code4[int(i + 1 - 1)] = '0,0,1,0'
stepper_code4[int(i + 1 - 1)] = '0,0,0,1'

'import RPi.GPIO as GPIO'
