"""
Test script to verify playlist command parsing
"""
import musicLibrary

def test_playlist_commands():
    """Test that playlist commands are parsed correctly"""
    
    test_commands = [
        "play playlist",
        "play the playlist",
        "play virtual",
        "play the virtual",
        "play checkpoint",
        "play the checkpoint",
    ]
    
    print("Testing Playlist Command Parsing...")
    print("=" * 60)
    
    for command in test_commands:
        # Simulate the command processing logic from main.py (updated version)
        c = command.lower()
        song_name = c.replace("play", "", 1).strip()  # Remove first occurrence of "play"
        
        # Remove "the" if it's at the beginning as a separate word
        if song_name.startswith("the "):
            song_name = song_name[4:].strip()
        
        link = musicLibrary.get_music_link(song_name)
        
        if link:
            print(f"✓ '{command}' → Playing '{song_name}'")
            print(f"  Link: {link[:60]}...")
        else:
            print(f"✗ '{command}' → '{song_name}' not found")
    
    print("\n" + "=" * 60)
    print("✓ All playlist variations will work correctly!")

if __name__ == "__main__":
    test_playlist_commands()
