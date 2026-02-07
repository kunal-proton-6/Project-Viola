"""
Music Library for Viola
Contains a collection of music links mapped to specific keywords
"""

music = {
    "virtual": "https://youtu.be/oklzVH8FfVQ?si=4l_9BmVeXazgCvO5",
    "checkpoint": "https://youtu.be/ieCU9OV8_tg?si=DoxhXJG6iPxv5DGQ",
    "ping": "https://youtu.be/RKW6rjnYEkc?si=TpQRY-msv2cjcoum",
    "overthinker": "https://youtu.be/luQSQuCHtcI?si=UeDet_p5wP-OoDzQ",
    "playlist": "https://www.youtube.com/watch?v=oklzVH8FfVQ&list=RDoklzVH8FfVQ&index=1"
}

def get_music_link(song_name):
    """
    Get the YouTube link for a specific song
    Returns the link if found, None otherwise
    """
    song_name = song_name.lower().strip()
    return music.get(song_name, None)

def list_available_songs():
    """
    Return a list of all available songs
    """
    return list(music.keys())
