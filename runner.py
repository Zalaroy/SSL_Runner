import sys
import GUI 
import TestObject
import ssl, socket, sys, tkinter, json

def main():
    #logic to parse command-line arguments
    if len(sys.argv) <= 1:
        raise ValueError("Please provide at least one website to parse, after calling the program name. Specfically, if you want to parse SSL information from more than one site, you must seperate the sites by comma(s). Example: SSL_Info siteX.com,siteY.com,siteZ.com")

    # Split the first argument by commas
    first_arg = sys.argv[1]
    args_list = first_arg.split(',')

    if len(args_list) > 1:
        # If there are multiple items separated by commas, consider them as separate arguments
        for arg in args_list:            
            new_dict = {}
            SSL_Dict = Pull_SSL_Info(arg)
            SSL_Object = TestObject.TestObject(SSL_Dict['subject'], SSL_Dict['subjectAltName'], SSL_Dict['version'], SSL_Dict['notAfter'], SSL_Dict['OCSP'], SSL_Dict['caIssuers'])   
            GUI.gui(SSL_Object._SubjectLabel, SSL_Object._SubjectAltNameLabel, SSL_Object.VersionLabel, SSL_Object.NotAfterLabel, SSL_Object.OCSPLabel, SSL_Object.CaIssuerLabel)        
    elif len(args_list) == 1:        
        SSL_Dict = Pull_SSL_Info(args_list[0])
        SSL_Object = TestObject.TestObject(SSL_Dict['subject'], SSL_Dict['subjectAltName'], SSL_Dict['version'], SSL_Dict['notAfter'], SSL_Dict['OCSP'], SSL_Dict['caIssuers'])   
        GUI.gui(SSL_Object._SubjectLabel, SSL_Object._SubjectAltNameLabel, SSL_Object.VersionLabel, SSL_Object.NotAfterLabel, SSL_Object.OCSPLabel, SSL_Object.CaIssuerLabel) 
    else:
        # If there is something else going on, raise an error
        raise ValueError("major error.")    
    # GUI_Newest.main

def Pull_SSL_Info(URLField):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname = URLField) as s:
        s.connect((URLField, 443))    
        results = json.dumps(s.getpeercert(), indent = 4)
        parsed = json.loads(results)
        return parsed

if __name__ == '__main__':
    main() 