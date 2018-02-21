import platform

def main():
    printPlatform()
    printMachineName()
    printOSType()
        
def printPlatform():
    print('Platform: ' + str(platform.platform()[-5:]))
    
def printMachineName():
    print('Machine name: ' + str(platform.machine()))
    
def printOSType():
    print('Operating system: ' + str(platform.system()))

    
if __name__ == '__main__':
    main()