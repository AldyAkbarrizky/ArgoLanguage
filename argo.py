import basic
import sys

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = ""

if file_name == "":
    while True:
        text = input('argo > ')
        if text.strip() == "": continue
        result, error = basic.run_shell('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
else:
    basic.run_file(file_name)