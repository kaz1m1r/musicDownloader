from typing import List
from googlesearch import search
from youtube_dl import YoutubeDL


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
