import cwiid
import time
import RPi.GPIO as io

io.setmode(io.BCM)

m1a = 17 
m1b = 18 
m2a = 22 
m2b = 23 
pins = (m1a,m1b,m2a,m2b)
for i in pins:
  io.setup(i,io.OUT)

for i in pins:
  io.output(i,False)

button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)


try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Can't connect to Wiimote"
  quit()


wii.rumble = 1
time.sleep(2)
wii.rumble = 0


print 'Wiimote connected'
wii.rpt_mode = cwiid.RPT_BTN


print 'Press Up or A to go Forward, Press Down or B to go Backward, Left and Right make the robot go in that direction, home will display the instructions again'

while True:
  buttons = wii.state['buttons']

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed, going forwards'
    time.sleep(button_delay)    
    io.output(m1a, True)      
    io.output(m2a, True)
    
  elif (buttons & cwiid.BTN_DOWN):
    print 'Down pressed, going backwards'   
    time.sleep(button_delay)  
    io.output(m1b, True)
    io.output(m2b, True)
  
  elif (buttons & cwiid.BTN_LEFT):
    print 'left pressed, going left'
    time.sleep(button_delay)         
    io.output(m1a, True)
    io.output(m2b, True)
   
  elif(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed, going backwards'
    time.sleep(button_delay)          
    io.output(m1b, True)
    io.output(m2a, True)
  
  elif (buttons & cwiid.BTN_A):
    print 'A pressed, going forwards'
    time.sleep(button_delay)
    io.output(m1a, True)
    io.output(m2a, True)
   
  elif (buttons & cwiid.BTN_B):
    print 'B pressed, going backwards'
    time.sleep(button_delay)
    io.output(m1b, True)
    io.output(m2b, True)
  
  elif (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print'Closing connection'   
    wii.rumble = 1
    time.sleep(2)
    wii.rumble = 0
    exit(wii)
    print'Connection terminated'
    
  elif (buttons & cwiid.BTN_HOME):
    print'Press Up or A to go Forward, Press Down or B to go Backward, Left and Right make the robot go in that direction, home will display the instructions again'
    time.sleep(button_delay)  
  else:
    io.output(m1a, False)
    io.output(m1b, False)
    io.output(m2a, False)
    io.output(m2b, False)
