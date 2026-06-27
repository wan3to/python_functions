from pathlib import Path
def count_vowels(text: str) -> int:
    """counts the number of vowels (A, E, I, O, U, case-intensitive)
    in a given string (excluding y & Y).
    
    Examples:
    >>> count_vowels('Hello World')
    3
    >>> count_vowels('AEIOUaeiou')
    10
    >>> count_vowels('')
    0
    """

    if not isinstance(text, str):
        raise TypeError(f'"text" must be a str. "{type(text)}" is invalid.')
    
    vowels: str = 'aeiouAEIOU'
    return sum(1 for letter in text if letter in vowels)

inputs: dict = {
    'He is over there!': 6,
    '': 0,
    'aeiouAEIOU':10,
    'Bob': 5,
    True: TypeError,
    Path('text.txt'): TypeError,
}

for var, result in inputs.items():
    try:
        passed: bool = count_vowels(var) == result
        print(f"count_vowels({repr(var)}) == {result}, {passed=}")
    except TypeError as e:
        passed = result is type(e)
