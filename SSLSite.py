class SSLSite:

    def __init__(self, URLLabel, SubjectLabel, IssuerLabel, VersionLabel, SerialNumberLabel, NotBeforeLabel, NotAfterLabel, SubjectAltNameLabel, OCSPLabel, CaIssuerLabel, CrlDistributionPointsLabel):
        self._URLLabel = URLLabel
        self._SubjectLabel = SubjectLabel
        self._IssuerLabel = IssuerLabel
        self._VersionLabel = VersionLabel
        self._SerialNumberLabel = SerialNumberLabel
        self._NotBeforeLabel = NotBeforeLabel
        self._NotAfterLabel = NotAfterLabel
        self._SubjectAltNameLabel = SubjectAltNameLabel
        self._OCSPLabel = OCSPLabel
        self._CaIssuerLabel = CaIssuerLabel
        self._CrlDistributionPointsLabel = CrlDistributionPointsLabel        
    
    @property
    def URLLabel(self):
        return self._URLLabel

    @property
    def SubjectLabel(self):
        return self._SubjectLabel
    @property
    def IssuerLabel(self):
        return self._IssuerLabel

    @property
    def VersionLabel(self):
        return self._VersionLabel

    @property
    def SerialNumberLabel(self):
        return self._SerialNumberLabel

    @property
    def NotBeforeLabel(self):
        return self._NotBeforeLabel

    @property
    def NotAfterLabel(self):
        return self._NotAfterLabel

    @property
    def SubjectAltNameLabel(self):
        return self._SubjectAltNameLabel

    @property
    def OCSPLabel(self):
        return self._OCSPLabel

    @property
    def CaIssuerLabel(self):
        return self._CaIssuerLabel

    @property
    def CrlDistributionPointsLabel(self):
        return self._CrlDistributionPointsLabel
        
    # Setter methods
    @URLLabel.setter
    def SetURLLabel(self, value):
        if isinstance(value, str):
            self._URLLabel = value
        else:
            raise ValueError("Must be a string")

    @SubjectLabel.setter
    def SetSubjectLabel(self, value):
        if isinstance(value, str):
            self._SubjectLabel = value
        else:
            raise ValueError("Must be a string")

    @IssuerLabel.setter
    def SetIssuerLabel(self, value):
        if isinstance(value, str):
            self._IssuerLabel = value
        else:
            raise ValueError("Must be a string")

    @VersionLabel.setter
    def SetVersionLabel(self, value):
        if isinstance(value, int):
            self._VersionLabel = value
        else:
            raise ValueError("Must be an int")
   
    @SerialNumberLabel.setter
    def SetSerialNumberLabel(self, value):
        if isinstance(value, int):
            self._SerialNumberLabel = value
        else:
            raise ValueError("Must be an int")   

    @NotBeforeLabel.setter
    def SetNotBeforeLabel(self, value):
        if isinstance(value, int):
            self._NotBeforeLabel = value
        else:
            raise ValueError("Must be an int")
    
    @NotAfterLabel.setter
    def SetNotAfterLabel(self, value):
        if isinstance(value, int):
            self._NotAfterLabel = value
        else:
            raise ValueError("Must be a int")

    @OCSPLabel.setter
    def SetOCSPLabel(self, value):
        if isinstance(value, str):
            self._OCSPLabel = value
        else:
            raise ValueError("Must be a string")
        
    @CaIssuerLabel.setter
    def SetCaIssuerLabel(self, value):
        if isinstance(value, str):
            self._CaIssuerLabel = value
        else:
            raise ValueError("Must be a string") 

    @CrlDistributionPointsLabel.setter
    def CrlDistributionPointsLabel(self, value):
        if isinstance(value, str):
            self._CrlDistributionPointsLabel = value
        else:
            raise ValueError("Label must be a string")               


# Example usage:
# Site = SSLSite()
# print(Site.URLLabel())  
print("objcet passed")  
# # Using setters to update properties
# person.first_name = "Jane"
# person.last_name = "Smith"
# print(person.full_name())  # Output: Jane Smith
