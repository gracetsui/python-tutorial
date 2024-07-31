def hello(name, lang):
    greetings = {
        "English": "Hello (EN)",
        "Spanish": "Hola (ES)",
        "German": "Hallo (DK)"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
    # return '(returning)' + msg


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname",
        required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German"],
        help="The language of the greeting."
    )
    
    print('args:', parser.parse_args()) # Alex: to understand args
    
    args = parser.parse_args()

    hello(args.firstname, args.lang)
    
    # msg = f"Hello {args.firstname}, perfers {args.lang}!"
    # returned_msg = hello(args.firstname, args.lang)
    # print(returned_msg)
    
    
