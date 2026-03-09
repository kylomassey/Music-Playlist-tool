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
    
    def print_songs(self):
        cnt = 1
        print("\nYour Playlist")
        for song in self.songs:
            print(f"{cnt}) {song.name}")
            cnt += 1

    def filter(self, arg, param):
        return 0