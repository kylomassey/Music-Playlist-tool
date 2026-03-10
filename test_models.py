import pytest
import json
from models import Song, Playlist
from utils import to_json, json_to_data

song_data = {"name":"Blinding Lights",
                "artist":"The Weeknd", "album":"After Hours",
                "year":2020, "minutes":3,
                "seconds":20, "bpm":171,
                "rating":5, "genre":"Pop"}
song_info = Song(
            name="Blinding Lights", artist="The Weeknd",
            album="After Hours", year=2020,
            bpm=171, genre="Pop",
            rating=5, minutes=3,
            seconds=20)

def make_playlist():
    playlist = Playlist()

    playlist.add_song(
        Song(
            name="Blinding Lights",
            artist="The Weeknd",
            album="After Hours",
            year=2020,
            bpm=171,
            genre="Pop",
            rating=5,
            minutes=3,
            seconds=20
        )
    )

    playlist.add_song(
        Song(
            name="Levitating",
            artist="Dua Lipa",
            album="Future Nostalgia",
            year=2020,
            bpm=103,
            genre="Pop",
            rating=4,
            minutes=3,
            seconds=23
        )
    )

    playlist.add_song(
        Song(
            name="Take Five",
            artist="The Dave Brubeck Quartet",
            album="Time Out",
            year=1959,
            bpm=174,
            genre="Jazz",
            rating=5,
            minutes=5,
            seconds=24
        )
    )
    playlist.print_songs
    return playlist

def test_filter_by_genre():
    playlist = make_playlist()

    results = playlist.filter(genre="pop")

    assert len(results) == 2
    assert [song.name for song in results] == ["Blinding Lights", "Levitating"]

def test_filter_by_rating():
    playlist = make_playlist()

    results = playlist.filter(min_rating=5)

    assert len(results) == 2
    assert [song.name for song in results] == ["Blinding Lights", "Take Five"]


def test_filter_by_bpm_range():
    playlist = make_playlist()

    results = playlist.filter(min_bpm=100, max_bpm=110)

    assert len(results) == 1
    assert results[0].name == "Levitating"


def test_filter_combined():
    playlist = make_playlist()

    results = playlist.filter(genre="pop", min_rating=5)

    assert len(results) == 1
    assert results[0].name == "Blinding Lights"


def test_invalid_bpm_range():
    playlist = make_playlist()

    with pytest.raises(ValueError):
        playlist.filter(min_bpm=150, max_bpm=120)


def test_invalid_rating():
    playlist = make_playlist()

    with pytest.raises(ValueError):
        playlist.filter(min_rating=10)


def test_invalid_genre_type():
    playlist = make_playlist()

    with pytest.raises(TypeError):
        playlist.filter(genre=123)


def test_invalid_min_bpm_type():
    playlist = make_playlist()

    with pytest.raises(TypeError):
        playlist.filter(min_bpm="fast")

def test_dict_to_song():
    mysong = Song.from_dict(song_data)
    data = song_info.to_dict()

    assert mysong.artist == song_info.artist
    assert mysong.album == song_info.album
    assert mysong.name == song_info.name
    assert mysong.genre == song_info.genre
    assert mysong.year == song_info.year
    assert mysong.rating == song_info.rating
    assert mysong.minutes == song_info.minutes
    assert mysong.seconds == song_info.seconds
    assert data == song_data

def test_json_roundtrip():
    playlist = make_playlist()
    file = "test"

    info = playlist.to_dict()
    to_json(data= info, filename= file)
    new_info = json_to_data(filename= file)
    newplaylist = Playlist.from_dict(new_info)

    assert len(newplaylist.songs) == len(playlist.songs)
    for original_song, loaded_song in zip(playlist.songs, newplaylist.songs):
        assert loaded_song.name == original_song.name
        assert loaded_song.artist == original_song.artist
        assert loaded_song.album == original_song.album
        assert loaded_song.genre == original_song.genre
        assert loaded_song.bpm == original_song.bpm
        assert loaded_song.rating == original_song.rating
        assert loaded_song.minutes == original_song.minutes
        assert loaded_song.seconds == original_song.seconds
        assert loaded_song.year == original_song.year

def test_invalid_json_filename():
    with pytest.raises(FileNotFoundError):
        json_to_data("RANDOM FILE NAME")

def test_song_from_dict_rejects_missing_name():
    data = {
        "artist": "Daft Punk",
        "genre": "Electronic",
        "bpm": 123,
        "rating": 5,
    }

    with pytest.raises(ValueError, match="Missing required field: name"):
        Song.from_dict(data)


def test_song_from_dict_rejects_none_name():
    data = {
        "name": None,
        "artist": "Daft Punk",
        "genre": "Electronic",
        "bpm": 123,
        "rating": 5,
    }

    with pytest.raises(ValueError, match="name is required"):
        Song.from_dict(data)


def test_load_from_json_missing_file():
    with pytest.raises(FileNotFoundError):
        json_to_data("does_not_exist.json")


def test_load_from_json_malformed_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{ not valid json }", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        json_to_data(bad_file)


def test_load_from_json_missing_song_field(tmp_path):
    bad_data = {
        "name": "Road Trip",
        "songs": [
            {
                "name": "Levitating",
                "artist": None,
                "genre": "Pop",
                "bpm": 103,
                "rating": 4,
            }
        ],
    }

    file_path = tmp_path / "playlist.json"
    file_path.write_text(json.dumps(bad_data), encoding="utf-8")

    with pytest.raises(ValueError, match= "Missing required field: name"):
        info = json_to_data(filename= file_path)
        Playlist.from_dict(data= info)