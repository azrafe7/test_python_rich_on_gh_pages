from rich.console import Console

print("python print")

console = Console()
console.log("console.log", [1, "str"], 'https://github.com/willmcgugan/rich/blob/9cba2027f4/tests/test_color_triplet.py', {"k": 'v', "date": '00:46:54'}, None, '2009-11-27T00:00:00.000100-06:39')
console.print("console.print", [1, "str"], 'https://github.com/willmcgugan/rich/blob/9cba2027f4/tests/test_color_triplet.py', {"k": 'v', "date": '00:46:54'}, None, '2009-11-27T00:00:00.000100-06:39')
