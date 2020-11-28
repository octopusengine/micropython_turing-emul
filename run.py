#  running TM from source programs_turing/program_xxx.txt

from turing import TuringMachine, run_src



"""
# ---------------- invers
program = 'programs_turing/program_inv.txt'
input = '11100101' # return: 00011010 H
run_src(program, input)

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

input = '110011' return: 1 H (palindrom)
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

program = 'programs_turing/program_inv.txt'
input = '11100101' # return: 00011010 H
run_src(program, input)

"""
program = 'programs_turing/program_u2b.txt'
input = '111111111' # return: 1001 H (9)
run_src(program, input)

program = 'programs_turing/program_b2u.txt'
input = '1001' # return: 111111111 H (9)
run_src(program, input)
"""



