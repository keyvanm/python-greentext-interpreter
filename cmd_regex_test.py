import re

from cmd_regex_dict import commands

for cmd in commands:
    all_examples = []
    cmd_types = commands[cmd]['types']
    for cmd_type in cmd_types:
        cmd_regex_str = cmd_types[cmd_type]['regex']
        cmd_regex_compiled = re.compile(cmd_regex_str)
        examples = cmd_types[cmd_type]['examples']
        all_examples.extend(examples)

        for example in examples:
            try:
                assert cmd_regex_compiled.match(example) is not None
            except AssertionError:
                print()
                print("{cmd}.{cmd_type} doesn't compile {example}".format(cmd=cmd, cmd_type=cmd, example=example))
                print()

    main_regex_str = commands[cmd]['regex']
    if main_regex_str:
        main_regex_compiled = re.compile(main_regex_str)
        for example in all_examples:
            try:
                assert main_regex_compiled.match(example) is not None
            except AssertionError:
                print()
                print("{cmd} doesn't compile {example}".format(cmd=cmd, cmd_type=cmd, example=example))
                print()
            except TypeError:
                pass
