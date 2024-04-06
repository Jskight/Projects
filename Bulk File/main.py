import os

def main():
    i = 0
    # Edit path variable below to your folder path
    path = "./bulk file/1/"
    for filename in os.listdir(path):
        # Edit my_dest variable to default file name and file extenstion
        my_dest = "text" + str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()