#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfc = dir()
    for i in range(len(allfc)):
        if allfc[i][:2] != "__":
            print("{}".format(allfc[i]))
