def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    if s==s.upper():
        return True
    elif s==s.capitalize():
        return False

print(main('HELLO'))