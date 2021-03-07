from __future__ import unicode_literals
import requests
import wget
import os
from youtube_search import YoutubeSearch
import youtube_dl
from colorama import Fore


try:
    while True:
        try:
            service = int(input(Fore.YELLOW + ''' \nWhich Service Do You Want To Use? , Enter 0 To Exit\n\n 1. JioSaavn\n 2. Youtube Audio\n 3. Youtube Video\n\n > '''))
        except ValueError:
            print(Fore.LIGHTGREEN_EX + '\n Exited!\n')
            exit()

        try:
            if service == 1:
                query = input(Fore.YELLOW + " \nEnter The Name Of Song You Want To Download.\n\n> ")
                print(Fore.YELLOW + "\nSearching....\n")

                try:
                    r = requests.get(f"https://jiosaavnapi.bhadoo.uk/result/?query={query}")
                except:
                    print(Fore.RED + "You're Having Some Network Issues, Try To Ping The Server.\n")
                    exit()

                n = 0
                ii = 0
                count = len(r.json())

                print(Fore.LIGHTGREEN_EX + "Found These Songs:\n")

                for i in range(count):
                    song_name = f"{r.json()[i]['song']}-{r.json()[i]['singers']}-{r.json()[i]['year']}"
                    print(f"{Fore.LIGHTGREEN_EX} {n}. {song_name}")
                    n += 1

                song_index = int(input(Fore.YELLOW + " \nEnter Song Number To Download It.\n\n > "))
                s = song_index
                song_name = f"{r.json()[s]['song']}-{r.json()[s]['singers']}-{r.json()[s]['year']}"
                song_link = r.json()[song_index]['media_url']
                print(Fore.YELLOW + "\nDownloading....\n")

                download = wget.download(song_link)
                final_song_name = f"{song_name}.m4a"
                os.rename(download, final_song_name)

                print(Fore.LIGHTGREEN_EX + " \n\nDownloaded In Current Directory\n")
            

            elif service == 2:
                query = input(Fore.YELLOW + " \nEnter The Name Of Song You Want To Download\Listen.\n\n> ")
                print(Fore.YELLOW + "\nSearching....\n")
                
                results = YoutubeSearch(query, max_results=5).to_dict()

                for i in range(len(results)):
                    print(f"{i}. {results[i]['title']}")
 
                song_index = int(input(Fore.YELLOW + " \nEnter Song Number.\n\n > "))
                query2 = int(input(Fore.YELLOW + " \nWhat Do You Want To Do?\n 1. Download\n 2. Listen\n\n> "))
                yt_link = f"https://youtube.com{results[song_index]['url_suffix']}"
                if query2 == 1:
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([yt_link])
                print(Fore.LIGHTGREEN_EX + " \n\nDownloaded In Current Directory\n")
                if query2 == 2:
                    print(Fore.YELLOW + "\nLoading...\n")
                    os.system(f"mpv {yt_link} --no-video")

                
            elif service == 3:
                query = input(Fore.YELLOW + " \nEnter The Name Of Video You Want To Download/Stream.\n\n> ")
                print(Fore.YELLOW + "\nSearching....\n")
                
                results = YoutubeSearch(query, max_results=5).to_dict()

                for i in range(len(results)):
                    print(f"{i}. {results[i]['title']}")
 
                song_index = int(input(Fore.YELLOW + " \nEnter Video Number.\n\n > "))
                query2 = int(input(Fore.YELLOW + " \nWhat Do You Want To Do?\n 1. Download\n 2. Stream\n\n> "))
                yt_link = f"https://youtube.com{results[song_index]['url_suffix']}"
                if query2 == 1:
                    ydl_opts = {}
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([yt_link])
                    print(Fore.LIGHTGREEN_EX + " \n\nDownloaded In Current Directory\n")
                if query2 == 2:
                    print(Fore.YELLOW + "\nLoading...\n")
                    os.system(f"mpv {yt_link}")

        except ValueError:
            print(Fore.RED + '\n Wrong Input! Try Again.\n')

except KeyboardInterrupt or ValueError:
    print(Fore.LIGHTGREEN_EX + '\n\n Exited!\n')
