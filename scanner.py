import socket
from sys import exit

ip = raw_input('\nSaisir l\'ip de votre cible : ')
ports=raw_input('Saisir les ports a scanner (21,22, etc...) : ')
ports = ports.replace(' ','')

print('\n)

for port in ports.replace(' ',''):
    try:
        port = int(port)
    except:
        print('Saisie incorrecte.. ')
        exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    code = sock.connect_ex((ip, port))

    if code==0 :
        print('Port {} is open |'.format(str(port)))
    else:
        print('Port {} is closed'.format(str(port)))

    sock.close()

print('\nScan terminé')
