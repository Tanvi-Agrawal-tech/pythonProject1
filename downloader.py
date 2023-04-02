from pytube import YouTube
link= input("please provide your link")
check=int(input("what do you want to download press 1 for video and press 2 for audio"))
if check==1:
    youtube_1= YouTube(link) #we can see all the streams
    #print(youtube_1.thumbnail_url) 
    videos=youtube_1.streams.filter(progressive=True)
    vid=list(enumerate(videos))
    for i in vid:
        print(i)
    strm=int(input("please provide your index you want to download"))
    videos[strm].download()
    print("video downloaded successfully")
elif check==2:
    youtube_1= YouTube(link)
    audio=youtube_1.streams.filter(only_audio=True)
    aud=list(enumerate(audio))
    for i in aud:
        print(i)
    strm2=int(input("please provide your index you want to download"))
    audio[strm2].download()
    print("audio downloaded successfully")

