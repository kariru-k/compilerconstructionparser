from lexer import *
from parse import *
import sys
# f = open("samplecode.txt", "r")
#
# data = f.read()


def main():
    print("This is the Compiler")

    if len(sys.argv) != 2:
        sys.exit("No source file specified as an argument for the compiler")
    with open(sys.argv[1], "r") as inputfile:
        input = inputfile.read()

    lexer = Lexer(input)
    # token = lexer.getToken()
    # while token.kind != TokenType.EOF:
    #     print("Token: ", token.kind, "Token value:", token.text)
    #     token = lexer.getToken()
    parser = Parser(lexer)

    parser.program()
    print('Parse Successful')

main()
