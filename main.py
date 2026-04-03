from typing import List, Optional


def func1():
    lst = []
    print("Enter numbers one at a time. Enter 0 to stop.")
    x = int(input("num:"))
    while x != 0:
        lst.append(x)
        x = int(input("num:"))
    return lst


def _op_loop(data, test_choice: int = None):
    while True:
        choice = (
            test_choice
            if test_choice
            else int(input("Select an option. 1-sum  2-min  3-max  4-quit"))
        )
        if choice == 1:
            _res = sum(data)
            print(f"The sum is {_res}")
            return _res
        elif choice == 2:
            _res = min(data)
            print(f"The min is {_res}")
        elif choice == 3:
            _res = max(data)
            print(f"The max is {_res}")
        elif choice == 4:
            print("Goodbye")
            return None
        if test_choice is not None:
            return _res


def func2(data, test_inputs: Optional[List[int]] = None):
    print("Data: ")
    print(data)
    if test_inputs:
        return [_op_loop(data, t) for t in test_inputs]
    return _op_loop(data)


def main():
    print("Hello, World!")
    data = func1()
    func2(data)


if __name__ == "__main__":
    main()
