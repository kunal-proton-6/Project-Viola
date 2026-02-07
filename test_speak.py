"""
Test script to verify all speak commands are working
"""
import pyttsx3
import sys

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return True
    except Exception as e:
        print(f"Error in speak: {e}")
        sys.stdout.flush()
        return False

def test_all_speak_commands():
    """Test all speak commands from the main program"""
    
    test_messages = [
        "Initializing Viola...",
        "Opening Google...",
        "Opening Youtube...",
        "Opening GitHub...",
        "Opening Stack Overflow...",
        "Yes, how can I help you?",
        "I didn't understand that command",
        "The time is 01:23 PM",
        "I am Viola, your AI assistant",
        "Stopping Viola. Goodbye!"
    ]
    
    print("Testing all speak commands from main.py...")
    print("=" * 60)
    
    success_count = 0
    failure_count = 0
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n[Test {i}/{len(test_messages)}] Speaking: '{message}'")
        if speak(message):
            print(f"✓ SUCCESS")
            success_count += 1
        else:
            print(f"✗ FAILED")
            failure_count += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {success_count} passed, {failure_count} failed")
    print("=" * 60)
    
    if failure_count == 0:
        print("\n✓ All speak commands are working correctly!")
        return True
    else:
        print(f"\n✗ {failure_count} speak command(s) failed!")
        return False

if __name__ == "__main__":
    test_all_speak_commands()
