# AVRunner
AVRunner allows to use VSCode as an *AVR microcontroller* development environment. Say goodbye to the frustration of clunky, outdated IDEs. 

AVRunner goal is to make microcontroller coding a more enjoyable and efficient experience.

## Installation
You will need to install the following tools to make **AVRunner** work, I recommend to create a directory in `C:\Program Files (x86)\AVR` to store all the files:
- [AVR toolchain][microchip_studio_toolchain] *(To compile c code for AVR devices)*
- [avrdude][avrdude] *(To flash AVR mcu's)*
- [GnuWin32][GnuWin32] *(To support Make)*

At the end you should have something like this:
![tools][tools_image]

Now you have to make tools available to the windows console, we will add the three tools gradually as follows:
1. Go to `C:\Program Files (x86)\AVR\avr8-gnu-toolchain-win32_x86_64\bin`, copy the path and paste it in the windows path system variable.
2. Go to `C:\Program Files (x86)\AVR\avrdude`, copy the path and paste it in the windows path system variable.
3. Go to `C:\Program Files (x86)\AVR\GnuWin32\bin`, copy the path and paste it in the windows path system variable.

Open a new terminal and execute the following commands and you should get a very similar answer: 
- Verify the correct installation of avr-gcc 
```
avr-gcc --version
```
![avr_gcc][avr_gcc_image] 
- Verify the correct installation of avrdude 
```
avrdude --version
```
![avrdude][avrdude_image]
- Verify the correct installation of make
```
make --version
```
![make][make_image]

Once you have all the tools installed, simply download the avrunner folder in this repo and put it inside the `C:\Program Files (x86)\AVR` directory, copy the path `C:\Program Files (x86)\AVR\avrunner` and add it to the windows path system variable just as the previous programs and you will be ready.

## Usage
Create a directory with your projects name, open a terminal in that folder and run the following command: 
```
avrunner -c
```
This will create a MakeFile, a base c project and a task file to automate make commands. The MakeFile has a default configuration to operate with an atmega328p and an usbtiny programmer, but you can modify it very easily through global variables.

![avrunner_output][avrunner_output_image]

Finally inside your project you can press `ctrl+shift+b` and the next options will pop up to compile, flash and do many other things with your microcontroller in a beautiful environment!

![tasks][tasks_image]

The options when calling `avrunner` are the following:
```
The following arguments are available:
                  
  -c     : Creates a C file with the same name as the folder.
  --mmcu : Specify the microcontroller to be used.
  -f     : Specify the mcu frequency and can be used as F_CPU in your code.
  -b     : Specify the baudrate value and can be used as BAUD in your code.
  -B     : Specify the bitclock value when using some programmers such as usbtiny (it specifies upload speed in us).
  -P     : Specify the programmer to be used.
  --help : Displays this help message.
```

[microchip_studio_toolchain]: https://www.microchip.com/en-us/tools-resources/develop/microchip-studio/gcc-compilers
[avrdude]: https://github.com/avrdudes/avrdude/releases
[GnuWin32]: https://gnuwin32.sourceforge.net/packages/make.htm
[tools_image]: resources/tools.png
[avr_gcc_image]: resources/avr-gcc.png
[avrdude_image]: resources/avrdude.png
[make_image]: resources/make.png
[avrunner_output_image]: resources/avrunner_output.png
[tasks_image]: resources/tasks.png