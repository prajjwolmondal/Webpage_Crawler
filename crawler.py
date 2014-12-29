# Author: Prajjwol Mondal
# Git website: https://github.com/theposter

# Webcrawler made using Beautiful Soup in Python

# This program, takes in a url from the user, and asks for data that 
# the user wants to extract from a page, such as all the url's, or all 
# the images in the page. Program also asks for a path to store the output.

import urllib;
import sys;
from bs4 import BeautifulSoup;

def getURL(): 
#This function is responsible for getting the URL from user and
#error checking, which makes sure the URL is at least 3 characters long.
    link = raw_input("Please enter target URL: ");
    valid = False;
    while (valid == False):
        if (len(link)<3):
            print "Invalid URL entered. Please try again";
            link  = raw_input("Please enter target URL: ");
        else:
            valid = True;
    return link;

def mainMenu():
# Simple function for the main menu.
    print "What do you want to extract from the page provided?"
    print "Enter one of the following codes:"
    print "0 for the title of the page"
    print "1 for all the links in the page"
    print "2 for all the text in the page"
    print "3 for all the images in the page"
    return ((int)(raw_input()));

def main():
    print "Welcome to the program.";
    url = getURL();
    doc = urllib.urlopen(url).read();
    soup = BeautifulSoup(doc);
    
    userInput = mainMenu();    
    if userInput == 0:
        data = soup.title.string;
    elif userInput == 1:
        data = soup.find_all('a');
    elif userInput == 2:
        data = soup.get_text();
    elif userInput == 3:
        raw_data = soup.findAll('img');
        data = [each.get('src') for each in raw_data]
    else:
        data = soup;
    
    if (userInput == 3):
        path = raw_input("Please provide path for the images to be stored. ");
        counter = 0;
        for arg in data:
            if (counter < 25):
                print "Downloading and storing..."
            elif (counter < 50):
                print "Still downloading and storing..."
            else:
                print "This might take a while..."
            fileName=arg.split('/')[-1];
            urllib.urlretrieve(arg,path+fileName);
            counter += 1;
        print "Done."
        print "Thanks for using my program!"
        sys.exit(0);
    userInput = int(raw_input("Type 1 to save to file and 2 to print to screen.  "));
    if (userInput == 2):
            print data;
            print ""
            print "Thanks for using my program!"
            sys.exit(0);
    elif (userInput == 1):
            path = raw_input("Please provide path for the text file to be stored. ");
            try: 
                dest = open((path+'/code.txt'), 'w'); #Path to destination
                dest.write(Data);
                print "Data written to file."
                print "Thanks for using my program!"
            except IOError, e:
                print >> sys.stderr, "Exception: %s" % str(e);
                sys.exit(1);
            except:
                print "Unexpected error:", sys.exc_info()[0];
                raise;
    else:
        print "Wrong input!"
        sys.exit(0);


main()
