import unittest
from museum_system import ArtworkManager, Exhibition, Artwork, Artifact ,ExhibitionManager, ArtifactManager, VisitorManager, TicketManager, Visitor


class TestMuseumSystem(unittest.TestCase):
    def test_artwork_management(self):
        artwork_manager = ArtworkManager()

        # Test adding new artwork
        artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Iconic portrait", "Permanent galleries")
        artwork_manager.add_artwork(artwork)
        self.assertEqual(len(artwork_manager.artworks), 1)

        # Test removing artwork
        artwork_manager.remove_artwork("Mona Lisa")
        self.assertEqual(len(artwork_manager.artworks), 0)

    def test_exhibition_management(self):
        # Test adding new exhibition
        exhibition_manager = ExhibitionManager()
        exhibition = Exhibition("Renaissance Art", "2 weeks", "Gallery 1")

        exhibition_manager.add_exhibition(exhibition)

        self.assertEqual(len(exhibition_manager.exhibitions), 1)

        # Test removing exhibition
        exhibition_manager.remove_exhibition("Renaissance Art")
        self.assertEqual(len(exhibition_manager.exhibitions), 0)

    def test_artifact_management(self):
        artifact_manager = ArtifactManager()

        # Test adding new artifact
        artifact = Artifact("Stone Axe", "A tool used by early humans", "Significant in human history", "Permanent galleries")

        artifact_manager.add_artifact(artifact)
        self.assertEqual(len(artifact_manager.artifacts), 1)

        # Test removing artifact
        artifact_manager.remove_artifact("Stone Axe")
        self.assertEqual(len(artifact_manager.artifacts), 0)

    def test_visitor_management(self):
        visitor_manager = VisitorManager()
        # Test adding new visitor
        visitor = Visitor("John", 30, "Exhibition", "Renaissance Art")
        visitor_manager.add_visitor(visitor)
        self.assertEqual(len(visitor_manager.visitors), 1)

        # Test removing visitor
        visitor_manager.remove_visitor("John")
        self.assertEqual(len(visitor_manager.visitors), 0)

    def test_ticket_purchasing(self):
        ticket_manager = TicketManager()

        # Test purchasing ticket for an adult
        ticket_manager.purchase_ticket("Adult")

        # Test purchasing ticket for a child (should be free)
        ticket_manager.purchase_ticket("Child")

        # Test purchasing ticket for a special event (musical concert)
        ticket_manager.purchase_ticket("Special Event")


if __name__ == "__main__":
    unittest.main()
