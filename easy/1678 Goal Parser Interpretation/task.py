"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""


def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    tmp = ""
    for i in range(len(command)):
        if command[i] == "G":
            tmp += command[i]
        elif command[i] == "(" and command[i + 1] == ")":
            tmp += "o"
        elif command[i] == "(" and command[i + 1] == "a":
            tmp += "al"
        else:
            continue

    return tmp


def interpret1(command):
    """
    :type command: str
    :rtype: str
    """
    s = command.replace("()", "o")
    s = s.replace("(al)", "al")
    return s
