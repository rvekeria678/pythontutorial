import os
import time

# os.getcwd() -> get current working directory
# os.chdir(<path>) -> change directory
# os.listdir() -> list directories
# os.mkdir(<dirname>) -> create a directory
# os.makedirs(<dirname>) -> make directories recursively
# os.rmdir(<dirname>) -> remove directory
# os.removedirs(<dirname>) -> remove directory recursively
# os.rename(<from>,<to>) -> rename file
# os.state(<filename>) -> print all info of a file
# os.walk(<path>) -> traverse directory recursively
# os.environ -> get environment variables
# os.path.join(<path>, <file>) -> join path without worrying about /
# os.path.basename(<filename>) -> get basename
# os.path.dirname(<filename>) -> get dirname
# os.path.exists(<path-to-file>) -> check if the path exists or not
# os.path.splitext(<path-to-file>) -> split path and file extension
# dir(os) -> check what methods exists


# Changes Directories
#os.chdir('C:/Users/Swaggy P/OneDrive\Documents/')

while True:
    print(os.getpid())
    time.sleep(1)