class TicketManager:
    VAT_RATE = 0.05  # VAT rate

    def __init__(self):
        self.ticket_prices = {
            "Adult": 63,
            "Child": 0,
            "Teacher": 0,
            "Student": 0,
            "Senior": 0,
            "Group": 0,
            "Special Event": {
                "Musical Concert": 100,
                "Light Show": 80,
                "Fundraising": 120
            }
        }

    def calculate_ticket_price(self, visitor_type):
        if visitor_type in self.ticket_prices:
            if visitor_type == "Group":
                return self.ticket_prices["Adult"] * 0.5  # 50% discount for groups
            elif visitor_type == "Special Event":
                print("Available special events:")
                for event, price in self.ticket_prices[visitor_type].items():
                    print(f"{event}: {price} AED")
                event_choice = input("Enter the event choice: ")
                if event_choice in self.ticket_prices[visitor_type]:
                    return self.ticket_prices[visitor_type][event_choice]
                else:
                    print("Invalid event choice.")
                    return None
            else:
                return self.ticket_prices[visitor_type]
        else:
            print("Invalid visitor type.")
            return None

    def apply_vat(self, price):
        return price * (1 + self.VAT_RATE)  # Applying VAT

    def purchase_ticket(self, visitor_type):
        ticket_price = self.calculate_ticket_price(visitor_type)
        if ticket_price is not None:
            if ticket_price == 0:
                print("Ticket is free.")
            else:
                ticket_price_with_vat = self.apply_vat(ticket_price)
                print(f"Ticket price (including VAT): {ticket_price_with_vat:.2f} AED")
