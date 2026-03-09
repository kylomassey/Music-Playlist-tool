from models import Song, Playlist
from utils import format_duration

def main():
    print("Music Playlist Tool")
    song1 = Song("Here we are", "The Journey", "Still here", 2009, 110, "rock", 1.5, 2, 30)
    song2 = Song("Sacred Sword", "The Journey", "Still here", 2009, 110, "rock", 1.5, 4, 20)
    song3 = Song("Flight to the stars", "The Journey", "Still here", 2009, 110, "rock", 1.5, 5, 30)
    mysongs = Playlist()
    mysongs.add_song(song1)
    mysongs.add_song(song2)
    mysongs.add_song(song3)
    print(mysongs.duration())
    mysongs.format_duration()
    mysongs.print_songs()

if __name__ == "__main__":
    main()