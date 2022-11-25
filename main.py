from reply import *

def main():
    msg = input()

    r = Reply(msg)
    r.message()
    print(r)



if __name__ == '__main__':
    main()