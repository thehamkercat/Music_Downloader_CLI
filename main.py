import requests
import wget
import os
from colorama import Fore
import jiosaavn_app

try:
    while True:
        try:
            service = int(input(Fore.YELLOW + ''' \nWhich Service Do You Want To Use? , Enter 0 To Exit\n\n 1. JioSaavn\n\n > '''))
        except ValueError:
            print(Fore.LIGHTGREEN_EX + '\n Exited!\n')
            exit()

        try:
            if service == 1:
                from config import jiosaavn_api as jsapi
                song_name = input(Fore.YELLOW + " \nEnter The Name Of Song You Want To Download.\n\n> ")
                print(Fore.YELLOW + "\nSearching....\n")

                try:
                    r = requests.get(f"{jsapi}{song_name}")
                except:
                    print(Fore.RED + "You're Having Some Network Issues, Try To Ping The Server.\n")
                    exit()
 
                n = 0
                ii = 0
                print(Fore.LIGHTGREEN_EX + "Found These Songs:\n")

                for i in range(5):
                    song_name = f"{r.json()[i]['song']}-{r.json()[i]['singers']}-{r.json()[i]['year']}"
                    print(f"{Fore.LIGHTGREEN_EX} {n}. {song_name}")
                    n += 1

                song_index = int(input(Fore.YELLOW + " \nEnter Song's Index To Download It.\n\n > "))
                s = song_index
                song_name = f"{r.json()[s]['song']}-{r.json()[s]['singers']}-{r.json()[s]['year']}"
                song_link = r.json()[song_index]['media_url']
                print(Fore.YELLOW + "\nDownloading....\n")

                download = wget.download(song_link)
                final_song_name = f"{song_name}.m4a"
                os.rename(download, final_song_name)
                
                print(Fore.LIGHTGREEN_EX + " \n\nDownloaded In Current Directory")
            
            elif service == 0:
                print(Fore.LIGHTGREEN_EX + "\nExited!\n")
                exit()

        except ValueError:
            print(Fore.RED + '\n Wrong Input! Try Again.\n')

except KeyboardInterrupt or ValueError:
    print(Fore.LIGHTGREEN_EX + '\n\n Exited!\n')
