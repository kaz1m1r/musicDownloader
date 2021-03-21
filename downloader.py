#!/usr/bin/python3

from typing import List
from googlesearch import search
from youtube_dl import YoutubeDL
from termcolor import colored


class Downloader:

    def __init__(self):
        """
        Class whose instance can be used to extract audio from a URL
        """

        # instance of YoutubeDownload class that can download a video using a url
        # with only the url
        self.video_downloader = YoutubeDL({"format": "mp4"})

        # instance of YoutubeDownload class that can download audio using a url
        # audio_downloader = YoutubeDL({"format": "bestaudio"})  # downloads best audio file
        self.audio_downloader = YoutubeDL({"format": "m4a"})

    def downloadVideo(self, url: str) -> None:
        """
        Download video using a url
        :param url: str
        :return: None
        """

        # download the video to the current directory
        self.video_downloader.extract_info(url)

    def downloadAudio(self, url: str) -> None:
        """
        Download audio file using a url
        :param url: str
        :return: None
        """

        # download the audio file in the current directory
        self.audio_downloader.extract_info(url)


class GoogleSearch:

    def __init__(self):
        """
        Class whose instance can retrieve urls
        """

    def SearchSong(self, song_description: str) -> str:
        """
        Retrieve the url that corresponds with the lyrics video of a son. The url is always
        a YouTube url.
        :param song_description: description of song (e.g. "bohemian rhapsody queen")
        :return: str
        """

        # query that should be performed to get the url to a .mp3 file
        query: str = f"youtube lyrics {song_description}"

        # empty string that contains the query results
        results: List[str] = []

        # querying google and appending results to 'results' list
        for result in search(query=query, tld='co.in', lang='en', num=10, stop=10, pause=2):
            results.append(result)

        # return url as string
        return results[0]


def welcomeMessage() -> None:
    """
    Print a welcome message
    :return: None
    """

    # saving the name of the program as ASCII art
    message: str = "" \
                   "    .___                  .__                    .___             \n" \
                   "  __| _/______  _  ______ |  |   _________     __| _/___________  \n" \
                   " / __ |/  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \ \n" \
                   "/ /_/ (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/ \n" \
                   "\____ |\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|    \n" \
                   "     \/                 \/                \/      \/    \/        \n"

    # saving the usage of the program in a variable
    usage: str = f"                                                       version 1\n\n" \
                 f"USAGE: \n" \
                 f"{colored('----------------------------------------------------------------', 'yellow')} \n" \
                 f"Enter a song description (e.g. 'bohemian rhapsody queen') \n" \
                 f"to download the song into the current directory. Enter '{colored('quit', 'red')} \n" \
                 f"at 'song > ' and press the 'enter' key to quit the program.\n" \
                 f"{colored('----------------------------------------------------------------', 'yellow')}"

    # print ASCII art name and usage
    print(colored(message, 'magenta'))
    print(usage)

def useDownloader() -> None:
    """
    This function handles the interaction with the user
    :return: None
    """

    # making instances of the Downloader class and GoogleSearch class
    downloader: Downloader = Downloader()
    google_search: GoogleSearch = GoogleSearch()

    # continually asking to for songs to download
    while True:
        song: str = input("\nsong > ")
        if song != 'quit':
            try:
                url: str = google_search.SearchSong(song)
            except Exception:
                print(f"{song} wasn't found. Try another description/song.")

            try:
                downloader.downloadAudio(url)
            except Exception:
                print(colored(f"Url for '{song}' was found but downloading failed", 'red'))
        else:
            print("\nbye!")
            break


if __name__ == "__main__":

    # welcome message to the user
    welcomeMessage()

    # start using downloader
    useDownloader()
