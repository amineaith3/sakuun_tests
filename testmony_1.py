import instaloader

def download_profil_pic(username):
    try:
        loader = instaloader.Instaloader()
        loader.download_profil(username, profile_pic_only=True)
        print("Profil picture downloaded")

    except instaloader.exceptions.ProfileNotExistsException:
        print("The pic doesn't exist")

username = input("Enter the name")

download_profil_pic(username)
