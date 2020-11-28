# modification for EDU_KIT1 - WS led strip 32 LEDs
# using pubsub module from Octopus Framework


from time import sleep
import pubsub

N = 32   # tape length - initialize to a "large" value
h_start =  5 # N // 2  - head is positioned in the middle
delay = 0.3


 
class TuringMachine:
   # initialize the Turing Machine
   def __init__(self, program, input, state=0):
      self.trf = {}
      self.state = str(state)
      self.tape = ''.join(['_']*N)
      self.head = h_start # N // 2   # head is positioned in the middle
      self.delay = delay
      self.tape = self.tape[:self.head] + input + self.tape[self.head:]
      # read the program and input
      for line in program.splitlines():
         s, a, r, d, s1 = line.split(' ')
         self.trf[s,a] = (r, d, s1)
 
   # step through a program
   def step(self, iter):
      if self.state != 'H':
         # assert self.head >= 0 and self.head < len(self.tape) here
         a = self.tape[self.head]
         action = self.trf.get((self.state, a))
         if action:
            r, d, s1 = action
            self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
            if d != '*':
               self.head = self.head + (1 if d.upper() == 'R' else -1)
            self.state = s1
            # print("   [%3d] %3s (%s) %s" % (iter, self.head, self.state, self.tape.replace('_', '')))
            tm = iter, self.head, self.state, self.tape.replace('_', '')
            # print(tm)
            pubsub.publish('tm', tm)
            sleep(delay)
 
   # run a program
   def run(self, max_iter=999):
       iter = 0
       while self.state != 'H' and iter < max_iter: # prevent infinite loop
           self.step(iter)
           iter += 1
           sleep(self.delay)
       print("Output: ", self.tape.replace('_', ''))


       

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
            print("   [%3s] %3s (%s) %s" % ("i", "H", "s", "tape"))
            print("."*39)
        tm = TuringMachine(program_file, input_vector)
        tm.run()
    except Exception as e:
        print("Error: ",e)
    print()
    print()
    sleep(3) 
