#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for order in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[order][0:2] != "__":
            print("{}".format(dir(hidden_4)[order]))
