class TestObject:
    def __init__(self, URLLabel, IssuerLabel):
        self._URLLabel = URLLabel  # Private attribute with a single underscore convention
        self._IssuerLabel = IssuerLabel  # Private attribute with a single underscore convention


    @property
    def URLLabel(self):
        return self._URLLabel * 2

    @URLLabel.setter
    def URLLabel(self, value):
        if value >= 0:
            self._URLLabel = value / 2
        else:
            print("Diameter cannot be negative.")

# Create an instance of the Circle class
Site = TestObject("www.google.com", "OSCP")

# Get the diameter property using the getter method
print("URLLabel:", Site.diameter)
print("IssuerLabel:", Site._IssuerLabel)



# # Update the diameter property using the setter method
# Site.URLLabel = 10

# # Get the updated radius using the getter method
# print("Updated Radius:", circle._radius)