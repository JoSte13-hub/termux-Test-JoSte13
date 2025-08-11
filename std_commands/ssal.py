# desc: save system as link
import os, zipfile, http.server, 
socketserver, threading def zipdir(path, 
ziph):
    for root, dirs, files in os.walk(path): 
        for file in files:
            ziph.write(os.path.join(root, 
            file),
                       os.path.relpath(os.path.join(root, 
                       file), 
                       os.path.join(path, 
                       '..')))
def main():
    # Passwort abfragen
    from importlib.machinery import 
    SourceFileLoader user = 
    SourceFileLoader("user", 
    os.path.expanduser("~/user/user.py")).load_module() 
    pw = input("Password: ") if pw != 
    user.password:
        print("Falsches Passwort!") return 
    zip_path = 
    os.path.expanduser("~/downloads/system.zip") 
    with zipfile.ZipFile(zip_path, 'w', 
    zipfile.ZIP_DEFLATED) as zipf:
        zipdir(os.path.expanduser("~"), zipf) 
    print(f"System gespeichert unter 
    {zip_path}") print("Apache muss manuell 
    konfiguriert werden, um es hochzuladen.")
if __name__ == "__main__":
    main()
