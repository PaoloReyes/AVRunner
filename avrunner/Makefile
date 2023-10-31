##########------------------------------------------------------##########
##########              Project-specific Details                ##########
##########    Check these every time you start a new project    ##########
##########------------------------------------------------------##########

MCU   = atmega328p
F_CPU = 16000000UL
BAUD  = 9600UL
## Also try BAUD = 19200 or 38400 if you're feeling lucky.

## A directory for common include files.
LIBDIR = ../../AVR-Programming-Library

##########------------------------------------------------------##########
##########                 Programmer Defaults                  ##########
##########          Set up once, then forget about it           ##########
##########        (Can override.  See bottom of file.)          ##########
##########------------------------------------------------------##########

PROGRAMMER_TYPE = usbtiny
## extra arguments to avrdude: baud rate, chip type, -F flag, etc.
PROGRAMMER_ARGS = -B 115200

##########------------------------------------------------------##########
##########                  Program Locations                   ##########
##########     Won't need to change if they're in your PATH     ##########
##########------------------------------------------------------##########

CC = avr-gcc
OBJCOPY = avr-objcopy
OBJDUMP = avr-objdump
AVRSIZE = avr-size
AVRDUDE = avrdude

##########------------------------------------------------------##########
##########                   Makefile Magic!                    ##########
##########         Summary:                                     ##########
##########             We want a .hex file                      ##########
##########        Compile source files into .elf                ##########
##########        Convert .elf file into .hex                   ##########
##########        You shouldn't need to edit below.             ##########
##########------------------------------------------------------##########

## The name of your project (without the .c)
## Or name it automatically after the enclosing directory
TARGET = $(lastword $(subst /, ,$(CURDIR)))

## Object files: will find all .c/.h files in current directory
## and in LIBDIR.  If you have any other (sub-)directories with code,
## you can add them in to SOURCES below in the wildcard statement.
SOURCES = $(wildcard *.c $(LIBDIR)/*.c)
OBJECTS = $(SOURCES:.c=.o)
HEADERS = $(SOURCES:.c=.h)

## Compilation options, defines macros for F_CPU and BAUD, includes libraries, optimize for size, enable all warnings and use c99 standard.
CPPFLAGS = -DF_CPU=$(F_CPU) -DBAUD=$(BAUD) -I. -I$(LIBDIR)
CFLAGS = -Os -std=gnu99 -Wall
## Use short (8-bit) data types 
CFLAGS += -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums 
## Splits up object files per function
CFLAGS += -ffunction-sections -fdata-sections 
## Instructsthe linker to create a .map file to show memory organization
LDFLAGS = -Wl,-Map,$(TARGET).map 
## Instructs the linker to analyze and remove unused or unreferenced code
LDFLAGS += -Wl,--gc-sections
## Relax shrinks code even more, but makes disassembly messy
## LDFLAGS += -Wl,--relax
## Target architecture depending on specific mcu
TARGET_ARCH = -mmcu=$(MCU)

## Explicit pattern rules:
## To make .o files from .c files 
%.o: %.c $(HEADERS) Makefile
	 $(CC) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c -o $@ $<;

## To make .elf files from .o files 
$(TARGET).elf: $(OBJECTS)
	$(CC) $(LDFLAGS) $(TARGET_ARCH) $^ -o $@

## To make .hex files from .elf files
%.hex: %.elf
	 $(OBJCOPY) -j .text -j .data -O ihex $< $@

## To make .hex files from .elf files for eeprom
%.eeprom: %.elf
	$(OBJCOPY) -j .eeprom --change-section-lma .eeprom=0 -O ihex $< $@ 

## To dissasambly .elf files
%.lst: %.elf
	$(OBJDUMP) -S $< > $@

## These targets don't have files named after them
.PHONY: all compile flash show_fuses write_fuses clean squeaky_clean size verify_config disassemble flash_eeprom flash_usbtiny flash_arduinoISP flash_arduino

## Make Hex file
all: compile
all: flash

compile: $(TARGET).hex

## See avr configuration
verify_config:
	@echo
	@echo "Source files:"   $(SOURCES)
	@echo "MCU, F_CPU, BAUD:"  $(MCU), $(F_CPU), $(BAUD)
	@echo	

## Optionally create listing file from .elf
## This creates approximate assembly-language equivalent of your code.
## Useful for debugging time-sensitive bits, 
## or making sure the compiler does what you want.
disassemble: $(TARGET).lst

## Optionally show how big the resulting program is 
size:  $(TARGET).elf
	$(AVRSIZE) -C --mcu=$(MCU) $(TARGET).elf

## Clean only folder name related files
clean:
	rm -f $(TARGET).elf $(TARGET).hex $(TARGET).obj \
	$(TARGET).o $(TARGET).d $(TARGET).eep $(TARGET).lst \
	$(TARGET).lss $(TARGET).sym $(TARGET).map $(TARGET)~ \
	$(TARGET).eeprom

## Clean all compiled files
squeaky_clean:
	rm -f *.elf *.hex *.obj *.o *.d *.eep *.lst *.lss *.sym *.map *~ *.eeprom

##########------------------------------------------------------##########
##########              Programmer-specific details             ##########
##########           Flashing code to AVR using avrdude         ##########
##########------------------------------------------------------##########

## Flash the AVR with global settings
flash: $(TARGET).hex 
	$(AVRDUDE) -c $(PROGRAMMER_TYPE) -p $(MCU) $(PROGRAMMER_ARGS) -U flash:w:$<

## Flash the eeprom with global settings
flash_eeprom: $(TARGET).eeprom
	$(AVRDUDE) -c $(PROGRAMMER_TYPE) -p $(MCU) $(PROGRAMMER_ARGS) -U eeprom:w:$<

## If you've got multiple programmers that you use, 
## you can define them here so that it's easy to switch.
## To invoke, use something like `make <programmer_type>`
flash_usbtiny: PROGRAMMER_TYPE = usbtiny
flash_usbtiny: PROGRAMMER_ARGS =  -B 115200
flash_usbtiny: flash

flash_arduinoISP: PROGRAMMER_TYPE = avrisp
flash_arduinoISP: PROGRAMMER_ARGS = -b 19200 -P COM5
flash_arduinoISP: flash

flash_arduino: PROGRAMMER_TYPE = arduino
flash_arduino: PROGRAMMER_ARGS = -b 19200 -P COM5
flash_arduino: flash

##########------------------------------------------------------##########
##########       Fuse settings and suitable defaults            ##########
##########------------------------------------------------------##########

## Default fuses from avrdudess
LFUSE = 0xE7
HFUSE = 0xDE
EFUSE = 0xFD

## Generic 
FUSE_STRING = -U lfuse:w:$(LFUSE):m -U hfuse:w:$(HFUSE):m -U efuse:w:$(EFUSE):m 

write_fuses: 
	$(AVRDUDE) -c $(PROGRAMMER_TYPE) -p $(MCU) \
	           $(PROGRAMMER_ARGS) $(FUSE_STRING)
show_fuses:
	$(AVRDUDE) -c $(PROGRAMMER_TYPE) -p $(MCU) $(PROGRAMMER_ARGS) -nvs