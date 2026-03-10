from utils import format_duration, validate_number, validate_str, dict_to_song

class Song:
    def __init__(self, name = None, artist= None, album= None, year= None,
                 bpm= None, genre= None, rating= None, minutes = 0, seconds = 0):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
        self.minutes = minutes
        self.seconds = seconds
        self.bpm = bpm
        self.rating = rating
        self.genre = genre

    def song_to_dict(self):
        data = {"name":self.name,
                "artist":self.artist, "album":self.album,
                "year":self.year, "minutes":self.minutes,
                "seconds":self.seconds, "bpm":self.bpm,
                "rating":self.rating, "genre":self.genre}
        return data

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
    
    def print_songs(self, songs = None):
        cnt = 1
        if not songs:
            songs = self.songs
        print("\nYour Playlist")
        for song in songs:
            print(f"{cnt}) {song.name}")
            cnt += 1
    
    def from_dict(self, data):
        for song in data["songs"]:
            self.add_song(dict_to_song(song))


    def to_dict(self):
        playlist_data = []
        for song in self.songs:
            playlist_data.append(song.song_to_dict())
        return {"songs": playlist_data}

    def filter(self, genre = None, artist = None, album = None, min_bpm = None, max_bpm = None, min_rating = None):
        results = []

        validate_str(genre, "genre")
        validate_str(artist, "artist")
        validate_str(album, "album")

        validate_number(min_bpm, "min_bpm")
        validate_number(max_bpm, "max_bpm")
        validate_number(min_rating, "min_rating")

        if min_bpm is not None and max_bpm is not None and max_bpm < min_bpm:
            raise ValueError("min_bpm must be less than or equal to max_bpm")
        
        if min_rating is not None and not (0 <= min_rating <= 5):
            raise ValueError("min_rating must be greater than or equal to zero and less than or equal to 5")

        for song in self.songs:
            if genre is not None and genre.lower() != song.genre.lower():
                continue
            if artist is not None and artist.lower() not in song.artist.lower():
                continue
            if album is not None and album.lower() not in song.album.lower():
                continue
            if min_bpm is not None and song.bpm < min_bpm:
                continue
            if max_bpm is not None and song.bpm > max_bpm:
                continue
            if min_rating is not None and song.rating < min_rating:
                continue

            results.append(song)
        return results