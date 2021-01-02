import requests
import wget
import os

while True:
    service = int(input(''' \nWhich Service Do You Want To Use? , Enter 0 To Exit1. JioSaavn\n\n > '''))
    if service == 1:
        from config import jiosaavn_api as jsapi
        song_name = input(" \nEnter The Name Of Song You Want To Download.> ")
        print("\nSearching....\n")
        r = requests.get(f"{jsapi}{song_name}")
        n = 0
        ii = 0
        print("Found These Songs:")
        for i in range(5):
            song_name = f"{r.json()[i]['song']}-{r.json()[i]['singers']}-{r.json()[i]['year']}"
            print(f"{n}. {song_name}")
            n += 1
        song_index = int(input(" \nEnter Song's Index To Download It.\n\n > "))
        s = song_index
        song_name = f"{r.json()[s]['song']}-{r.json()[s]['singers']}-{r.json()[s]['year']}"
        song_link = r.json()[song_index]['media_url']
        print("\nDownloading....\n")
        download = wget.download(song_link)
        final_song_name = f"{song_name}.m4a"
        os.rename(download, final_song_name)
        print(" \n\nDownloaded In Current Directory")
