import pathlib
import os
import sys




class GlobalData:
    utilityName = "cgen"
    utilityVersion = "0.0.1"





# function to get the path from the relative path of file
# required when file is bundled with pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)








# class containing path lib methods
class PathFunctions:


    # method to return all sub folders inside a dir
    @classmethod
    def getSubFolders(cls , root_path):

        pathList = []

        dirpath = pathlib.Path(root_path)
        
        # raise error if the root path is not a dir itself
        assert dirpath.is_dir()

        for path in dirpath.iterdir():
            if(path.is_dir()):
                pathList.append(path)

        pathList = sorted(pathList , key=lambda x : x.name)

        return pathList



    # method to return all sub files inside a dir
    # does not include files inside sub dirs
    @classmethod
    def getSubFiles(cls , folder_path):

        filesList = []

        dirpath = pathlib.Path(folder_path)

        # raise error if the folder_path is not a dir itself
        assert dirpath.is_dir()

        for x in dirpath.iterdir():
            if(x.is_file()):
                filesList.append(x)

        filesList = sorted(filesList , key=lambda x : x.name)

        return filesList








# function to get the mapping dict
# mapping dict structure = {
# "dir1_dirOne" : [{"name" : "file1" , "fullName" : "file1.ext" , "path" : pathlib.Path()} , {} , {}] , 
# "dir2" : [] ,
# }
# dir1 and dir2 are dirs inside templates folder
# dirOne is alternative name to dir1
# file1.ext is file inside dir1 dir
# pathlib.Path() is the absolute path of the file 
def get_mapping_dict(root_path):

    result_dict = {}

    for dir in PathFunctions.getSubFolders(root_path):
        dirName = str(dir.name).lower()

        subFiles = PathFunctions.getSubFiles(dir)

        subList = []

        for file in subFiles:
            subDict = {}
            subDict["name"] = str(file.stem).lower()
            subDict["fullName"] = str(file.name).lower()
            subDict["path"] = file.absolute()
            subList.append(subDict)

        result_dict[dirName] = subList

    return result_dict









# get the file path from the file requested by resolving the syntax
# returns absolute path of file else returns None
# ex - file_requested = py-main
# returned path = absolute path of templates/py/main.py
def get_file_path(file_requested):
    # dirName-filename
    # fileName should be without extension

    dirName , fileName = str(file_requested).lower().split("-")

    # get mapping dict
    mapping_dict = get_mapping_dict(resource_path("templates/"))

    for key , value in mapping_dict.items():
        dirNames = key.split("_")

        if(dirName in dirNames):

            for i in value:

                # if the name matched return file path
                if(i.get('name') == fileName):
                    return i.get("path")

    return None

     






# method to parse the system arguments
def args_parser():
    
    # file containing the boiler plate code
    try:
        boiler_plate_file = sys.argv[1]
    except IndexError:
        raise IndexError("No boiler_plate_file reference passed")
        

    # file path to write to
    try:
        file_name = pathlib.Path(sys.argv[2]).absolute()
    except IndexError:
        raise IndexError("No file_name passed")
    except FileNotFoundError:
        raise ValueError(f"No path found at {sys.argv[2]}")


    boiler_plate_file_path = get_file_path(boiler_plate_file)

    if(boiler_plate_file_path == None):
        raise ValueError(f"No Template named {boiler_plate_file}")

    
    return file_name , boiler_plate_file_path









# function to copy the boiler plate code from boiler_plate_file_path to file_name
def generate_boiler_plate_file(file_name , boiler_plate_file_path):

    try:
        with open(file_name , "wb") as toWrite , open(boiler_plate_file_path , "rb") as toRead:
            data = toRead.read()
            toWrite.write(data)
    except PermissionError:
        raise PermissionError(f"Looks like {GlobalData.utilityName} does not have permission to write at {file_name}")
        







# function to generate markdown documentation of all the templates
def get_markdown(path):

    markdown = ""

    # get mapping dict
    mapping_dict = get_mapping_dict(resource_path("templates/"))

    count = 1
    
    allDirs = []

    for key , value in mapping_dict.items():

        # getting the alternate names of dir seperated by _
        dirNames = key.split("_")

        string = ""

        # adding all the dirs to string
        for i in dirNames:
            string = string + i + " / "

        string = string[:-3]
        
        # generating heading
        markdown = markdown + f"\n\n# {count}. {string}\n<br>\n<br>\n\n"

        tempList = []

        # adding boiler plates 
        for valueCount,i in enumerate(value):

            # adding boiler plate heading
            markdown = markdown + f"""### {valueCount + 1}. {dirNames[-1]}-{i.get("name")}\n\n<br>\n\n"""
            tempList.append(f"""{dirNames[-1]}-{i.get("name")}""")

            with open(i.get("path") , "r") as file:
                data = file.read()

            # add boiler plate code
            markdown = markdown + f"""```{dirNames[0]}\n{data}\n```"""

            markdown = markdown + "\n<br>\n<br>\n<br>\n"    


        allDirs.append([string , tempList])

        markdown = markdown + "\n<br>\n<br>\n<br>\n<br>\n<br>\n"    

        count = count + 1


    # preparing index
    markdown_alldirs = "# Index : \n"
    
    for i,j in enumerate(allDirs):
        markdown_alldirs = markdown_alldirs + f"{i + 1}. {j[0]}\n"

        for k,l in enumerate(j[1]):
            markdown_alldirs = markdown_alldirs + f"    {k + 1}. {l}\n"



    markdown_alldirs = markdown_alldirs + "\n<br>\n<br>\n<br>\n<br>\n<br>\n"    


    # writing markdown
    with open(path , "w") as file:
        file.write(markdown_alldirs)
        file.write(markdown)


    




def main():
    
    try:
        result = args_parser()
    except Exception as ex:
        print("\n\n")
        print("ERROR :" , ex)
        sys.exit()


    try:
        generate_boiler_plate_file(*result)
    except Exception as ex:
        print("\n\n")
        print("ERROR :" , ex)
        sys.exit()









if __name__ == "__main__":
    main()