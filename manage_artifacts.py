class ArtifactManager:
    def __init__(self):
        self.artifacts = []

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)

    def remove_artifact(self, name):
        for artifact in self.artifacts:
            if artifact.name == name:
                self.artifacts.remove(artifact)
                print(f"{name} artifact has been removed.")
                return
        print(f"Artifact with name '{name}' not found.")

    def display_all_artifacts(self):
        if not self.artifacts:
            print("No artifacts in the collection.")
        else:
            print("All Artifacts:")
            for artifact in self.artifacts:
                print("Name:", artifact.name)
                print("Description:", artifact.description)
                print("Historical Significance:", artifact.historical_significance)
                print("Location:", artifact.location)
                print("--------------------")