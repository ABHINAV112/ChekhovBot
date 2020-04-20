from subprocess import STDOUT, check_output
import subprocess
from threading import Timer
from config import BASE_PATH

# to be edited

def execute_command(option,instructions):
    if(option == "terminal"):
        process = subprocess.Popen(instructions,stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout

    if(option=="python"):
        python_file = open("Program_Files/python_run.py", "w")
        python_file.write(instructions)
        python_file.close()
        process = subprocess.Popen("python3 {}/Program_Files/python_run.py".format(BASE_PATH),stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout

    if(option=="cpp"):
        cpp_file = open("Program_Files/cpp_run.cpp", "w")
        cpp_file.write(instructions)
        cpp_file.close()
        process=subprocess.Popen("g++ -o {}/Program_Files/cpp_run {}/Program_Files/cpp_run.cpp; {}/Program_Files/cpp_run".format(BASE_PATH,BASE_PATH,BASE_PATH),stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout

    if(option=="c"):
        cpp_file = open("Program_Files/c_run.c", "w")
        cpp_file.write(instructions)
        cpp_file.close()
        process=subprocess.Popen("gcc -o {}/Program_Files/c_run {}/Program_Files/c_run.c; {}/Program_Files/c_run".format(BASE_PATH,BASE_PATH,BASE_PATH),stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout


    output = output.decode("utf-8")
    if(output==""):
        output = "Nothing was written to the stdout"

    return output


