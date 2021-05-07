#File Renaming Script
#by: Arman Nadjarian
import sys, fileinput
import os

#file_extension is of the format, .txt, .pdf, .cpp, etc...
#new_file(file_extension) :: this program takes an input,
#and checks that the input contains all alphanumeric values.
#If the first value is a number however, it removes it.
#If a file extension is entered, it is ignored.
#Function uses the passed in value for file_extension
def new_file(file_extension):
    new_file_name = input("Enter a valid file name: ")
    while new_file_name[0].isnumeric():
        print("File cannot start with number. Removing first value...")
        new_file_name = new_file_name[1:]
    if '.' in new_file_name: #handles the possibility of users entering a different file extension on accident
        new_file_name = new_file_name[: new_file_name.index('.')]
    new_file_name = new_file_name + file_extension
    return new_file_name

#Program begins here
if __name__ == '__main__':
    #If the program does not take in the correct amount 
    #of arguments from the command line
    if len(sys.argv) <= 1:
        print("Program should be run as :: python3 file_rename.py <path to change>")
        print("Goodbye")
        quit()
    file_path = sys.argv[1]
    #if the file does not exist in the given path
    if(not os.path.exists(file_path)):
        print("File path does not exist. Goodbye.")
        quit()
    try:
        fileOpened = open(file_path)
        # Do something with the file
    except IOError:
            print(f"{fileOpened} File can't be opened. Goodbye.")
            quit()
    finally:
        fileOpened.close()
    print(f"The file path to be modified :: {file_path}")

    #file_head contains the path to the directory of the file, excluding the final "/"
    #file_tail contains the file itself
    file_head, file_tail = os.path.split(file_path) #split path

    #Splits the file_tail into the name of the file and it's file extension
    file_name, file_extension = os.path.splitext(file_tail) #split name with extension
    print(f"File Name :: {file_name} ... File Extension :: {file_extension} \n")
    
    final_file_name = new_file(file_extension) #new_file(file_extension) gets the new file name
    
    #if the file is in a different directory
    if file_head != '':
        final_file_path = file_head + "/" + final_file_name #builds the final file path
    else: #else (file is in the same directory)
        final_file_path = final_file_name
    os.rename(file_path, final_file_path) #rename the file path with final file path