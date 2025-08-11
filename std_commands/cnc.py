# desc: create new command
import os def main(): name = input("name: ") 
    desc = input("description: ") filename = 
    input("file name: ") path = 
    os.path.expanduser(f"~/commands/{filename}.py") 
    with open(path, "w") as f:
        f.write(f"# desc: {desc}\n") 
        f.write("print('Command 
        running...')\n")
    os.chmod(path, 0o755) print(f"Command 
    '{name}' erstellt unter {path}")
if __name__ == "__main__":
    main()
