import pyautogui
import time
from datetime import datetime
import threading

st = [
    "15:10:00",
    "15:20:30",
    "16:00:00",
    "16:15:30",
    "16:55:00",
    "17:05:30",
    "17:45:00"
] #put what u like here~

def current_time_str():
    return datetime.now().strftime("%H:%M:%S")

def should_execute_now():
    return current_time_str() in st

def user_input():
    while True:
        command = input()
        if command.lower() == "exit":
            print("Exiting...")
            global running
            running = False
            break

def main():
    global running
    running = True
    print("Started...")
    last_output_time = datetime.now()

    input_thread = threading.Thread(target=user_input)
    input_thread.daemon = True
    input_thread.start()

    while running:
        now = datetime.now()
        current_str = current_time_str()

        if should_execute_now():
            pyautogui.hotkey('ctrl', 'alt', 'p')
            print(f"Executed[Ctrl+Alt+P] : {current_str}")
            st.remove(current_str)
            if not st:
                print("Exiting...")
                running = False
                break

        if (now - last_output_time).total_seconds() >= 180:
            print("Running...")
            last_output_time = now

        time.sleep(1) #optimize

if __name__ == "__main__":
    main()