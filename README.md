# ESP32 micropython_turing-emul
ESP32 &amp; MicroPython - turing machine emulator

A Turing machine is a mathematical model of computation that defines an abstract machine, which manipulates symbols on a strip of tape according to a table of rules.

---

This repo contains ESP32 Micropython application based on **OctopusLAB Framework** -> [octopusengine/octopuslab](https://github.com/octopusengine/octopuslab).

This runs example, that allows you to control I/O peripherals connected to your [OctopusLAB EDU_KIT1](https://www.octopusengine.org/edu-kit1/).

## Emulator

The program is loaded as a text file (`programs_turing/program.txt`) where **each line represents a transition function of the form 𝛿(𝑝,𝑋)=(𝑞,𝑌,D)**, so the 5 tuples are strictly in the order p, X, Y, D, q *(the character _ represents a blank symbol on the tape)*

```
0 0 0 r 0
0 1 1 r 0
0 _ _ r 1
1 0 0 r 1
1 1 1 r 1
1 _ _ l 2
2 0 1 l 2
2 1 0 l 3
2 _ _ r 5
3 0 0 l 3
...
```

---

Links:

https://sandipanweb.wordpress.com/2020/08/08/simulating-a-turing-machine-with-python-and-executing-programs


