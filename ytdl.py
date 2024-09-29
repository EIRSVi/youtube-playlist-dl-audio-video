import subprocess
import os
import pyfiglet
from colorama import Fore, Back, Style, init
import time

# Initialize Colorama
init(autoreset=True)

def print_colored_logo():
    # Generate ASCII art for the logo with a modern font
    logo = pyfiglet.figlet_format("SRIEVi", font="slant")

    # Center the logo in the terminal
    terminal_width = os.get_terminal_size().columns
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Colors for the gradient effect (cyber-like appearance)
    colors = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    # Apply a glowing effect to each character in the logo
    print("\n")  # Add spacing before the logo
    for i, char in enumerate(centered_logo):
        if char.strip():  # Apply color only to non-space characters
            print(colors[i % len(colors)] + char, end='', flush=True)
            time.sleep(0.03)  # Slight delay to create a glowing effect
        else:
            print(char, end='', flush=True)
    print("\n")  # New line after the logo

def print_welcome():
    # Call the function to print the colored logo
    print_colored_logo()
    
    # Welcome message
    welcome_message = Fore.LIGHTGREEN_EX + "Welcome to the YouTube Playlist Downloader! \n"
    terminal_width = os.get_terminal_size().columns
    centered_message = welcome_message.center(terminal_width)
    print(centered_message)

    # Updated GitHub and social links
    developer_info = Fore.LIGHTCYAN_EX + "Support us @eirsvi "
    centered_developer = developer_info.center(terminal_width)
    print(centered_developer)

    social_links = Fore.LIGHTMAGENTA_EX + "GitHub | X | YouTube \n"
    centered_social_links = social_links.center(terminal_width)
    print(centered_social_links)

    # Example URL without centering
    example_url = Fore.LIGHTYELLOW_EX + "EXAMPLE PLAYLIST URL:  https://www.youtube.com/playlist?list=PLXYZ123  \n"
    print(example_url)

    print()  # Add an extra newline for spacing

def download_youtube_playlist():
    # Call the welcome message function
    print_welcome()
    
    # Prompt user for the playlist URL
    url = input(Fore.LIGHTCYAN_EX + "Enter the YouTube playlist URL: ")

    # Prompt user to choose between video or audio download
    choice = input(Fore.LIGHTMAGENTA_EX + "Do you want to download (v)ideo only or (a)udio only? (v/a): ").strip().lower()

    # Define base output directory (e.g., ~/Downloads)
    output_dir_base = os.path.expanduser('~/Downloads')

    if choice == 'v':
        # Create a folder to store only videos
        output_dir = os.path.join(output_dir_base, 'YouTube_Videos')
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, '%(title)s.%(ext)s')
        # Command to download the video playlist (only video)
        command = ['yt-dlp', '-f', 'bestvideo+bestaudio/best', '-o', output_file, url]
    elif choice == 'a':
        # Create a folder to store only audios
        output_dir = os.path.join(output_dir_base, 'YouTube_Audios')
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, '%(title)s.%(ext)s')
        # Command to download the audio playlist (audio only as .mp3)
        command = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', output_file, url]
    else:
        print(Fore.RED + "Invalid choice. Please select 'v' for video or 'a' for audio.")
        return

    try:
        # Run the yt-dlp command
        subprocess.run(command, check=True)
        print(Fore.LIGHTGREEN_EX + f"Playlist downloaded successfully to: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error downloading playlist: {e}")

if __name__ == "__main__":
    download_youtube_playlist()
