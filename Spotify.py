class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
        print(f"{song} added!")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song}' not found in playlist.")
    def display(self):
        print("Songs:", self.songs)
    def details(self):
        print("Name:", self.name)
        print("Genre:", self.genre)
    def __del__(self):
        print("Playlist deleted!")
p = Playlist("My Playlist", "Pop")
while True:
    print("\n1. Add song")
    print("2. Remove song")
    print("3. Display songs")
    print("4. Playlist details")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        p.add_song(input("Enter song: "))
    elif choice == "2":
        p.remove_song(input("Enter song: "))
    elif choice == "3":
        p.display()
    elif choice == "4":
        p.details()
    elif choice == "5":
        del p
        break
    else:
        print("Invalid choice!")
