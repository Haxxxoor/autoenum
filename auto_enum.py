import os
import subprocess

def is_pingable(ip):
    # Check if the IP address is pingable
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

def run_nmap(ip):
    # Open a new xterm window and run nmap with -sC and -sV flags
    subprocess.Popen(['xterm', '-hold', '-e', f'nmap -sC -sV {ip}'])

def run_nmap_all_ports(ip):
    # Open a new xterm window and run nmap with -p- flag to scan all ports
    subprocess.Popen(['xterm', '-hold', '-e', f'nmap -p- {ip}'])

def run_gobuster(ip):
    # Open a new xterm window and run gobuster with the specified wordlist
    wordlist = "/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt"
    subprocess.Popen(['xterm', '-hold', '-e', f'gobuster dir -u http://{ip} -w {wordlist}'])

def run_gobuster_dns(ip):
    # Open a new xterm window and run gobuster dns with the updated wordlist
    dns_wordlist = "/usr/share/wordlists/amass/subdomains-top1mil-110000.txt"
    subprocess.Popen(['xterm', '-hold', '-e', f'gobuster dns -d {ip} -w {dns_wordlist}'])

def run_gobuster_with_extensions(ip):
    # Open a new xterm window and run gobuster with -x flag for extensions and a new wordlist
    wordlist = "/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt"
    extensions = "html,txt,php,js,py"
    subprocess.Popen(['xterm', '-hold', '-e', f'gobuster dir -u http://{ip} -w {wordlist} -x {extensions}'])

def main(ip):
    if is_pingable(ip):
        print(f"{ip} is pingable, running nmap (default), nmap (all ports), gobuster (directory), gobuster (DNS), and gobuster (with extensions).")
        run_nmap(ip)                     # Default nmap scan
        run_nmap_all_ports(ip)            # Nmap scan for all ports
        run_gobuster(ip)                  # Gobuster directory scan
        run_gobuster_dns(ip)              # Gobuster DNS subdomain scan
        run_gobuster_with_extensions(ip)  # Gobuster with file extensions scan
    else:
        print(f"{ip} is not pingable.")

if __name__ == "__main__":
    # Replace this with the IP address or domain you want to check
    target_ip = input("Enter the target IP address or domain: ")
    main(target_ip)
