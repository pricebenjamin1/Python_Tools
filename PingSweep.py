import sys, os
for i in range(0,(int(sys.argv[3])-int(sys.argv[2])+1)):
    if "bytes=" in os.popen(f"ping -c 1 {(sys.argv[1] + str((int(sys.argv[2]) + i)))}").read():
        print(str(sys.argv[1] + str((int(sys.argv[2]) + i))))
