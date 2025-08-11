# desc: change user name
import os def main(): new_user = input("new 
    user name: ") path = 
    os.path.expanduser("~/user/user.py") 
    lines = [] with open(path, "r") as f:
        lines = f.readlines() for i in 
    range(len(lines)):
        if lines[i].startswith("username"): 
            lines[i] = f"username = 
            '{new_user}'\n"
    with open(path, "w") as f: 
        f.writelines(lines)
    print("Username geändert! Starte Termux 
    neu, um den Prompt zu aktualisieren.")
if __name__ == "__main__":
    main()
