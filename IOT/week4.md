In Computer system architecture,
* Set of buu\sses in different data rates (to make it efficient)
    1. AGP - display
* These busses are divided into 3 sections calling, high speed,medium speed, and low speed busses
* High speed -> display,..
* Medium speed -> Network card,...
* Low speed -> keyboard, mouse,...
* Byte addressable -> send 8 bytes for each and everything (even one bit is used from them)

In IoT,
* Volume is small
* Have to work with rough envirnment (Computers are in a soft envirnment(resistance in noise signals))
* IoT devices always work with noise (not shielded)
* Need to be fast (So use simple architecture)
* SRAM - fast, but small
* Supervisory circuit -> fail detection (seperate independent circuit to see whats going on the bus, identify glitches and fix them,  identify infinite loops)
    simply, monitor everything in the system and detect failures and fix them/restart the system
* Power management -> slow down the clock to save power , sometimes freeze the clock (Nothing change in the logic, like slow motion, pause btns)
* Consumes power in micro watts (remote controller, sleep mode in mobile,...)
* bit addressable -> Sending bits to optimize the power, memory

* SOC = System on Chip
* Microcontroller -> SOC
* Micro Computer -> System in a single component (inlcuding input output subsystem)

# Microcontrollers
## PIC (Perpharal Interface Controller)
* 33 pre configured IO pins (so we can directly connect an IO and control it , otherwise we have to configure ports,.... to control IO in main stream chip)
* Everytime we connect an external component to a system, it gives a space of vulnerability of failures, but if we have them in built-in no need to worry about it

## Intel 8051
* first one is 8086 (main stream one)
* Scale down, but same with its main stream processor architecture
* medical equipment, NASA space operations

## AVR
* Arduino also based on them
* Main bussiness is microcontrollers

## ARM
* In high end market (mobiles, camera, rasberypi, ...)

# Microcontroller as a SOC
## Parallax Basic Stamp
* rechargable battery
* BASIC programming language built-in
* more like system on a module

## AVR
* USART -> handle multiple protocols
* Timer/Counter -> Detect time intervals in events
* Watchdog timer -> Monitor failures
    ex - timer have 10 sec timeout
        if our task doesn't work and doesn't reset the timer, the timer sends a ginal to restart the processor  
        otherwise we can work without a problem (avoiding infinite loops)

* JTAG Interface -> To run diagnosis (to read hardware signals while it is running)

## Esp (Silicon free manufactures)
* They do the design and sell it to manufactures :)
* built-in wifi -> cheap method to use
1. Esp8266
2. Esp32 -> cryptography -> built in hardware without running as a software with consuming more power to processor

# Software on a Thing
## Data driven
* load data to memory -> process

## IO driven
* sometimes data might not even come to the memory
* decision takes at the moment of the input comes

# Software vs Hardware implementation
* Filtering sugnals -> in hardware/software
* interface -> sense are converted into signals
* Based on the constraints we have to decide which part should be in hardware and software

