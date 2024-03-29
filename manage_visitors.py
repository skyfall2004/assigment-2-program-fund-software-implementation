class VisitorManager:
    def __init__(self):
        self.visitors = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)
        print("Visitor added successfully.")

    def remove_visitor(self, name):
        for visitor in self.visitors:
            if visitor.name == name:
                self.visitors.remove(visitor)
                print(f"{name} has been removed from the visitor list.")
                return
        print(f"Visitor with name '{name}' not found in the list.")

    def display_all_visitors(self):
        if not self.visitors:
            print("No visitors in the list.")
        else:
            print("All Visitors:")
            for visitor in self.visitors:
                print("Name:", visitor.name)
                print("Age:", visitor.age)
                print("Ticket Type:", visitor.ticket_type)
                print("Event Details:", visitor.event_details)
                print("--------------------")