#!/data/data/com.termux/files/usr/bin/bash
echo "=== Termux System Installer ===" pkg 
update -y
pkg install -y apache2 python python2 python3 unzip zip
# Verzeichnisse erstellen
mkdir -p $HOME/commands
mkdir -p $HOME/user 
mkdir -p $HOME/downloads
# Standardbefehle kopieren
cp std_commands/* $HOME/commands/
chmod +x $HOME/commands/*.py
# Startskript ins Home kopieren
cp start.py $HOME/start.py
chmod +x $HOME/start.py
# Prompt setzen
BASHRC="$HOME/.bashrc"
if ! grep -q "JoSte13" "$BASHRC"; then 
cat << 'EOF' >> $BASHRC
# Dynamischer Prompt mit Username aus user.py
if [ -f "$HOME/user/user.py" ]; then 
    USERNAME=$(python3 -c "import sys; 
    sys.path.insert(0, '$HOME/user'); import 
    user; print(user.username)")
else USERNAME="unknown" fi export 
PS1="\[\e[32m\]┌──(\[\e[34m\]$USERNAME@JoSte13\[\e[32m\])─[\[\e[37m\]\w\[\e[32m\]]\n\[\e[32m\]└─\[\e[34m\]$\[\e[0m\] 
" EOF fi
# Apache2 starten
apachectl start echo echo "Installation 
abgeschlossen!"
echo "Starte mit: python3 ~/start.py"
