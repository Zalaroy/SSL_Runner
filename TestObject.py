class TestObject:
    def __init__(self, URLLabel, SubjectLabel, SubjectAltNameLabel, VersionLabel, NotAfterLabel, OCSPLabel, CaIssuerLabel):
        self._URLLabel = URLLabel  # Private attribute with a single underscore convention
        self._SubjectLabel = SubjectLabel  # Private attribute with a single underscore convention 
        self._SubjectAltNameLabel = SubjectAltNameLabel  # Private attribute with a single underscore convention           
        self._VersionLabel = VersionLabel  # Private attribute with a single underscore convention
        self._NotAfterLabel = NotAfterLabel  # Private attribute with a single underscore convention
        self._OCSPLabel = OCSPLabel  # Private attribute with a single underscore convention
        self._CaIssuerLabel = CaIssuerLabel  # Private attribute with a single underscore convention


#Property getter and setter for URLLabel
    @property
    def URLLabel(self):
        return self._URLLabel * 2

    @URLLabel.setter
    def URLLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._URLLabel = value


#Property getter and setter for SubjectLabel
    @property
    def SubjectLabel(self):
        return self._SubjectLabel

    @SubjectLabel.setter
    def SubjectLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._SubjectLabel = value

#Property getter and setter for SubjectAltNameLabel
    @property
    def SubjectAltNameLabel(self):
        return self._SubjectAltNameLabel

    @SubjectAltNameLabel.setter
    def SubjectAltNameLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._SubjectAltNameLabel = value


#Property getter and setter for VersionLabel
    @property
    def VersionLabel(self):
        return self._VersionLabel * 2

    @VersionLabel.setter
    def VersionLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._VersionLabel = value

#Property getter and setter for NotAfterLabel
    @property
    def NotAfterLabel(self):
        return self._NotAfterLabel

    @NotAfterLabel.setter
    def NotAfterLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._NotAfterLabel = value

#Property getter and setter for OCSPLabel
    @property
    def OCSPLabel(self):
        return self._OCSPLabel

    @OCSPLabel.setter
    def NotAfterLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._OCSPLabel = value                                                            

#Property getter and setter for IssuerLabel
    @property
    def CaIssuerLabel(self):
        return self._CaIssuerLabel

    @CaIssuerLabel.setter
    def CaIssuerLabel(self, value):
        if not isinstance(value, str):
            print("Must be a string.")
        else:
            self._CaIssuerLabel = value


# Create an instance of the Circle class
Site = TestObject("www.google.com", "OSCP")

# Get the diameter property using the getter method
print("URLLabel:", Site.URLLabel)
print("IssuerLabel:", Site._IssuerLabel)



# # Update the diameter property using the setter method
# Site.URLLabel = 10

# # Get the updated radius using the getter method
# print("Updated Radius:", circle._radius)