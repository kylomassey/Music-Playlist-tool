from utils import format_duration, validate_number, validate_str

class Song:
    def __init__(self, name= None, artist= None, album= None, year= None,
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
    
    @classmethod
    def from_dict(cls, data):
        if "name" not in data:
            raise ValueError("Missing required field: name")
        if data["name"] is None:
            raise ValueError("name is required")
        validate_str(data["name"], "name")
        if data["genre"] is not None:
            validate_str(data["genre"], "genre")
        if data["artist"] is not None:
            validate_str(data["artist"], "artist")
        if data["album"] is not None:
            validate_str(data["album"], "album")

        if data["bpm"] is not None:
            validate_number(data["bpm"], "bpm")
        if data["rating"] is not None:
            validate_number(data["rating"], "rating")
        if data["year"] is not None:
            validate_number(data["year"], "year")
        if data["minutes"] is not None:
            validate_number(data["minutes"], "minutes")
        if data["seconds"] is not None:
            validate_number(data["seconds"], "seconds")

        if data["rating"] is not None and not (0 <= data["rating"] <= 5):
            raise ValueError("rating must be greater than or equal to zero and less than or equal to 5")
        if data["minutes"] is not None and (data["minutes"] < 0):
            raise ValueError("minutes can't be a negative nubmer")
        if data["seconds"] is not None and not (0 <= data["seconds"] < 60):
            raise ValueError("seconds must be greater than or equal to zero and less than 60")
        if data["year"] is not None and (data["year"] <= 0):
            raise ValueError("year must be greater than zero")
        if data["bpm"] is not None and (data["bpm"] <= 0):
            raise ValueError("bpm must be greater than zero")

        return cls(
        name= data["name"],
        artist= data["artist"],
        album= data["album"],
        year= data["year"],
        bpm= data["bpm"],
        genre= data["genre"],
        rating= data["rating"],
        minutes= data["minutes"],
        seconds= data["seconds"]
        )

    def to_dict(self):
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
    def __init__(self, songs = None):
        if songs is None:
            self.songs = []
        else:
            self.songs = songs
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
        if songs is None:
            songs = self.songs
        print("\nYour Playlist")
        for song in songs:
            print(f"{cnt}) {song.name}")
            cnt += 1
    
    @classmethod
    def from_dict(cls, data):
        songlist = []
        for song in data["songs"]:
            newsong= Song.from_dict(song)
            songlist.append(newsong)
        return cls(songs= songlist)

    def to_dict(self):
        playlist_data = []
        for song in self.songs:
            playlist_data.append(song.to_dict())
        return {"songs": playlist_data}

    def filter(self, name= None, genre = None, artist = None, album = None, min_bpm = None, max_bpm = None, min_rating = None):
        results = []

        validate_str(genre, "genre")
        validate_str(artist, "artist")
        validate_str(album, "album")
        validate_str(name, "name")

        validate_number(min_bpm, "min_bpm")
        validate_number(max_bpm, "max_bpm")
        validate_number(min_rating, "min_rating")

        if min_bpm is not None and max_bpm is not None and max_bpm < min_bpm:
            raise ValueError("min_bpm must be less than or equal to max_bpm")
        
        if min_rating is not None and not (0 <= min_rating <= 5):
            raise ValueError("min_rating must be greater than or equal to zero and less than or equal to 5")

        for song in self.songs:
            if name is not None and name.lower() not in song.name.lower():
                continue
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