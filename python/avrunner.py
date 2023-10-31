import shutil, os, sys, datetime

path = os.getcwd()

shutil.copyfile(r'C:\Program Files (x86)\AVR\avrunner\Makefile', f'{path}\\Makefile')
if not os.path.exists(f'{path}\\.vscode'):
    os.mkdir(f'{path}\\.vscode')
shutil.copyfile(r'C:\Program Files (x86)\AVR\avrunner\tasks.json', f'{path}\\.vscode\\tasks.json')

folder_name = path.split('\\')[-1].lower()

if len(sys.argv) == 1:
    print('AVR project created successfully!')
elif len(sys.argv) > 1:
    todo_files = []
    for arg in sys.argv[1:]:
        if arg != '-c':
            print('Invalid Flag')
            sys.exit(1)
    file_name = f'{path}\\{folder_name}.c'
    if not os.path.exists(file_name):
        with open(file_name, 'w') as init_file:
            init_file.write(f'/*\n * {folder_name}.c\n * Created: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n * Author: {os.getlogin()}\n */\n\n#include <avr/io.h>\n\nint main(void) {{\n\t/* Replace with your initialization code */\n\twhile(1) {{\n\t\t/* Replace with your loop code */\n\t}}\n\treturn 0;\n}}')
        print(f'AVR project created and initialized in./{folder_name}.c successfully!!!')