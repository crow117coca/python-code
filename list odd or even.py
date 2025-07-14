
numbers = {
'a': 34,

'b': 23,

'c': 323,

'd': 76,

'e': 87,

'f': 64
}
for key, value in numbers.items():
    print(f"{key} = {value}")
    choice = input("\nChoose a letter (a–f): ").strip().lower()
if choice in numbers:
    num = numbers[choice]
if num % 2 == 0:
    print(f"{choice} is an even number ({num}).")
else:
    print("Invalid choice. Please run the program again and pick a letter a–f.")