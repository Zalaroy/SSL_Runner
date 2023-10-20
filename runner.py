import sys
import GUI_Newest 
import SSLSite
import TestObject


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
        for arg in args_list:
            TestObject(arg)
    elif len(args_list) == 1:
        gui1(args_list)   
    else:
        # If there is something else going on, raise an error
        raise ValueError("major error.")    
    GUI_Newest.main



if __name__ == '__main__':
    main() 