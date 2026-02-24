#!/data/data/com.termux/files/usr/bin/bash
# INSTALLER WIFI HACK TOOL - TERMUX
# Copy paste semua kode ini ke file install.sh

clear
echo "╔══════════════════════════════════════╗"
echo "║    INSTALLER WIFI HACK TOOL         ║"
echo "║         FOR TERMUX ANDROID           ║"
echo "╚══════════════════════════════════════╝"
echo ""

echo "[*] Mengupdate package Termux..."
pkg update -y && pkg upgrade -y

echo "[*] Menginstall tools yang diperlukan..."
pkg install -y python python2
pkg install -y git
pkg install -y wget
pkg install -y nmap
pkg install -y root-repo
pkg install -y tsu
pkg install -y aircrack-ng

echo "[*] Menginstall module Python..."
pip install requests
pip install scapy
pip install colorama

echo "[*] Membuat folder untuk wordlist..."
mkdir -p ~/wordlists

echo "[*] Download wordlist sederhana..."
cd ~/wordlists
wget -O wordlist.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt

echo ""
echo "[✓] INSTALASI SELESAI!"
echo ""
echo "Cara menjalankan:"
echo "python wifi-hack.py"
echo ""
echo "Catatan: Untuk fitur monitor mode, jalankan dengan:"
echo "tsu python wifi-hack.py"