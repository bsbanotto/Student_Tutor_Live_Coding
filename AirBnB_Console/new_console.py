#!/usr/bin/python3
"""
This is a comand line interpreter created during a live code
"""
import cmd


class LiveCodePrompt(cmd.Cmd):
    """
    doc string for LiveCodePrompt class
    """
    prompt = "promptymcpromptface "

    def do_exit(self, args):
        """
        Exits command line interpreter
        """
        raise SystemExit

    def do_printline(self, args):
        """
        prints the line that is passed to it
        """
        print(args)

    def do_addition(self, args):
        """Adds two numbers together"""
        numbers = args.split()
        numbers = [int(number) for number in numbers]
        print(numbers[0] + numbers[1])

if __name__ == "__main__":
    LiveCodePrompt().cmdloop()