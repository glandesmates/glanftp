from colorama import init, Fore
from ftplib import FTP
import argparse as arg
import ftplib
import os


init(autoreset=False)
banner = r"""
 ________  ___       ________  ________   ________ _________  ________   
|\   ____\|\  \     |\   __  \|\   ___  \|\  _____\\___   ___\\   __  \  
\ \  \___|\ \  \    \ \  \|\  \ \  \\ \  \ \  \__/\|___ \  \_\ \  \|\  \ 
 \ \  \  __\ \  \    \ \   __  \ \  \\ \  \ \   __\    \ \  \ \ \   ____\
  \ \  \|\  \ \  \____\ \  \ \  \ \  \\ \  \ \  \_|     \ \  \ \ \  \___|
   \ \_______\ \_______\ \__\ \__\ \__\\ \__\ \__\       \ \__\ \ \__\   
    \|_______|\|_______|\|__|\|__|\|__| \|__|\|__|        \|__|  \|__|   
                                                                         

                            By Mynor Estrada

                          [GITHUB] GlandesMates
                          [YOUTUBE] GlandesMates


"""
print(Fore.GREEN + banner)

parser = arg.ArgumentParser()
parser.add_argument('to', help='[host victim here]')
parser.add_argument('-usr', help='[custom login (user)]')
parser.add_argument('-pwd', help='[custom login (password)]')
args = parser.parse_args()

def emul(osOne, osTwo):
    try: osOne
    except: osTwo

host = args.to

try:

    with FTP(host, timeout=5) as ftp:

        try:

            if args.usr and args.pwd:
                ftp.login(args.usr, args.pwd)
            else:
                ftp.login('anonymous', 'anonymous@')

            print(f'Sucesfully logged in {host}')


            def commander():

                while True:

                    command = input('> ')

                    try:
                        
                        if command.startswith('cd'):
                            ftp.cwd(command[3:])
                        elif command == 'clear' or command == 'cls':
                            try: os.system('cls')
                            except: os.system('clear')
                        elif command == 'back' or command == 'cd ..' or command == '..':
                            emul(os.system('cd ..'), os.system('..'))
                        elif command == 'dir' or command == 'ls':
                            ftp.dir()
                        elif command == 'exit':
                            ftp.quit()
                            break
                        elif command == 'close':
                            ftp.close()
                            break
                        
                        elif command.startswith('open'):
                            ftp.retrbinary('RETR %s' %command[5:], open(command[5:], 'wb').write)
                            open(command[5:])
                        elif command.startswith('get file'):
                            ftp.retrbinary('RETR %s' %command[9:], open(command[9:], 'wb').write)
                            print(f'{command[9:]} downloaded')
                        elif command.startswith('get dir'):
                            ftp.retrlines(command[8:])

                        elif command.startswith('mkdir'):
                            ftp.mkd(command[6:])
                        elif command.startswith('size'):
                            ftp.size(command[5:])
                        elif command.startswith('rm'):
                            try:
                                ftp.rmd(command[3:])
                            except:
                                ftp.delete(command[3:])
                        elif command == 'name':
                            print(f'Name: {ftp.pwd()}')
                        elif command.startswith('sf '):
                            ftp.storbinary('STOR %s' %command[3:], open(command[3:], 'rb'))
                            print(f'Archive {command[3:]} sucesfully sended')
                        elif command.startswith('rename'):
                            ftp.rename(fromname=command[7:], toname=input('New name file: '))
                        elif command == 'get all':
                            files = ftp.nlst()
                            for file in files:
                                print(file)
                                try:
                                    ftp.retrbinary('RETR %s' %file, open(file, 'wb').write)
                                    print(f'{file} downloaded')
                                except:
                                    pass
                                if KeyboardInterrupt:
                                    break
                        
                        elif command == 'help':
                            print("""
                            cd (directory to access)           get file (file to download)
                            cls, clear (clean terminal)        get all (get all files)
                            rm (filename to delete)            sf (send file)
                            size (file size)                   back, .., cd .. (back)
                            mkdir (make directory)             help (show this message)
                            dir, ls (see content)              close, exit (end)
                            name (location path)
                            """)
                        else:
                            print(f'{command} is a not valid command')

                        print()

                    except ftplib.Error as e:
                        print(e)
                        continue


            commander()
            print(Fore.RESET + Fore.LIGHTGREEN_EX + '\n\t\tGoodbye...')

        except ftplib.Error as e:
            print(e)

except ftplib.Error as e:
    print(e)
