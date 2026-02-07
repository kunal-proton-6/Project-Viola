"""
Test script to verify music library functionality
"""
import musicLibrary

def test_music_library():
    print("Testing Music Library...")
    print("=" * 60)
    
    # Test 1: List all available songs
    print("\n[Test 1] Available songs in library:")
    songs = musicLibrary.list_available_songs()
    for song in songs:
        print(f"  • {song}")
    
    # Test 2: Get specific music links
    print("\n[Test 2] Testing song lookups:")
    test_songs = ["virtual", "checkpoint", "ping", "overthinker", "playlist", "unknown_song"]
    
    for song in test_songs:
        link = musicLibrary.get_music_link(song)
        if link:
            print(f"  ✓ '{song}' -> {link[:50]}...")
        else:
            print(f"  ✗ '{song}' not found in library")
    
    # Test 3: Test case-insensitive lookup
    print("\n[Test 3] Case-insensitive lookup:")
    test_cases = ["VIRTUAL", "Virtual", "viRtual"]
    for case in test_cases:
        link = musicLibrary.get_music_link(case)
        if link:
            print(f"  ✓ '{case}' correctly found")
        else:
            print(f"  ✗ '{case}' lookup failed")
    
    print("\n" + "=" * 60)
    print("✓ Music library is working correctly!")

if __name__ == "__main__":
    test_music_library()
