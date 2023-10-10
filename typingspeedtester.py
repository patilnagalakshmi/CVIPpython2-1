import time
def calculate_typing_speed(start_time, end_time, typed_text):
    # Calculate the time taken in seconds
    elapsed_time = end_time - start_time
    # Calculate the number of words typed
    typed_words = len(typed_text.split())
    # Calculate typing speed in words per minute (WPM)
    wpm = (typed_words / elapsed_time) * 60
    return wpm
def main():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter to start...")
    
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    wpm = calculate_typing_speed(start_time, end_time, typed_text)
    print(f"Your typing speed: {wpm:.2f} WPM")
    if wpm >= 40:
        print("Great job! You have excellent typing speed.")
    elif 20 <= wpm < 40:
        print("Not bad! Keep practicing to improve.")
    else:
        print("You might want to practice more to improve your typing speed.")

if __name__ == "__main__":
    main()
