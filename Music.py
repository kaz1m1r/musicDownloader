from typing import List
from googlesearch import search


class GoogleSearch:

    def __init__(self):
        """
        Class whose instance can retrieve urls
        :param search_description: Description of what you want to retrieve
        :param domain: website from which you want to retrieve
        """

    def SearchSong(self, song_name: str, file_type: str) -> str:
        """
        Perform google search and retrieve URL in the form of string. The url redirects
        to a file of the specified file type
        :return: str
        """

        # query that should be performed to get the url to a .mp3 file
        query: str = f"index of: .{file_type} {song_name}"

        # empty string that contains the query results
        results: List[str] = []

        # querying google and appending results to 'results' list
        for result in search(query=query, tld='co.in', lang='en', num=10, stop=10, pause=2):
            results.append(result)

        # return url as string
        return results[0]


class Song:

    def __init__(self, song_name: str, file_type: str):
        self.song_name = song_name
        self.file_type = file_type

        # making GoogleSearch object
        gs = GoogleSearch()

        # retreiving the url that corresponds with the song and file type
        self.song_url: str = gs.SearchSong(song_name, file_type)

    def getFileType(self) -> str:
        """
        Return the file type as string
        :return: str
        """

        # return the file type of the song as string
        return self.file_type

    def getName(self) -> str:
        """
        Return the name of the song
        :return: str
        """

        # return the song name as string
        return self.song_name

    def getSongUrl(self) -> str:
        """
        return the url that corresponds with the Song instance
        :return:
        """

        # return url as string
        return self.song_url


class Album:

    def __init__(self, songs: List[Song] = List[Song]):
        self.songs: List[Song] = songs

    def addSong(self, song: Song) -> None:
        """
        Adding a song to the album
        :param song: Song that should be added to album
        :return: None
        """

        # adding the song to the album
        self.songs.append(song)
