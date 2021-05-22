import pafy
import time
import vlc

from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PL9FUXHTBubp-_e0wyNu1jfVVJ2QVAi5NW')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)

def Urlget(url) :

        start_time = time.time()
        media_player = vlc.MediaPlayer()  
        video = pafy.new(url)                                                                                                          
        best = video.getbestaudio()                                                                                                                 
        playurl = best.url                                                                                                                          
        player = vlc.MediaPlayer(playurl)
        media_player.audio_set_volume(30)                                                                                                           
        player.play()
        time.sleep(0.2)
        duration = player.get_length() / 1000
        time.sleep(duration)
        player.stop()
        
        seconds = 4
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time > seconds:
                print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
                pass
                break

for video_url in playlist.video_urls:
    print(video_url)
    Urlget(video_url)



