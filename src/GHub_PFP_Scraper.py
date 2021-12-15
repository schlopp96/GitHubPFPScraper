#/usr/bin/env python3

#> Small script that opens github profile pictures associated with the entered username.
#@ Based off of http://freecodecamp.org/ tutorial video: https://youtu.be/SqvVm3QiQVk?t=37

#import PySimpleGUI as sg
from time import sleep as s
from webbrowser import open as open_window
from requests import get
from loadingSequence import load
from bs4 import BeautifulSoup as bs


def profile_search(username: str) -> bool:
    """
    Small script that opens the profile-picture of the entered Github username within your default browser.

    - If there is already a browser window opened, the image will be loaded as a new tab within the window.

    :param username: username of the GitHub profile to search for.
    :type username: str
    :return: Opens found profile picture in user's default browser as a new window, or as a new tab if there is already a window open.
    :rtype: Any
    """

    try:
        url = f'https://github.com/{username}'
        gh_profile = get(url)
        #:NOTE - #* "content" represents all data contained within an html response.
        soup = bs(gh_profile.content, 'html.parser')
        #:NOTE - #? Finds info by inspecting profile picture element in my browser.
        profile_img: str = soup.find('img', {'alt': 'Avatar'})['src']

        #:NOTE - #!Open found prof-pic in browser:
        load(
            f'\nOpening {username}\'s Github profile picture: "{profile_img}"', 'Ok!\n'
        )
        return open_window(profile_img, 2)

    except TypeError:
        print(
            f'\n\t~   ERROR   ~\nUnable to find user "{username}" profile.\n\nPlease try again.\n'
        )
        s(1.2)
        return False


def main():
    """
    Program function wrapper.

    - NOT MEANT TO BE CALLED MANUALLY!schlopp
    - Enter "exit" to close program when prompted for username.
    - Prints "how-to-exit" reminders every 3rd entry.

    :return: Primary flow of program.
    :rtype: NoReturn
    """
    searchCount: int = 0

    while True:
        if searchCount % 3 == 0:
            print(
                '\nNote:\nYou may enter "Exit" at any point to close application.\n'
            )
        profile: str = input('Enter a GitHub username:\n-> ')
        if profile.lower() == 'exit':
            break
        profile_search(profile)
        searchCount += 1
    exit()


if __name__ == '__main__':
    main()
