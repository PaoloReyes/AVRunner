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
1. Go to *"C:\Program Files (x86)\AVR\avr8-gnu-toolchain-win32_x86_64\bin"*, copy the path and paste it in the windows path system variable.
2. Go to *"C:\Program Files (x86)\AVR\avrdude"*, copy the path and paste it in the windows path system variable.
3. Go to *"C:\Program Files (x86)\AVR\GnuWin32\bin"*, copy the path and paste it in the windows path system variable.

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

Once you have all the tools installed, simply download the avrunner folder in this repo and put it inside the `C:\Program Files (x86)\AVR` directory, copy the path *"C:\Program Files (x86)\AVR\avrunner"* and add it to the windows path system variable just as the previous programs and you will be ready.

## Usage
Create a directory with your projects name, open a terminal in that folder and run the following command: 
```
avrunner -c
```
This will create the MakeFile with a default configuration to operate with an atmega328p and an usbtiny programmer, but you can modify it very easily.

<video controls autoplay loop>
  <source src="resources/avrunner.mp4" type="video/mp4">
</video>

[microchip_studio_toolchain]: https://www.microchip.com/en-us/tools-resources/develop/microchip-studio/gcc-compilers
[avrdude]: https://github.com/avrdudes/avrdude/releases
[GnuWin32]: https://gnuwin32.sourceforge.net/packages/make.htm
[tools_image]: resources/tools.png
[avr_gcc_image]: resources/avr-gcc.png
[avrdude_image]: resources/avrdude.png
[make_image]: resources/make.png
