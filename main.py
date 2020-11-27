from turing import TuringMachine

def run_src(src_file, input_vector, debug=True):
    print("="*39)
    print("File: " + src_file)
    print("="*39)
    try:
        program_file = open(src_file).read()
        if debug:
            print(program_file)
            print("="*39)
            print("Input: ", input_vector)
            print("-"*39)
        tm = TuringMachine(program_file, input_vector)
        tm.run()
    except Exception as e:
        print("Error: ",e)
    print()
    print() 


# ----------------

program = 'programs_turing/program_add.txt'
input = '1101_101' # return: 10010 H
run_src(program, input)

input = '1100_001' # return: 1101 H
run_src(program, input)

input = '111_1000' # return: 1111 H
run_src(program, input)

