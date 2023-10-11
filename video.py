class VideoDownloader:
    def __init__(self, youtube):
        self.youtube = youtube
        self.vid = None
        self.videos = youtube.streams.filter(progressive=True)
        
        
    def start(self):
        self.vid = list(enumerate(self.videos))

        for i in self.vid:
            print(i)

        strm = int(input("Select Resolution:"))
        self.videos[strm].download()