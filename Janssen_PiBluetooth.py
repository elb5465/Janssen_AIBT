
from bluedot import BlueDot
from signal import pause
from time import sleep
from gpiozero import LED, PWMLED

led_list = [14, 15, 24, 18, 25, 23]   # GPIO numbers for the LEDs
led1   = PWMLED(led_list[0])
led2   = PWMLED(led_list[1])
led2_2 = PWMLED(led_list[2])
led3   = PWMLED(led_list[3])
led3_2 = PWMLED(led_list[4])
led4   = PWMLED(led_list[5])
# ------------------------ HANDLE EACH INPUT CASE ------------------------
def turn_OFF_allLEDs():
    global led1
    global led2
    global led2_2
    global led3
    global led3_2
    global led4
    led1.off()
    led2.off()
    led2_2.off()
    led3.off()
    led3_2.off()
    led4.off()

# ------------------------ HANDLE EACH INPUT CASE ------------------------
def turn_ON_allLEDs():
    global led1
    global led2
    global led2_2
    global led3
    global led3_2
    global led4
    led1.pulse()
    led2.pulse()
    led2_2.pulse()
    led3.pulse()
    led3_2.pulse()
    led4.pulse()

# ------------------------ CHECK FOR VALID INPUT ------------------------
# return True only if input in valid range for the left button, home button, or right bu                         tton...
def is_inputValid(bx, by):
    global led1
    global led2
    global led2_2
    global led3
    global led3_2
    global led4

    if  (by < 0.45):                           
        # ========================== CHECK IF X IN RANGE BEFORE DOING ANYTHING ========================
        if (bd_x_pos < -0.79):
            print("Back", bd_x_pos)

        elif (bd_x_pos < 0.15) and (-0.15 < bd_x_pos):
            print("Home: ", bd_x_pos)
        

        elif (bd_x_pos > 0.79):
            print("Next: ", bd_x_pos)

        else:
            # just loop to wait for next input if not within one of the previously specified                          ranges.
            print("User input not in range.")
            return False
        # =============================================================================================

        turn_OFF_allLEDs()

        xc = bx
        print(" IV VALUE FOR IF STATEMENTS: \n   ", xc, "     \n")

        if (xc < 0):
            xc = xc*(-1)
            print("\t neg to pos: \n   ", xc, "     \n")

        if (xc < 0.85):
            print("step 1")

        elif (xc == 0.85):
            print("step 5:   Turn on OLED 1")
            led1.pulse()

        elif (xc == 0.852):
            print("step 5_2: Turn on OLED 2 and 2_2")
            led2.pulse()
            led2_2.pulse()

        elif (xc == 0.86):
            print("step 6:   Turn on OLED 3")
            led3.pulse()

        elif (xc == 0.87):
            print("step 7:   Turn on OLED 3_2")
            led3_2.pulse()
        
        elif (xc == 0.88):
            print("step 8:   Turn on OLED 4")
            led4.pulse()

        elif (xc == 0.89) or (xc == 0.90):
            print("step 9/10: Turn off all")
            turn_OFF_allLEDs()

        elif (xc == 0.91):
            print("step 11: Pulse all")
            turn_ON_allLEDs()

        else:
            turn_OFF_allLEDs()


    else:
        print("top: ", bx, by)
        print("INPUT TOO HIGH: ", bx, by)

    return True

# ------------------------ START MAIN PART OF FUNCTION ------------------------
bd = BlueDot()
bd.allow_pairing(None) #set to None makes indefinitely pairable, otherwise set to 60 (60                          seconds) or another int
bd.square = True
bd.visible = False

while True:
        # RESET ALL OF THE PROGRAM VARIABLES AND STUFF WHEN CONNECTION LOST OR USER LEAV                         ES APP
        while bd.is_connected == False:
            pass

        while bd.is_connected:
            # -------------- CHECK IF PRESS WAS ON THE BUTTONS - NOT IN BETWEEN THEM ---                         -------------
            # if prev input was not in range, loop here until there is new input to chec                         k
            check_inp_flag = False

            # if some touch input on the screen occurs...
            bd.wait_for_press()
            print("\n--------------------- PRESSED SCREEN --------------------------")

            # save the input as an "Interaction Object"...
            bdi = bd.interaction

            # wait for user to take their finger off screen...
            while bdi.released_position == None:
                    pass

            # record the coordinates of where they released their finger...
            bd_x_pos = bdi.released_position.x
            bd_y_pos = bdi.released_position.y

            # check for valid input and do corresponding action if so..
            is_inputValid(bd_x_pos, bd_y_pos)
         



