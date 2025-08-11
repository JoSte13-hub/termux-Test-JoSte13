import os COMMANDS_DIR = 
os.path.expanduser("~/commands") def main():
    print("=== Available Commands ===") for 
    file in os.listdir(COMMANDS_DIR):
        if file.endswith(".py"): name = 
            file[:-3] desc = "" desc_path = 
            os.path.join(COMMANDS_DIR, file) 
            try:
                with open(desc_path, "r") as 
                f:
                    for line in f: if 
                        line.startswith("# 
                        desc:"):
                            desc = 
                            line.split(":", 
                            1)[1].strip() 
                            break
            except: pass print(f"{name} - 
            {desc}")
if __name__ == "__main__":
    main()

