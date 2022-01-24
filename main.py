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

        assert dirpath.is_dir()

        for path in dirpath.iterdir():
            if path.is_dir():
                pathList.append(path)

        return pathList



    # method to return all sub files inside a dir
    # does not include files inside sub dirs
    @classmethod
    def getSubFiles(cls , folder_path):

        filesList = []

        dirpath = pathlib.Path(folder_path)

        assert dirpath.is_dir()

        for x in dirpath.iterdir():
            if x.is_file():
                filesList.append(x)

        return filesList








def main():
    print(PathFunctions.getSubFolders(resource_path("templates/")))
    input()
    print(PathFunctions.getSubFiles(resource_path("templates/py/")))







if __name__ == "__main__":
    main()