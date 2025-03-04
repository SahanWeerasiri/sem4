# PC  vs IoT Devices
* in pc -> everything comes with the Frameworks, only the logic will be ours. No need of worry about hardware. Runtime envirnment take care about everything for you. Common runtime is handled by OS, and OS is handled by BIOS.
* in IoT -> We need a software specific to the hardware. We have to have more control on hardware and software. "setup, loop" are basic runtime framework at minimal level. Hardware directly work with Device libraries. We detect only the key code(not the ascii code) when pressing a key in keyboard. 

## Cross-platform developmet
* For debugging we do cross compilations using simulation platforms, because it is difficult to debugg with lack of debugging tools.(sometimes simulator can't give the real envirnment to test)
* So we need to get some tools which are specific to the hardware manufacturer.
ex- **ICE**(in circuit emulator) - expensive
* JTAG - help to monitor (sometimes built in)  -cheap

## IoT programming languages
* derivatives of main stream programming languages. (remove unnessecary parts from the language)
* ex- Zero division errors -> IoT won't give them, since the overhead is high
* event driven programming - asyncronous event handling

***
* Traditional Compile
* Source code => compile => Processor Machine code(only work on that processor)

* Interpreter
* Source code => Interpreter => Runtime with all the libraries, even athey are not useful =>  Machine code

* JVM(Decouple the development envirnment from the runtime)
* Source code => Byte code compile=> Runtime with only nessecary parts(very thin)/byte code(run on any processor)

# Key components
### Power up 
* Cold start (Configure all and verify all the initializations and POST(Power on self test))
* hot start -> restart while the system runs

### Main loop
* Interupt routine -> we need to get out from there as fast as possible, to avoid deadlocks with facing another interupt while we are inside an interupt routine
* volatile key word -> compiler allocate memory from the fastest part

## Security Considerations
* Authentication -> need to be done in device level as well as the user level(Mallicious codes or devices can be there)

## Testing 
* Lesser paramerters -> Easy to test

## Power management
* Sleep Modes -> Deep sleep -> problem: even it freezes, we need to take care of dynamic memory wothout letting its memory to be corrupted.

## Deployment and Maintainance
* Life cycle management -> Reuse/ recycle the devices at the end of its life