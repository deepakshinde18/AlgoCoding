"""Module providing a function matching parenthesis."""


def match_parenthesis(string):
    """This method match parenthesis

    Args:
        string (string): string to match parenthesis

    Returns:
        boolean: returns True or False depending on parenthesis match
    """
    stack = []
    for char in string:
        # if char == "(" or char == "{" or char == "[":
        if char in ("(", "{", "["):
            stack.append(char)
        # elif char == ")" or char == "}" or char == "]":
        elif char in (")", "}", "]"):
            if not stack:
                return False
            elif (
                (char == ")" and stack[-1] == "(")
                or (char == "}" and stack[-1] == "{")
                or (char == "]" and stack[-1] == "[")
            ):
                stack.pop()
            else:
                return False
    return not stack


print(match_parenthesis("({[]})"))
print(match_parenthesis("]}()[]"))
