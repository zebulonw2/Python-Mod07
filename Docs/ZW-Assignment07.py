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