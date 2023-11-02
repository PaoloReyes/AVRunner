import shutil, os, sys, datetime

MCU_LIST_URL = "https://github.com/PaoloReyes/AVRunner/blob/main/avrunner/mcu_list.txt"
PROGRAMMER_LIST_URL = "https://github.com/PaoloReyes/AVRunner/blob/main/avrunner/programmer_list.txt"

def create_utilities(mmcu = None, f_cpu = None, baud = None, bitclock = None, programmer = None) -> None:
    with open(r'C:\Program Files (x86)\AVR\avrunner\Makefile', 'r') as makefile:
        makefile_base_data = makefile.readlines()

    for line_id, line in enumerate(makefile_base_data):
        if line[0:3] == 'MCU':
            if mmcu != None: makefile_base_data[line_id] = f'MCU   = {mmcu}\n'
        elif line[0:5] == 'F_CPU':
            if f_cpu != None: makefile_base_data[line_id] = f'F_CPU = {f_cpu}\n'
        elif line[0:4] == 'BAUD':
            if baud != None: makefile_base_data[line_id] = f'BAUD  = {baud}\n'
        elif line[0:15] == 'PROGRAMMER_ARGS':
            if bitclock != None: makefile_base_data[line_id] = makefile_base_data[line_id][:-1]+f' -B {bitclock}\n'
        elif line[0:15] == 'PROGRAMMER_TYPE':
            if programmer != None: makefile_base_data[line_id] = f'PROGRAMMER_TYPE = {programmer}\n'

    with open(f'{path}\\Makefile', 'w') as makefile:
        makefile.writelines(makefile_base_data)

    if not os.path.exists(f'{path}\\.vscode'):
        os.mkdir(f'{path}\\.vscode')
    shutil.copyfile(r'C:\Program Files (x86)\AVR\avrunner\tasks.json', f'{path}\\.vscode\\tasks.json')

def is_valid_param(param: str, data_file) -> None:
    with open(data_file, 'r') as raw_data:
        data_list = raw_data.readlines()
    data_list = [data_line[:-1].lower() for data_line in data_list]
    if param not in data_list:
        print(f'Invalid argument: {mmcu}, please input a valid argument from this list: {MCU_LIST_URL}')
        sys.exit(1)
    return 1

def is_positive_integer(value, arg):
    if not (value.isnumeric() and int(value) > 0):
        print(f'Invalid argument {arg}: {value}, please input a numeric value greater than 0')
        sys.exit(1)
    return 1

def read_arg(i, arg):
    if argc == i:
        print(f'You did not provide a value for argument {arg}, please provide one')
        sys.exit(1)
    return sys.argv[i].lower()

path = os.getcwd()
folder_name = path.split('\\')[-1].lower()

argc = len(sys.argv)

if argc == 1:
    create_utilities()
    print('Default AVR project created successfully!!!')
elif argc > 1:
    todo_file = None
    mmcu = None
    f_cpu = None
    baud = None
    bitclock = None
    programmer = None

    i = 1
    while i < argc:
        argument = sys.argv[i]
        if argument == '-c':
            todo_file = f'{folder_name}.c'
        elif argument[0:6] == '--mmcu':
            mmcu = read_arg(i+1, argument)
            i += is_valid_param(mmcu, r'C:\Program Files (x86)\AVR\avrunner\mcu_list.txt')
        elif argument == '-f':
            f_cpu = read_arg(i+1, argument)
            i += is_positive_integer(f_cpu, argument)
            f_cpu+='UL'
        elif argument == '-b':
            baud = read_arg(i+1, argument)
            i += is_positive_integer(baud, argument)
            baud+='UL'
        elif argument == '-B':
            bitclock = read_arg(i+1, argument)
            i += is_positive_integer(bitclock, argument)
        elif argument == '-P':
            programmer = read_arg(i+1, argument)
            i += is_valid_param(programmer, r'C:\Program Files (x86)\AVR\avrunner\programmer_list.txt')
        elif argument == '--help':
            print('''
The following arguments are available:
                  
  -c     : Creates a C file with the same name as the folder.
  --mmcu : Specify the microcontroller to be used.
  -f     : Specify the mcu frequency and can be used as F_CPU in your code.
  -b     : Specify the baudrate value and can be used as BAUD in your code.
  -B     : Specify the bitclock value when using some programmers such as usbtiny (it specifies upload speed in us).
  -P     : Specify the programmer to be used.
  --help : Displays this help message.''')
            sys.exit(0)
        else:
            print(f'Invalid argument: {argument}')
            sys.exit(1)
        i+=1

    file_path = f'{path}\\{todo_file}'

    base_project_string = f"""/*
* {todo_file}
* Created: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
* Author: {os.getlogin()}
*/

#include <avr/io.h>

int main(void) {{
    /* Replace with your initialization code */
    while(1) {{
        /* Replace with your loop code */
    }}
    return 0;
}}"""

    success_message = 'AVR project created successfully!!!'
    if not os.path.exists(file_path) and todo_file != None:
        with open(file_path, 'w') as main_file:
            main_file.write(base_project_string)
            success_message = f'AVR project created and initialized in./{todo_file} successfully!!!'
    create_utilities(mmcu, f_cpu, baud, bitclock, programmer)
    print(success_message)