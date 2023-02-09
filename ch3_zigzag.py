import time,sys
indent = 0 #number of spaces to indent
is_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('*' * 8)
        time.sleep(0.1)
        
        if is_increasing:
            indent += 1
            if indent == 20:
                is_increasing = False
        
        else:
            indent -= 1
            if indent == 0:
                is_increasing = True 
except KeyboardInterrupt:
    sys.exit()