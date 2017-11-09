commands = {
    "comments": {
        'regex': None,
        'types': {
            "single_line": {
                'regex': r"(?P<script>.*)(?P<comment>\/\/.*)",
                'examples': ["blah blah // start game", ]
            },
            "multi_line_1line": {
                'regex': r"^\/\*.*\*\/",
                'examples': ["/* start tutorial chapter */", ]
            },
            "multi_line_start": {
                'regex': r"^\/\*.*",
                'examples': ["/* start tutorial chapter", ]
            },
            "multi_line_end": {
                'regex': r".*\*/$",
                'examples': ["start tutorial chapter */", ]
            },
        }
    },
    "commands": {
        'regex': r"(?P<command>^\\\w+)\s(?P<args>.*)",
        'types': {
            "be": {
                'regex': r"^\\be\s(?P<me>me)\s\=\s@(?P<char_name>\w+)",
                'examples': ["\be me = @player", ]
            },
            "end": {
                'regex': r"^\\end\s(?P<me>me)",
                'examples': ["\end me", ]
            },
            "load": {
                'regex': r"^\\load\s(?P<var>\w+)\sfrom\s(?P<file_name>[\w\.]+)",
                'examples': ["\load objects from objects.json", ]
            },
            "delay": {
                'regex': r"^\\delay(\s(?P<time>\d+)(?P<unit>\w+))?",
                'examples': ["\delay", "\delay 100ms", ]
            },
            "clear": {
                'regex': r"^\\clear",
                'examples': ["\clear", ]
            },
            "assign": {
                'regex': r"^\\assign(\s\$(?P<var>\w+))(:(?P<type>\w+))?\s*=\s*(?P<value>\S.*)",
                'examples': ["\assign $var = asdf", "\assign $var:str = asdf"]
            },
        }
    },
    "narrative_structure": {
        'regex': None,
        'types': {
            "chapter": {
                'regex': r"^#\s(?P<chapter_name>\w+)",
                'examples': ["# Tutorial", ]
            },
            "level": {
                'regex': r"^##\s(?P<level_name>\w+)",
                'examples': ["## Level 1", ]
            },
            "objective": {
                'regex': r"^###\s(?P<objective_name>\w+)",
                'examples': ["### Level 1", ]
            },
        }
    },
    "output": {
        'regex': r"^(>|!).*",
        'types': {
            "named_dialog": {
                'regex': r"^>(\s\[(?P<char_name>\w+)\])?(\s(?P<text>.*))?",
                'examples': [">", "> [diana]", "> lol", "> [diana] Hi!", ]
            },
            "console_output": {
                'regex': r"^!\s(?P<text>.*)",
                'examples': ["! Loading...", ]
            },
        }
    },
    "input": {
        'regex': r"^\$.*",
        'types': {
            "input": {
                'regex': r"^\$(\s\((?P<prompt>.*)\))?((\s\$(?P<var>\w+))(:(?P<type>\w+))?(\sfrom\s\[(?P<choices>.*)\])?)?",
                'examples': ["$", "$ (Please enter your name)", "$ $name", "$ (Please enter your name) $name", "$ (Please enter your name) $name:str", "$ (Please enter your name) $name:int from [1|2|3|4]", "$ $name:int from [1|2|3|4]"]
            },
        }
    },
    "action": {
        'regex': r"^\*.*",
        'types': {
            "request_task": {
                'regex': r"",
                'examples': []
            }
        }
    }
}
