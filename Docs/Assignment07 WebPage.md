**Zeb Williams**  
29Nov2021  
IT FND 110A Au21  
Assignment 07

# ZWAssignment07.py

### Introduction
This week we learned about structured error handling, pickling, and how to format a GitHub web page using the markdown language. In order to demonstrate my understanding of these concepts I have written a test script which I will use to illustrate these topics.

### My Script
This is a short script which opens a .txt file from the file directory, reads the file contents and puts them into a list item, and gives the user the option to write the list item into a new binary file. I have added a try-except block with a ‘file not found’ error, and a non-specific error.

### Python Documentation
To learn more about pickling and error-handling I used the python documentation:  
[Pickling](https://docs.python.org/3/library/pickle.html)  
[Errors and Exceptions](https://docs.python.org/3/tutorial/errors.htm)  
I like these pages because they are comprehensive and I have the confidence that the information is accurate. I want to get used to reading official python documentation early in my coding career, even though it might be more challenging to digest than a page found in an internet search. 

### File Not Found  
When the user runs the script, the first thing it does it to try opening a .txt file and writing the data within into a list item, using the following function (**Figure 1**)  

![Figure 1](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure1.png "Figure 1")  
**Figure 1 -- Add data from .txt file into list item**  

I added an exception to handle a ‘FileNotFoundError.’ This would be triggered if the file name was misspelled, or if the file was not located in the same folder as the script. If this error was triggered I displayed a simple message to the user explaining how to proceed. (**Figure 2**) I also added a general error message, which instructs the user to send the error information to the programming department so they could look into it and add more try-except blocks to the code, so the next time that error is encountered there will be a better presentation to the user.  

![Figure 2](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure2.png "Figure 2")  
**Figure 2-- Try-Except block**  

### Pickling

If the file is correctly named, and present in the correct folder, it will be added to a list. I then created a function that, when instructed to do so by the user, will add that list to a binary file (**Figure 3**) The function opens a new file in ‘write-binary’ or ‘wb’ mode, then uses the pickle method ‘dump()’ to add the contents of the list into the new file.  

![Figure 3](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure3.png "Figure 3")  
**Figure 3 --Pickle list**  

### Testing the script  
I first ran the script in the command shell, and to test the error handling I made sure the file name was not spelled correctly (**Figure 4**)  

![Figure 4](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure4.png "Figure 4")  
**Figure 4 -- File name with errant underscore**  

The exception block worked as expected (**Figure 5**)  

![Figure 5](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure5.png "Figure 5")  
**Figure 5 -- Error message produced by "FileNotFoundError"**  

I then used PyCharm to run the script when the file was correctly named (**Figure 6**)  

![Figure 6](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure6.png "Figure 6")  
**Figure 6 -- File named correctly**  

And the script ran as expected (**Figure 7**) and generated a binary file (**Figure 8**)  

![Figure 7](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure7.png "Figure 7")  
**Figure 7 -- List item derived from .txt file, user directing script to make binary file**

![Figure 8](https://github.com/zebulonw2/IntroToProg-Python-Mod07/blob/main/docs/attachments/Figure8.png "Figure 8")  

### Appendix: ZWAssignment07.py script text
```
# ------------------------------------------------- #
# Title: ZW-Assignment07
# Description: Open .txt file, read contents into list, pickle and unpickle list
# ChangeLog: Zeb W, 29Nov2021, Create Script
# ------------------------------------------------- #
import pickle
# -- Data -- #
start_file = 'openme.txt'
end_file = 'new_file.dat'

# -- Processing -- #
class work_with_files: #class containing functions that process input file, list item, and output file

    @staticmethod
    def read_data_from_txt_file_into_list(file_name):
        """ Reads rows of data data from a file into a list

        :param file_name: (string) with name of file
        :return: (list) of data rows read from the file
        """
        data = []
        for row in open(file_name, 'r'):
            data.append(row.strip())
        return data

    @staticmethod
    def pickle_list(new_file, list_to_add):
        '''puts list into binary file

        :param new_file: file object
        :param list_to_add: list object to put into file object
        :return: a new file
        '''
        objFile = open(new_file, "wb")
        pickle.dump(list_to_add, objFile)
        objFile.close()
        return new_file

# -- Presentation (I/O) -- #
try:
    list = work_with_files.read_data_from_txt_file_into_list(start_file)
except FileNotFoundError as e:
    print("File Not Found:")
    print("Plese make sure the file name is spelled correctly")
    print("and is in the same folder as this script, then rerun the program")
except Exception and e:
    print("There was an unexpected error:")
    print("Please screenshot the following information and send it to the programming department")
    print("So they can look into the error and add a new exception to this code")
    print("==========================")
    print(e, e.__doc__, type(e), sep='\n')
    print("==========================")
else:
    while True:
        print('Here is your new list item:')
        print(list)
        user_choice = input("Would you like to add this list to a new binary file? (Y/N): ")
        if user_choice.lower() == 'y':
            work_with_files.pickle_list(end_file, list)
            print("\nSuccess! Check the file directory to find your new binary file.")
            break

        elif user_choice.lower() == 'n':
            print("\nGoodbye!")
            break

        else:
            print("\nThat is not an option, enter either Y or N\n")
```
