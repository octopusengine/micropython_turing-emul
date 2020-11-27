from turing import TuringMachine

def run_src(src_file, input_vector, debug=True):
    print("="*39)
    print("File: " + src_file)
    print("="*39)
    try:
        program_file = open('programs_turing/program.txt').read()
        if debug:
            print(program_file)
            print("="*39)
        tm = TuringMachine(program_file, input_vector)
        tm.run()
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)
    print()
    print() 


# ----------------

input = '1101_101'
program = 'programs_turing/program.txt'

run_src(program, input)
# return: 10010 H
