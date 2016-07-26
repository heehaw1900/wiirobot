import cwiid
import time
import RPi.GPIO as io
import cgi,os,cgitb,sys
cgitb.enable()
sys.path.insert(0, "/usr/bin/espeak")

io.setmode(io.BCM)
#Motor 1 is designed to be the motors on the left, Motor 2 is designed to be on the right
#If one motor is in the wrong direction you can swap the pins around to save you having to re-wrire the robot.
m1a = 17 #Motor 1 Forwards
m1b = 18 #Motor 1 Backwards
m2a = 22 #Motor 2 Forwards
m2b = 23 #Motor 2 Backwards
pins = (m1a,m1b,m2a,m2b)
for i in pins:
  io.setup(i,io.OUT)

for i in pins:
  io.output(i,False)

button_delay = 0.1

os.system('sudo espeak "Press 1 and  2 on your Wii Remote now"')
time.sleep(1)

# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  os.system('sudo espeak  "Cannot connect to Wiimote"')
  quit()


wii.rumble = 1
time.sleep(2)
wii.rumble = 0


os.system('sudo espak "Wiimote connected"')
wii.rpt_mode = cwiid.RPT_BTN


os.system('sudo espeak "Press Up or A to go Forward, Press Down or B to go Backward, Left and Right, home says instructions"')

while True:
  buttons = wii.state['buttons']

  if (buttons & cwiid.BTN_UP):
    time.sleep(button_delay)
    io.output(m1a, True)
    io.output(m2a, True)

  elif (buttons & cwiid.BTN_DOWN):
    time.sleep(button_delay)
    io.output(m1b, True)
    io.output(m2b, True)

  elif (buttons & cwiid.BTN_LEFT):
    time.sleep(button_delay)
    io.output(m1a, True)
    io.output(m2b, True)

  elif(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)
    io.output(m1b, True)
    io.output(m2a, True)

  elif (buttons & cwiid.BTN_A):
    time.sleep(button_delay)
    io.output(m1a, True)
    io.output(m2a, True)

  elif (buttons & cwiid.BTN_B):
    time.sleep(button_delay)
    io.output(m1b, True)
    io.output(m2b, True)

  elif (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    os.system('sudo espeak "Closing connection"')
    wii.rumble = 1
    time.sleep(2)
    wii.rumble = 0
    os.system('sudo espeak "Connection terminated"')
    exit(wii)

  elif (buttons & cwiid.BTN_HOME):
    os.system('sudo espeak "Press Up or A to go Forward, Press Down or B to go Backward, Left and Right, home says instructions"')
    time.sleep(button_delay)
  else:
    io.output(m1a, False)
    io.output(m1b, False)
    io.output(m2a, False)
    io.output(m2b, False)


