import os
from parser import Parser
from util import isHaas


def main():
    # Use a breakpoint in the code line below to debug your script.
    file = open(os.getcwd() + "/test/sample_email")
    parser = Parser(file)
    for article in parser.get_articles():
        if isHaas(article):
            print(article)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()