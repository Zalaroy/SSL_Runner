import ssl, socket, sys, tkinter, json
from tkinter import *
from SSLSite import *

propertyHashMap = {}


def gui1():
    main_window = Tk() 

    #To do: add feature where multiple websites can be added#
    URLLabel = Label(main_window, text = " URL ").grid(row = 0, column = 0)
    
    SubjectLabel = Label(main_window, text = " subject ")
    SubjectLabel.grid(row = 0, column = 2)
    SubjectValue = Label(main_window, text = propertyHashMap['subject'])
    SubjectValue.grid(row = 1, column = 2)

    IssuerLabel = Label(main_window, text = " issuer ")
    IssuerLabel.grid(row = 0, column = 3)
    # IssuerValue = Label(main_window, text = keyValReturn(dict, "issuer"))
    # IssuerValue.grid(row = 1, column = 3)

    VersionLabel = Label(main_window, text = " version ")
    VersionLabel.grid(row = 0, column = 4)
    # VersionValue = Label(main_window, text = keyValReturn(dict, "version"))
    # VersionValue.grid(row = 1, column = 4)

    serialNumberLabel = Label(main_window, text = " serialNumber ")
    serialNumberLabel.grid(row = 0, column = 5)
    # serialNumberValue = Label(main_window, text = keyValReturn(dict, "serialNumber"))
    # serialNumberValue.grid(row = 1, column = 5)

    notBeforeLabel = Label(main_window, text = " notBefore ")
    notBeforeLabel.grid(row = 0, column = 6)
    # notBeforeValue = Label(main_window, text = keyValReturn(dict, "notBefore"))
    # notBeforeValue.grid(row = 1, column = 6)

    notAfterLabel = Label(main_window, text = " notAfter ")
    notAfterLabel.grid(row = 0, column = 7)
    # notAfterValue = Label(main_window, text = keyValReturn(dict, "notAfter"))
    # notAfterValue.grid(row = 1, column = 7)

    subjectAltNameLabel = Label(main_window, text = " subjectAltName ")
    subjectAltNameLabel.grid(row = 0, column = 8)
    # SubjectAltNameValue = Label(main_window, text = keyValReturn(dict, "subjectAltName"))
    # SubjectAltNameValue.grid(row = 1, column = 8)

    OCSPLabel = Label(main_window, text = " OCSP ")
    OCSPLabel.grid(row = 0, column = 9)
    # OCSPValue = Label(main_window, text = keyValReturn(dict, "OSCP"))
    # OCSPValue.grid(row = 1, column = 9)

    caIssuerLabel = Label(main_window, text = " caIssuer ")
    caIssuerLabel.grid(row = 0, column = 10)
    # caIssuerValue = Label(main_window, text = keyValReturn(dict, "caIssuer"))
    # caIssuerValue.grid(row = 1, column = 10)

    crlDistributionPointsLabel = Label(main_window, text = " crlDistributionPoints ")
    crlDistributionPointsLabel.grid(row = 0, column = 11)
    # crlDistributionPointsValue = Label(main_window, text = keyValReturn(dict, "crlDistributionPoints"))
    # crlDistributionPointsValue.grid(row = 1, column = 11)

    URLField = Entry(main_window, width = 25, text="URL: ")
    URLField.grid(row = 2, column = 0)          
   
    URLButton = Button(text = "Analyze URL", command = lambda: URLEntryOnClick(URLField.get()))
    URLButton.grid(row = 2, column = 1)
    print("URL Submitted: " , URLField.get())
    main_window.mainloop()

def URLEntryOnClick(URLField):      
    global propertyHashMap
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname = URLField) as s:
        s.connect((URLField, 443))
        results = json.dumps(s.getpeercert(), indent = 4)
        parsed = json.loads(results)
        propertyHashMap.update({"URL" : URLField})
        propertyHashMap.update({"Subject" : parsed['subject']})
        propertyHashMap.update({"Issuer" : parsed['issuer']})
        propertyHashMap.update({"Version" : parsed['version']})
        propertyHashMap.update({"Serial Number" : parsed['serialNumber']})
        propertyHashMap.update({"Not Before" : parsed['notBefore']})
        propertyHashMap.update({"Not After" : parsed['notAfter']})
        propertyHashMap.update({"Subject Alt Name" : parsed['subjectAltName']})
        propertyHashMap.update({"OCSP" : parsed['OCSP']})
        propertyHashMap.update({"caIssuers" : parsed['caIssuers']})

       
        # print("URL: ", str(URLField))
        # print("Subject: ", str(parsed['subject']))
        # print("Issuer: ", str(parsed['issuer']))
        # print("Version: ", str(parsed['version']))
        # print("Serial Number: ", str(parsed['serialNumber']))
        # print("Not Before: ", str(parsed['notBefore']))
        # print("Not After: ", str(parsed['notAfter']))
        # print("Subject Alt Name: ", str(parsed['subjectAltName']))
        # print("OCSP: ", str(parsed['OCSP']))
        # print("caIssuers: ", str(parsed['caIssuers']))
        
      


def main():
    gui1()

if __name__ == '__main__':
    main() 