from pytube import YouTube
from os import system
from video import VideoDownloader
from music import MusicDownloader


def main():
    canrun = True
    while canrun:
        system('cls')
        print(" WELCOME TO THE YOUTUBE VIDEO DOWNLOADER")
        link = input("Paste the link below:\n")
        youtube = YouTube(link)
        vd = VideoDownloader(youtube)
        md = MusicDownloader(youtube )
        print(f"Video to download: \n{youtube.title}")
        #print("Image link: " + youtube.thumbnail_url)
        canplay = True
        while canplay:
            ask = input("What do you wanna download music or video?Type 'music', 'video' and 'All' for both.\n").lower()
            if ask == "video":
                vd.start()
                canplay = False
            elif ask == "music":
                md.start()
                canplay = False
            elif ask == "all":
                vd.start()
                md.start()
                canplay = False
            elif ask == "exit":
                break
            else:
                print("Type again.")
            print("Successfully Downloaded!")
        again = input("Do you wanna download again??Type 'y' to download Or 'n' to end.").lower()
        if again != 'y':
            print("GoodBye!")
            canrun = False
        else:
            main()

main()

