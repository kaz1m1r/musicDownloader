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
