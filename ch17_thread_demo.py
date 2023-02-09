import threading, time
print('START')

def take_a_nap():
    time.sleep(5)
    print('WAKE UP!')
    
thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('END')