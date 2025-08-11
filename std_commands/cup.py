# desc: change password
import os def main(): new_pass = input("new 
    password: ") path = 
    os.path.expanduser("~/user/user.py") 
    lines = [] with open(path, "r") as f:
        lines = f.readlines() for i in 
    range(len(lines)):
        if lines[i].startswith("password"): 
            lines[i] = f"password = 
            '{new_pass}'\n"
    with open(path, "w") as f: 
        f.writelines(lines)
    print("Passwort geändert!") if __name__ 
== "__main__":
    main()
