import time
import board
import usb_hid
import digitalio
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

##### LED

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

##### MuteButton

button1 = digitalio.DigitalInOut(board.GP14)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

##### TsConnect

button2 = digitalio.DigitalInOut(board.GP16)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

##### RandomKey3

button3 = digitalio.DigitalInOut(board.GP17)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

##### RandomKey4

button4 = digitalio.DigitalInOut(board.GP18)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP
 
##### RandomKey5
 
button5 = digitalio.DigitalInOut(board.GP19)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

##### RandomKey6

button6 = digitalio.DigitalInOut(board.GP20)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP


# KeyboardSetup

keyboard = Keyboard(usb_hid.devices)

# LCD Setup
lcd = LCD(I2CPCF8574Interface(busio.I2C(board.GP1, board.GP0), 0x27), num_rows=2, num_cols=16)

# States
button1_state = False
button2_state = False
button3_state = False
button4_state = False
button5_state = False
button6_state = False
led.value = False
mute_state = False

while True:
    # MuteButton
    if button1.value == False and not button1_state:
        button1_state = True
        if mute_state:
            keyboard.press(Keycode.F7, Keycode.F9)
            time.sleep(0.1)
            keyboard.release(Keycode.F7, Keycode.F9)
            led.value = False
            lcd.clear()
            lcd.print("Du bist unmuted")
            time.sleep(0.5)
            mute_state = False
        else:
            keyboard.press(Keycode.F7, Keycode.F9)
            time.sleep(0.1)
            keyboard.release(Keycode.F7, Keycode.F9)
            led.value = True
            lcd.clear()
            lcd.print("Du bist gemuted")
            time.sleep(0.5)
            mute_state = True
    elif button1.value and button1_state:
        button1_state = False

    # TsConnect Button
    if button2.value and not button2_state:
        button2_state = True
        print("Button 2 gedrückt")
        keyboard.press(Keycode.GUI, Keycode.SPACE)
        time.sleep(0.1)
        keyboard.release(Keycode.GUI, Keycode.SPACE)
        keyboard.press(Keycode.T)
        keyboard.press(Keycode.E)
        keyboard.press(Keycode.A)
        keyboard.press(Keycode.M)
        time.sleep(0.5)
        keyboard.release(Keycode.T, Keycode.E, Keycode.A, Keycode.M)
        keyboard.press(Keycode.ENTER)
        keyboard.release(Keycode.ENTER)
        time.sleep(1)
        keyboard.press(Keycode.F12)
        keyboard.release(Keycode.F12)
    elif not button2.value and button2_state:
        button2_state = False
        
    #RandomButton3
    if button3.value and not button3_state:
        button3_state = True
        print("Test3")
    elif not button3.value and button3_state:
        button3_state = False
        
    #RandomButton4
    if button4.value and not button4_state:
        button4_state = True
        print("Test4")
    elif not button4.value and button4_state:
        button4_state = False
        
    #RandomButton5
    if button5.value and not button5_state:
        button5_state = True
        print("Test5")
    elif not button5.value and button4_state:
        button5_state = False
        
    #RandomButton6
    if button6.value and not button6_state:
        button6_state = True
        print("Test6")
    elif not button6.value and button6_state:
        button6_state = False
        
        
