# GMIT PforCS
# Author Michal Sudol G00398852@gmit.ie
# Python - The Collatz Sequence V2

print ("Hi, to hit Enter to Proceed..")
from typing import Generator

def collatz_gen(starting_num: int) -> Generator[int, None, None]:
    yield starting_num

    num = starting_num
    while num > 1:
        num = (num // 2) if num % 2 == 0 else (3 * num + 1)
        yield num

def ask_for_num() -> int:
    while True:
        raw_num = input("> ")

        try:
            return int(raw_num)

        except ValueError:
            print('Please enter a number')