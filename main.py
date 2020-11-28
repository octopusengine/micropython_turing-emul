#  running TM from source programs_turing/program_xxx.txt

from time import sleep
from uturing import TuringMachine, run_src
from components.button import Button
from components.rgb import Rgb
import colors_rgb as rgb
import pubsub
# from utils.octopus import disp7_init

from machine import Pin
button0 =  Button(Pin(0), release_value=1)

# d7 = disp7_init()  # 8 x 7segment display init
ws_num = 32
ws = Rgb(15,ws_num)
ws.simpleTest()

c1 = (32,8,0)
c0 = (0,16,0)


print()
print("Turing Machine Emulator (ESP32 - Micropython)")

def ws_clear_all(num=ws_num):
    for i in range(num):
         ws.color(rgb.BLACK,i)


def ws_show_tape(tape,ofset=5):
    # ws_clear_all()
    i = 0
    for c in tape:
         if c=="1":
            # print("=1=",end="")
            ws.color(c1,i+ofset)
         else: 
            # print("-0-",end="")
            ws.color(c0,i+ofset)
         i += 1


@button0.on_press
def on_press_button():
    print("the button_0 has been pressed -> ws_clear_all")
    ws_clear_all()


@pubsub.subscriber("tm")
def show_tape(tm):
     ws_clear_all()
     print("ps:",tm[0],tm[1],tm[3])  # test pub sub - ok 
     ws.color((16,0,0))
     sleep(0.05)
     ws.color(rgb.BLACK)
     ws_show_tape(tm[3],tm[1])
     print()


def run(program, input="101010", note="->"):
    print("--- run ---")
    print("note")
    ws_clear_all()
    ws.color((0,0,32))
    ws_show_tape(input,ofset=5) # h_start 
    sleep(1)
    ws_clear_all()
    sleep(0.3)
    # program = 'programs_turing/program_inv.txt'
    # input = '11100101' # return: 00011010 H
    run_src(program, input)
    sleep(5)


# ===================================================
"""
# ---------------- invers
ws_clear_all()
sleep(1)
program = 'programs_turing/program_inv.txt'
input = '11100101' # return: 00011010 H
run_src(program, input)
sleep(5)

# ---------------- sum x + y (xxxxx_yyyyy)
program = 'programs_turing/program_sum.txt'
input = '1101_101' # return: 10010 H
run_src(program, input)

input = '1100_001' # return: 1101 H
input = '111_1000' # return: 1111 H
run_src(program, input)

input = '1101_101' # return: 10010 H
run_src(program, input)

input = '1100_001' # return: 1101 H
input = '111_1000' # return: 1111 H

# ---------------- increment +1
program = 'programs_turing/program_inc.txt'
input = '1' # Err
run_src(program, input)

input = '10101010' # Err
run_src(program, input)

input = '1111111111' # Err
run_src(program, input)

# ---------------- palindrom
program = 'programs_turing/program_pal.txt'
input = '111000' # return: 0 H (no palindrom)
run_src(program, input)

input = '110011' # return: 1 H (palindrom)
run_src(program, input)

input = '1011001101___' # return: 1 H (palindrom)
run_src(program, input)


# ---------------- Binary to a Unary
program = 'programs_turing/program_b2u.txt'
input = '10' # return: 11 H (2)
run_src(program, input)

input = '101' # return: 11111 H (5)
run_src(program, input)

input = '1001' # return: 111111111 H (9)
run_src(program, input)

# ---------------- Unary to a Binary
program = 'programs_turing/program_u2b.txt'
input = '1' # return: 11 H (2)
run_src(program, input)

input = '11111' # return: 101 H (5)
run_src(program, input)

input = '111111111' # return: 1001 H (9)
run_src(program, input)

"""

# -------- USAGE: -------------------------

run('programs_turing/program_inv.txt','1110001010',"inversion return: 0001110101")

run('programs_turing/program_pal.txt','11100111',"palindrome return: 1")

run('programs_turing/program_sum.txt','1101_101',"suma return: x+y")

run('programs_turing/program_b2u.txt','1001',"b2u return: 111111111 (9)")

run('programs_turing/program_u2b.txt','111111111',"u2b return: 1001 (9)")







