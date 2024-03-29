class ArtworkManager:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print("Artwork added successfully.")

    def remove_artwork(self, artwork_title):
        for artwork in self.artworks:
            if artwork.title == artwork_title:
                self.artworks.remove(artwork)
                print(f"Artwork '{artwork_title}' removed successfully.")
                return
        print(f"Artwork '{artwork_title}' not found.")

    # Display all the artworks 
    def display_all_artworks(self):
        if not self.artworks:
            print("No artworks in the collection.")
        else:
            print("All Artworks:")
            for artwork in self.artworks:
                print("Title:", artwork.title)
                print("Artist:", artwork.artist)
                print("Date of Creation:", artwork.date_of_creation)
                print("Historical Significance:", artwork.historical_significance)
                print("Location:", artwork.location)
                print("--------------------")