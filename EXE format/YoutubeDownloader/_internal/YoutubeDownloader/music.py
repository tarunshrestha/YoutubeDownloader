class MusicDownloader:
    def __init__(self, youtube):
        self.youtube = youtube
        self.aud = None
        self.audio = youtube.streams.filter(only_audio=True)

    def start(self):
        self.aud = list(enumerate(self.audio))
        for i in self.aud:
            print(i)
        strm = int(input("Select the type of Audio:Type '5' for mp3 default.\n"))
        if strm == 5:
            self.audio[0].download(filename=f"{self.youtube.title}.mp3")
        elif 0 <= strm < len(self.aud):
            self.audio[self.aud[strm][0]].download()
        else:
            print("Invalid selection. Please try again.")
