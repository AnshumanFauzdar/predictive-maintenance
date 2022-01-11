# https://stackoverflow.com/questions/1606795/catching-stdout-in-realtime-from-subprocess
import subprocess
import re

def use_regex(input):
    pattern = re.compile(r"[+-]?([0-9]*[.])?[0-9]+")
    return pattern.search(input, re.IGNORECASE)

cmd=['hostname']
proc = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = proc.stdout

def shell_data():
    for line in stdout:
        print(">>> " + str(line.rstrip()))
        stdout.flush()
        return line

def shell_data_findbystring(word: str):
    for line in stdout:
        #print(str(line))
        string = str(line.rstrip().decode())
        #print(string)
        if word in string:
            num = float(use_regex(string).group(0))
            stdout.flush()
            return num

if __name__ == "__main__":
    # run python .\shell_read.py
    #while(True):
    num = shell_data_findbystring("none = ")
    print(num)
