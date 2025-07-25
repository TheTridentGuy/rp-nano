# rp-nano
## Tiny RP2040 based board, ideal for USB HID applications, i.e USB rubber ducky.

I designed this mainly for rubber ducky applications. It's extremely similar to the [picoducky](https://github.com/Outdatedcandy92/PicoDucky), but rp2040 based, and I started designing it before i knew picoducky was a thing. I created because I wanted a small, cheap (\**laughs in trump tax*\*), board that could be used for general HID tasks, or even a one LED+tactile switch microcontroller project.

### PCB Layers:
- Top - High-priority signal and 3V3 pour
- Inner1 - GND pour and USB crossover
- Inner2 - 1V1 and 5V
- Bottom - GND pour and signal

### PCB:
![](images/3d1.png)
![](images/top.png)
![](images/inner1.png)
![](images/inner2.png)
![](images/bottom.png)
### Schematic:
![](images/sch2.png)
### BOM:

| Item     | Qty | Price Each | Running Total |
|-         |-    |-           |-              |
| PCBs x10 | 1   | $139       | $139          |
### Firmware: https://circuitpython.org/board/raspberry_pi_pico/
