from models import Song, Playlist
from utils import format_duration

def main():
    print("Music Playlist Tool")
    song1 = Song("Here we are", "The Journey", "Still here", 2009, 110, "rock", 4.5, 2, 30)
    song2 = Song("Sacred Sword", "The Journey", "Still here", 2009, 110, "rock", 2, 4, 20)
    song3 = Song("Flight to the stars", "My Mystery", "Vagabond", 2009, 110, "rock", 5, 5, 30)
    mysongs = Playlist()
    mysongs.add_song(song1)
    mysongs.add_song(song2)
    mysongs.add_song(song3)
    print(mysongs.duration())
    mysongs.print_songs()
    filtered_songs = mysongs.filter(genre = "rock", album = "Vag", rating = 1)
    if filtered_songs:
        mysongs.print_songs(filtered_songs)

if __name__ == "__main__":
    main()