#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum_of_arg = 0
    arg_int = []
    if len(argv) == 1:
        print("{}".format(len(argv)-1))
    elif len(argv) >= 2:
        for arg in range(1, len(argv)):
            arg_int.append(int(argv[arg]))
        sum_of_arg = sum(arg_int)
        print("{}".format(sum_of_arg))
