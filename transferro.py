from time import sleep

def transferro():
    try:
        import server,client
    except:
        print('Dependencies not found')
        print('server.py & client.py should be in same directory as transferro.py')
        sleep(2)
        exit()
    
    choice = input('Welcome to Transferro\nYou are\n1 Sender\n2 Receiver\n')
    if choice == '1':
        server.main()
    else:
        client.main()

def main():
    try:
        transferro()
    except KeyboardInterrupt:
        print('Operation Aborted')

if __name__ == '__main__':
    main()
        
