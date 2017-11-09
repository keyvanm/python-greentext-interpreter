from getch import getch


def get_next():
    ch = getch()
    while ch.strip() != '':
        ch = getch()


def echo(char, text, wait_for_next=True):
    if char:
        print("> [{char_name}] {text}".format(char_name=char['name'], text=text))
    else:
        print("> {text}".format(text=text))

    if wait_for_next:
        get_next()


def get_input(prompt, type, choices):
    if prompt:
        return input("$ ({})".format(prompt))
    return input("$ ")


