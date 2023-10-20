import sys
import GUI_Newest 
import SSLSite
import TestObject
import ssl, socket, sys, tkinter, json

def ocjectPopulation(x, y, z,):
    Site = SSLSite("zxzxc", "yds", "sdfy", "Sdf", "dsf", "sdf", "sdf", "sdf")
    Site.SetURLLabel()

def main():
    #logic to parse command-line arguments
    if len(sys.argv) <= 1:
        raise ValueError("Please provide at least one website to parse, after calling the program name. Specfically, if you want to parse SSL information from more than one site, you must seperate the sites by comma(s). Example: SSL_Info siteX.com,siteY.com,siteZ.com")

    # Split the first argument by commas
    first_arg = sys.argv[1]
    args_list = first_arg.split(',')

    if len(args_list) > 1:
        # If there are multiple items separated by commas, consider them as separate arguments
        i = 0
        for arg in args_list:            
            TestObject.TestObject(arg)
            arg = TestObject.TestObject(arg, "IssuerLabel")
            i = i + 1
        GUI_Newest.gui1()        
    elif len(args_list) == 1:
        SSLLinfo(arg)
        arg = TestObject.TestObject(args_list, "IssuerLabel")   
    else:
        # If there is something else going on, raise an error
        raise ValueError("major error.")    
    # GUI_Newest.main

def SSLLinfo(URLField):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname = URLField) as s:
        s.connect((URLField, 443))
        results = json.dumps(s.getpeercert(), indent = 4)
        parsed = json.loads(results)

if __name__ == '__main__':
    main() 