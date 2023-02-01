#!/usr/bin/env python3
"""
Creating a python command line interpreter for live coding
"""
import cmd


class LiveCodeCommand(cmd.Cmd):
    """
    This class will implement the interpreter
    """
    prompt = "PromptyMcPromptFace$ "

    def do_exit(self, args):
        """Exits the command line interpreter"""
        raise SystemExit

    def do_print_cheerful_message(self, args):
        """Prints a cheerful message
    usage: print_cheerful_message "Message to be printed"
        """
        print(args)

    def do_addition(self, args):
        """Returns the sum of two numbers
        usage: addition num1 num2
        """
        numbers = args.split()
        if (len(numbers) != 2):
            print("error: Must use two or more argumennts")
            return
        numbers = [int(number) for number in numbers]
        print(numbers[0] + numbers[1])

if __name__ == "__main__":
    LiveCodeCommand().cmdloop()
