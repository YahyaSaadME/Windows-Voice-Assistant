import pyautogui
import time

# List of key combinations (each inner list represents a key combination)

def execute_key_combinations(combinations,sleep=1):
    for combo in combinations:
        print(f"Executing: {' + '.join(combo)}")
        if 'write' in combo:
            pyautogui.write(combo[1])
        else:    
            pyautogui.hotkey(*combo)  # Unpack the list into arguments for hotkey
        time.sleep(sleep)  # Wait 1 second between commands for visibility


# key_combinations = [
#         ['win', 'e'],
#     ]
# execute_key_combinations(key_combinations)
