import time

counter=0
running = True
def thr_fun():
    global counter
    while running:
        counter+=1
        time.sleep(1)
