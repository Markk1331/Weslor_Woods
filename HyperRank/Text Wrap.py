import textwrap
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))
if __name__ == '__main__':
    string_name, sector = input(), int(input())
    result = wrap(string_name, sector)
    print(result)