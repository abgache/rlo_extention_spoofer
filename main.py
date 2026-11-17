#!/bin/python
from colorama import init, just_fix_windows_console, Fore, Style
from os import rename, path
import argparse, sys

def rlo():
    return "\u202e"

def parse():
    parser = argparse.ArgumentParser(description="Easely hide an exe file under another extension using RLO unicode character.")
    parser.add_argument("file", help="target file path (only .exe)")
    parser.add_argument("-n", "--name", help="The new file name (e.g. THAT.pdf)", required=True)
    parser.add_argument("-e", "--extention", help="the new file extention", default="pdf")
    # Soon: parser.add_argument("-i", "--icon", help="No-mandatory, the new file icon")
    parser.add_argument("--debug", help="Debug mode", action='store_true')
    return parser.parse_args()

def main():
    args=parse()
    file=str(args.file)
    if not file.endswith(".exe"):
        file=file+".exe"
    name=str(args.name)
    extention=str(args.extention)
    # check if it starts with a dot & remove it
    if extention.startswith("."):
        extention=extention[1:]
    predicted_output=f"{name}exe.{extention}"
    print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} Spoofing {file} to {predicted_output}...")
    print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} This technique was created for educationnal and threat intelligence purposes only, the owner refuses any responsibility of any illegal usage and forbids it.")

    # check if the file indeed exists
    if not path.isfile(file):
        print(f"{Fore.RED}[-]{Style.RESET_ALL} The target file does not exists.")
        exit(1)

    # Name + rlo + inverted extention (bcs rlo inverts it) + exe (inverted or not its the same)
    new_name=f"{name}{rlo()}{extention[::-1]}.exe"
    if path.isfile(new_name):
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Target file already exists, overwriting it.")
    try:
        rename(file, new_name)
    except OSError as expt:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Failed to spoof the file. Unknown error: {type(expt).__name__}: {expt}")
        exit(2)

    # TODO: Add icon support

    if path.isfile(new_name):
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} File succesfully spoofed.")
    


if __name__ == "__main__":
    init()
    just_fix_windows_console()
    try:
        main()
    except Exception as expt:
        _, _, tb = sys.exc_info()
        while tb.tb_next is not None:    
                tb = tb.tb_next
                print(f"{Fore.RED}[-]{Style.RESET_ALL} "
                       f"{type(expt).__name__}: {expt} "
                       f"(line {tb.tb_lineno}, function {tb.tb_frame.f_code.co_name})")
        if "--debug" in sys.argv:
           raise