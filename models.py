from utils import format_duration

class Song:
    def __init__(self, name, artist, album, year,
                 bpm, genre, rating, minutes = 0, seconds = 0):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
        self.minutes = minutes
        self.seconds = seconds
        self.bpm = bpm
        self.rating = rating
        self.genre = genre

    def set_track_time(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def mins_to_secs(self):
        time = (self.minutes * 60) + self.seconds
        return time

    def print_song_info(self):
        print("Song:", self.name, " by ", self.artist, " | BPM: ", self.bpm,
             " | Rating: ", self.rating)

class Playlist:
    def __init__(self):
        self.songs  = []
        self.totaltime = 0

    def add_song(self, song):
        self.songs.append(song)

    def duration(self):
        time = 0
        if not self.songs:
            return time
        for song in self.songs:
            time += song.mins_to_secs()
        self.totaltime = time
        return format_duration(time)
    
    def print_songs(self, list = None):
        cnt = 1
        if not list:
            list = self.songs
        print("\nYour Playlist")
        for song in list:
            print(f"{cnt}) {song.name}")
            cnt += 1

    def filter(self, genre = None, artist = None, album = None):
        results = []
        for song in self.songs:
            if genre is not None and genre.lower() != song.genre.lower():
                continue
            if artist is not None and artist.lower() not in song.artist.lower():
                continue
            if album is not None and album.lower() not in song.album.lower():
                continue
            results.append(song)
        self.print_songs(results)