import pytest
from models import Song, Playlist

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
            seconds=20,
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
            seconds=23,
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
            seconds=24,
        )
    )

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