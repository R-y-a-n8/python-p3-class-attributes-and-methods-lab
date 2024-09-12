#!/usr/bin/env python3

from song import Song

def test_song_creation():
    song = Song("99 Problems", "Jay-Z", "Rap")
    assert song.name == "99 Problems"
    assert song.artist == "Jay-Z"
    assert song.genre == "Rap"

def test_song_count():
    Song.count = 0
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    assert Song.count == 2

def test_genres():
    Song.genres = []
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    assert "Rap" in Song.genres
    assert "Pop" in Song.genres

def test_artists():
    Song.artists = []
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    assert "Jay-Z" in Song.artists
    assert "Beyonce" in Song.artists

def test_genre_count():
    Song.genre_count = {}
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    assert Song.genre_count["Rap"] == 1
    assert Song.genre_count["Pop"] == 1

def test_artist_count():
    Song.artist_count = {}
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    assert Song.artist_count["Jay-Z"] == 1
    assert Song.artist_count["Beyonce"] == 1
