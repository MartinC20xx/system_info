import platform

def main():
    print('Platform: ' + str(platform.platform()[-5:]))
    print('Machine name: ' + str(platform.machine()))
    print('Operating system: ' + str(platform.system()))
    
if __name__ == '__main__':
    main()