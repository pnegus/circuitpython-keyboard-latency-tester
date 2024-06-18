# circuitpython-keyboard-latency-tester
code for using circuitpython esp32 to test mech keyboard latency

## Overview

`code.py` programs your esp32 to send the f key over USB followed by a high digital signal on D11. I used a 2N2222 NPN transistor with a 1kohm pull down resistor and a 1kohm resistor connected to the gate. The source/sink are hooked up to the switch pins on the keyboard. Press the debug button to start the routine, it'll run 20 iterations.

## Usage

- Load `code.py` to your circuitpython board

- Run KeyResponsePK in bump mode (download from Bloody website-- though it doesn't seem to be hosted there anymore? [mirror](https://drive.google.com/file/d/1kiUobSebUWdqPSi0QxpxsH_TUng1uGVF/view?usp=sharing))

- Press debug button

## Results (latency avg):

Keychron V1: 1.8ms

Blackwidow V4 75%: 0.8ms
