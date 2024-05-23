# circuitpython-keyboard-latency-tester
code for using circuitpython esp32 to test mech keyboard latency

## Overview

`code.py` programs your esp32 to-- on the press of the debug button-- send an 'f' keypress followed by setting the 'g' switch contact high. It does this 50 times.

`program.py` intercepts these inputs and simply prints the time differential between the two. This in theory should allow for comparing PCB latency between various keyboards.

## Usage

- Load `code.py` to your circuitpython board

- Run `program.py`

- Press debug button