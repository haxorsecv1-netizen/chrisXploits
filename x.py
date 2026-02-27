import os
import subprocess
import time
from colorama import Fore
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.style import Style
from rich.text import Text
from tabulate import tabulate
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.box import SIMPLE

# Initialize Rich Console
console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message, duration=2):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(description=message, total=duration * 10)
        for _ in range(duration * 10):  # Loop for duration seconds
            time.sleep(0.1)
            progress.update(task, advance=1)
        progress.stop()
        console.print(f"[green]{message} - Done!")

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            unique_lines = set(file.readlines())
        with open(output_file, 'w') as file:
            file.writelines(unique_lines)
        console.print(f"[green]Duplicate entries removed. Output saved to {output_file}")
    except Exception as e:
        console.print(f"[red]Error: {e}")

def run_exe(exe_path):
    # Simpan direktori saat ini
    original_dir = os.getcwd()

    # Ubah direktori ke folder tempat 'rev.exe' berada (folder 'tools')
    os.chdir(os.path.dirname(exe_path))

    try:
        subprocess.run([os.path.basename(exe_path)], check=True)
    finally:
        os.chdir(original_dir)

def run_script(script_name, cwd, args=None):
    try:
        args = args or []
        script_path = os.path.join(cwd, script_name)
        subprocess.run(['python', script_path] + args, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error running script {script_name}: {e}")

def print_menu():
    """Print the main menu in a table format."""
    clear_screen()
    console.print(Panel(Text("coded by: t.me/chrisnewbot", style="bold white"), style="on blue"))
    
    # Define menu items in a structured format
    main_menu = [
        ["1", "Shell Finder"],
        ["2", "Splitter+Auto Run"],
        ["3", "Cpanel & FTP Scanner"],
        ["4", "Perlalfa scan+Auto upload"],
        ["5", "Phpunit scan+Auto upload"],
        ["6", "WP-CVE-2023-5630 scan+Auto upload"],
        ["7", "Subfinder V2[UPDATED]"],
    ]
    grabber_menu = [
        ["8", "Grab By Ext[UPDATED]"],
        ["9", "Zone Xsec Grabber"],
        ["10", "Haxorid Grabber"],
        ["11", "Grabber By KeyWord"],
        ["12", "Grabber By Page V1"],
        ["13", "Grabber By A-Z 0-9"],
        ["14", "Grab Domain Per Sec"],
        ["15", "Grabber By Page V2"],
        ["16", "Grabber By Angka"],
    ]
    other_menu = [
        ["17", "Mass Subdomain Finder"],
        ["18", "FREE REVERSE IP[UPDATE]"],
        ["19", "CMS Scanner"],
        ["20", "Remove Duplicate"],
        ["21", "Brute Force Password Webshell"],
        ["22", "Cpanel Checker"],
        ["23", "RCE CyberPanel"],
        ["24", "PHPINFO checker[NEW]"],
        ["25", "parameter scanner[NEW]"],
        ["26", "DA PA CHECKER[NEW]"],
    ]
    all_menus = main_menu + grabber_menu + other_menu
    max_description_length = max(len(item[1]) for item in all_menus)
    
    # Function to add color to [NEW] and [UPDATED]
    def add_color_to_tags(menu):
        for item in menu:
            if "[NEW]" in item[1]:
                item[1] = item[1].replace("[NEW]", Text("[NEW]", style="bold red"))
            if "[UPDATED]" in item[1]:
                item[1] = item[1].replace("[UPDATED]", Text("[UPDATED]", style="bold red"))
        return menu

    def pad_descriptions(menu):
        return [[item[0], item[1].ljust(max_description_length)] for item in menu]
    
    main_menu = pad_descriptions(main_menu)
    grabber_menu = pad_descriptions(grabber_menu)
    other_menu = pad_descriptions(other_menu)
    
    console.print("\n[bold red]  MAIN MENU[/bold red]")
    console.print(tabulate(main_menu, headers=["NO", "TOOLS NAME "], tablefmt="fancy_grid"))
    console.print("\n[bold green]  GRABBER MENU[/bold green]")
    console.print(tabulate(grabber_menu, headers=["NO", "TOOLS NAME                     "], tablefmt="fancy_grid"))
    console.print("\n[bold yellow]  OTHER MENU[/bold yellow]")
    console.print(tabulate(other_menu, headers=["NO", "TOOLS NAME                     "], tablefmt="fancy_grid"))

def main_menu():
    """Main menu loop."""
    while True:
        print_menu()
        choice = Prompt.ask("PILIH MENU")
        if choice == '1':
            current_directory = os.path.dirname(os.path.abspath(__file__))
            tools_directory = os.path.join(current_directory, 'tools')
            rsf_script = os.path.join(tools_directory, 'rsf.py')
            file_name = input("list: ")
            file_path = os.path.join(current_directory, file_name)
            if os.path.isfile(rsf_script) and os.path.isfile(file_path):
                subprocess.run(['python', rsf_script, file_path], cwd=tools_directory)
            else:
                console.print(Fore.RED + "list not found")
        elif choice == '2':
            run_script('split.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '3':
            run_script('config.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '4':
            run_script('perlalfa.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '5':
            run_script('phpunit.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '6':
            run_script('wp.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '7':
            try:
                subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"], check=True)
            except subprocess.CalledProcessError:
                console.print(Fore.RED + "Golang belum terinstal. Silahkan instal Golang terlebih dahulu.")
                exit()

            list_name = input("Masukkan nama list: ")
            output_name = input("Masukkan nama output: ")

            max_per_file = int(input("maksimum domain per file: "))

            with open(list_name, 'r') as f:
                domains = f.readlines()

            split_files = []
            for i in range(0, len(domains), max_per_file):
                split_file_name = f"split_{i // max_per_file + 1}.txt"
                with open(split_file_name, 'w') as split_file:
                    split_file.writelines(domains[i:i+max_per_file])
                split_files.append(split_file_name)

            # Menjalankan subfinder untuk setiap split file
            for split_file in split_files:
                cmd = f'start cmd /c subfinder -dL {split_file} -o {output_name}'
                os.system(cmd)

            console.print(Fore.GREEN + "Proses selesai, semua output disimpan dalam file: " + output_name)
        elif choice == '8':
            run_script('grab1.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '9':
            run_script('zonexsec.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '10':
            run_script('haxorid.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '11':
            run_script('grab2.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '12':
            run_script('grab3.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '13':
            run_script('grab4.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '14':
            run_script('grab5.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '15':
            run_script('grab6.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '16':
            run_script('grab7.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '17':
            run_script('subfind.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '18':
            run_exe('tools/rev.exe')
        elif choice == '19':
            run_script('cmsscan.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '20':
            input_file = input("Input file: ")
            output_file = input("Output file: ")
            remove_duplicates(input_file, output_file)
        elif choice == '21':
            run_script('bfpass.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '22':
            run_script('cpcheck.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '23':
            file_name = input("list: ")
            command = input("command: ")
            run_script('rce.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'),
                       args=['-f', file_name, '-o', "RCE.txt", '-t', "5"] + command.split())
        elif choice == '24':
            current_directory = os.path.dirname(os.path.abspath(__file__))
            tools_directory = os.path.join(current_directory, 'tools')
            rsf_script = os.path.join(tools_directory, 'phpinfo.py')
            file_name = input("list: ")
            file_path = os.path.join(current_directory, file_name)
            if os.path.isfile(rsf_script) and os.path.isfile(file_path):
                subprocess.run(['python', rsf_script, file_path], cwd=tools_directory)
            else:
                console.print(Fore.RED + "list not found")
        elif choice == '25':
            run_script('extrak.py', cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
        elif choice == '26':
            run_exe('tools/metrics.exe')
        else:
            print(Fore.RED + "Pilihan tidak valid.")
            print(Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()