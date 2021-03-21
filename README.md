# musicDownloader
Download music using Google

# Purpose
The purpose of musicDownloader is to quickly download music to the directory that you launch the program from. The song should be downloaded using nothing of a brief description of the song.

# How does it work
1. Asking the user for a song description (e.g. 'enter sandman metallica').
2. Performing a Google search using the 'google' library. This search uses the song description + 'youtube lyrics' as it's search terms.
3. Retrieve the url of the first result.
4. Use the 'youtube_dl' library to download the audio that corresponds with the retrieved url to the current directory.

# Installation
Personally I prefer clone the download the content of the musicDownloader repo to a folder in my home directory (e.g. /home/kaz1m1r/thirdPartyPrograms) and then add this folder to my PATH variable. This can be done by adding the line ```export PATH=$PATH:/home/kaz1m1r/thirdPartyPrograms``` to my ```.bashrc``` and/or ```.zshrc```. This ensures that every time I start a terminal session the folder ```/home/kaz1m1r/thirdPartyPrograms``` is added to my PATH variable. In turn it makes it easier to download music in different folders since I only have to create a foler named after a band, ```cd``` into the folder and download the music.

# Used libraries
1. [google](https://pypi.org/project/googlesearch-python/)
2. [youtube_dl](https://youtube-dl.org/)
3. [termcolor](https://pypi.org/project/termcolor/)
4. [typing](https://docs.python.org/3/library/typing.html)

The first three libraries can be installed using pip3. The ```typing``` module is a part of the standard libraries.
