'''
TODO:
ONLY DOWNLOAD .mp3 FILES
------------------------

1. Aks if you want to download an album or a song.
2. Ask which album/song you want to download.
3. Download the album/song.
    3.1. Ask where you want to save the album/song.
    3.2. Save the album/song to the specified location.

NOTES:
1. If searching YouTube, only look for 'lyrics' videos
'''

from Music import GoogleSearch
if __name__ == "__main__":
    song = "20 percent cooler"
    file_type = "mp3"
    gs = GoogleSearch()
    result = gs.SearchSong(song, file_type)
    print(result)
