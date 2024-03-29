class ExhibitionManager:
    def __init__(self):
        self.exhibitions = []

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def remove_exhibition(self, name):
        for exhibition in self.exhibitions:
            if exhibition.name == name:
                self.exhibitions.remove(exhibition)
                print(f"{name} exhibition has been removed.")
                return
        print(f"Exhibition with name '{name}' not found.")

    def display_all_exhibitions(self):
        if not self.exhibitions:
            print("No exhibitions in the collection.")
        else:
            print("All Exhibitions:")
            for exhibition in self.exhibitions:
                print("Name:", exhibition.name)
                print("Duration:", exhibition.duration)
                print("Location:", exhibition.location)
                print("--------------------")