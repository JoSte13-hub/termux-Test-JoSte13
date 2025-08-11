import os, sys, urllib.request, zipfile LOGO 
= r"""
        _ ____ _ _ _____
       | | ___/ ___|| |_ ___/ |___ /
    _ | |/ _ \___ \| __/ _ \ | |_ \
   | |_| | (_) |__) | || __/ |___) |
    \___/ \___/____/ \__\___|_|____/ """ def 
save_user(username, password):
    with 
    open(os.path.expanduser("~/user/user.py"), 
    "w") as f:
        f.write(f"username = 
        '{username}'\npassword = 
        '{password}'\n")
def load_user(): try: import importlib.util 
        path = 
        os.path.expanduser("~/user/user.py") 
        spec = 
        importlib.util.spec_from_file_location("user", 
        path) user = 
        importlib.util.module_from_spec(spec) 
        spec.loader.exec_module(user) return 
        user.username, user.password
    except: return None, None def 
new_account():
    print(LOGO) username = input("Name: ") 
    password = input("Password: ") 
    save_user(username, password) 
    print("\nAccount erstellt!")
def from_link(): print(LOGO) link = 
    input("Link: ") zip_path = 
    os.path.expanduser("~/downloads/system.zip") 
    urllib.request.urlretrieve(link, 
    zip_path) with zipfile.ZipFile(zip_path, 
    'r') as zip_ref:
        zip_ref.extractall(os.path.expanduser("~")) 
    print("\nSystem vom Link geladen!")
def main(): os.system("clear") print(LOGO) 
    print("1) new account") print("2) from 
    link") choice = input("\nchoose from: ") 
    if choice == "1":
        new_account() elif choice == "2": 
        from_link()
    else: print("Ungültige Auswahl!") if 
__name__ == "__main__":
    main()
