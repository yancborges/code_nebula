import dbMethods
import methods
import time
import timeit

def get_results():
    print("nothing")
    print("")
    print("")
    print_process(0)

def update_process():
    if(methods.time_remeaning() == 0):
        print("]Completo!")
        get_results()
    else:
        print("*", end="", flush=True)
        time.sleep(360)

def print_process(elapsed):
    print("   Ultima busca[          ]Proxima busca")
    print("                ", end="", flush=True)
    update_process()

def open_terminal():
    print("Abrindo terminal...")
    print("")
    print("")
    rem_time = methods.time_remeaning()
    print_process(int(rem_time/6))
        
        
        
    
