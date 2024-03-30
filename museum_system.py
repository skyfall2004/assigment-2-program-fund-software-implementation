from classes.manage_artworks import ArtworkManager
from classes.manage_exhibitions import ExhibitionManager
from classes.manage_artifacts import ArtifactManager
from classes.manage_visitors import VisitorManager
from classes.manage_tickets_and_pricing import TicketManager
from classes.artwork import Artwork
from classes.exhibition import Exhibition
from classes.artifact import Artifact
from classes.visitor import Visitor


class MuseumSystem:
    def __init__(self):
        # Initialize admin credentials and login status
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.logged_in = False
        self.artwork_manager = ArtworkManager()
        self.exhibition_manager = ExhibitionManager()
        self.artifact_manager = ArtifactManager()
        self.visitor_manager = VisitorManager()
        self.ticket_manager = TicketManager()

    # Handle Login for Administrator 
    def login(self, username, password):
        # Method to log in as admin
        if username == self.admin_username and password == self.admin_password:
            print("Logged in successfully as admin.")
            self.logged_in = True
        else:
            print("Invalid username or password.")

    # Display the main menu
    def display_menu(self):
        # Display main menu options
        print("Welcome to the Louvre Museum System")
        print("1. Admin Login")
        print("2. Exit")

    # Display main menu options
    def display_admin_menu(self):
        # Display admin menu options
        print("\nAdmin Menu:")
        print("1. Manage Artworks")
        print("2. Manage Exhibitions")
        print("3. Manage Artifacts")
        print("4. Manage Visitors")
        print("5. Manage Tickets and Pricing")
        print("6. Logout")

    # Manage Artwork
    def manage_artworks(self):
        while True:
            print("\nArtwork Management:")
            print("1. Add Artwork")
            print("2. Remove Artwork")
            print("3. Display Artworks")
            print("4. Go back to main menu")

            option = input("Enter your choice: ")

            if option == "1":
                # Add few record for testing 
                artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Iconic portrait", "Permanent galleries")
                artwork2 = Artwork("The Starry Night", "Vincent van Gogh", "1889", "Depicts van Gogh's view from the asylum", "Permanent galleries")
                artwork3 = Artwork("The Thinker", "Auguste Rodin", "1880", "Represents philosophy", "Outdoor spaces")

                self.artwork_manager.add_artwork(artwork1)
                self.artwork_manager.add_artwork(artwork2)
                self.artwork_manager.add_artwork(artwork3)
                # Insert new artwork
                title = input("Enter artwork title: ")
                artist = input("Enter artist name: ")
                date_of_creation = input("Enter date of creation: ")
                historical_significance = input("Enter historical significance: ")
                location = input("Enter location: ")

                artwork = Artwork(title, artist, date_of_creation, historical_significance, location)
                self.artwork_manager.add_artwork(artwork)
            elif option == "2":
                title = input("Enter title of the artwork to remove: ")
                self.artwork_manager.remove_artwork(title)
            elif option == "3":
                self.artwork_manager.display_all_artworks()
            elif option == "4":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # Manage Exhibitions
    def manage_exhibitions(self):
        # Placeholder method for managing exhibitions
        while True:
            print("\nExhibition management:")
            print("1. Add Exhibition")
            print("2. Remove Exhibition")
            print("3. Display Exhibitions")
            print("4. Go back to main menu")

            option = input("Enter your choice: ")

            if option == "1":
                # Add few record for testing 
                exhibition1 = Exhibition("Renaissance Art", "2 weeks", "Gallery 1")
                exhibition2 = Exhibition("Modern Art", "1 month", "Gallery 2")

                self.exhibition_manager.add_exhibition(exhibition1)
                self.exhibition_manager.add_exhibition(exhibition2)
                # Insert new exhibition
                name = input("Enter exhibition name: ")
                duration = input("Enter exhibition duration: ")
                location = input("Enter location: ")

                exhibition = Exhibition(name, duration, location)
                self.exhibition_manager.add_exhibition(exhibition)
            elif option == "2":
                name = input("Enter name of the exhibition to remove: ")
                self.exhibition_manager.remove_exhibition(name)
            elif option == "3":
                self.exhibition_manager.display_all_exhibitions()
            elif option == "4":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # Manage Artifacts
    def manage_artifacts(self):
        # Placeholder method for managing artifacts
        while True:
            print("\nArtifacts Management:")
            print("1. Add Artifact")
            print("2. Remove Artifact")
            print("3. Display Artifacts")
            print("4. Go back to main menu")

            option = input("Enter your choice: ")

            if option == "1":
                # Add few record for testing 
                artifact1 = Artifact("Stone Axe", "A tool used by early humans", "Significant in human history", "Permanent galleries")
                artifact2 = Artifact("Roman Coin", "Currency used in ancient Rome", "Reflects Roman economy", "Exhibition halls")

                self.artifact_manager.add_artifact(artifact1)
                self.artifact_manager.add_artifact(artifact2)
                # Insert new exhibition
                name = input("Enter artifact name: ")
                description = input("Enter description: ")
                historical_significance = input("Enter historical significance: ")
                location = input("Enter location: ")

                artifact = Artifact(name, description, historical_significance, location)
                self.artifact_manager.add_artifact(artifact)

            elif option == "2":
                name = input("Enter name of the artifact to remove: ")
                self.artifact_manager.remove_artifact(name)
            elif option == "3":
                self.artifact_manager.display_all_artifacts()
            elif option == "4":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # Manahe Visitors
    def manage_visitors(self):
        print("\nVisitor management options:")
        print("1. Add Visitor")
        print("2. Remove Visitor")
        print("3. Display All Visitors")
        print("4. Go Back")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter visitor's name: ")
                age = int(input("Enter visitor's age: "))
                ticket_type = input("Enter ticket type (Exhibition/Tour/Special Event): ")
                event_details = input("Enter event details: ")
                visitor = Visitor(name, age, ticket_type, event_details)
                self.visitor_manager.add_visitor(visitor)
            elif choice == "2":
                name = input("Enter visitor's name to remove: ")
                self.visitor_manager.remove_visitor(name)
            elif choice == "3":
                self.visitor_manager.display_all_visitors()
            elif choice == "4":
                print("Going back to the main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # Manage tickets and pricing information
    def manage_tickets_and_pricing(self):

        print("\nTicket and pricing management options:")
        print("1. Purchase Ticket")
        print("2. Go Back")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                visitor_type = input("Enter visitor type (Adult/Child/Teacher/Student/Senior/Group/Special Event): ")
                self.ticket_manager.purchase_ticket(visitor_type)
            elif choice == "2":
                print("Going back to the main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def run(self):
        # Main execution loop
        while True:
            self.display_menu()  # Display main menu
            choice = input("Enter your choice: ")  # Get user input

            if choice == "1":
                # Admin login
                if not self.logged_in:
                    username = input("Enter admin username: ")
                    password = input("Enter admin password: ")
                    self.login(username, password)
                else:
                    print("Already logged in as admin.")
            elif choice == "2":
                # Exit the system
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

            while self.logged_in:
                # Admin menu loop
                self.display_admin_menu()  # Display admin menu
                admin_choice = input("Enter your choice: ")  # Get admin choice

                if admin_choice == "1":
                    self.manage_artworks()  # Manage artworks
                elif admin_choice == "2":
                    self.manage_exhibitions()  # Manage exhibitions
                elif admin_choice == "3":
                    self.manage_artifacts()  # Manage artifacts
                elif admin_choice == "4":
                    self.manage_visitors()  # Manage visitors
                elif admin_choice == "5":
                    self.manage_tickets_and_pricing()  # Manage tickets and pricing
                elif admin_choice == "6":
                    print("Logging out.")
                    self.logged_in = False  # Logout
                else:
                    print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    museum_system = MuseumSystem()
    museum_system.run()
