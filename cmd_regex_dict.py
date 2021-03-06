commands = {
    "comment": {
        'regex': None,
        'types': {
            "single_line": {
                'regex': r"(?P<code>.*)(?P<comment>\/\/.*)",
                'examples': [r"blah blah // start game", ]
            },
            "multi_line_1line": {
                'regex': r"^\/\*.*\*\/$",
                'examples': [r"/* start tutorial chapter */", ]
            },
            "multi_line_start": {
                'regex': r"^\/\*.*",
                'examples': [r"/* start tutorial chapter", ]
            },
            "multi_line_end": {
                'regex': r".*\*/$",
                'examples': [r"start tutorial chapter */", ]
            },
        }
    },
    "exec": {
        'regex': r"^\\(?!if|else|elif|endif)(?P<command>\w+)(\s+(?P<args>.*))?",
        'types': {
            "be": {
                'regex': r"^\\be\s+(?P<me>me)\s*\=\s*@(?P<char_id>\w+)",
                'examples': [r"\be me=@player", ]
            },
            "end": {
                'regex': r"^\\end\s+(?P<me>me)",
                'examples': [r"\end me", ]
            },
            "load": {
                'regex': r"^\\load\s+(?P<var_name>\w+)(\s+from\s+(?P<file_name>\w+))?",
                'examples': [r"\load objects", r"\load objects from objects", ]
            },
            "delay": {
                'regex': r"^\\delay(\s+(?P<time>\d+)(?P<unit>\w+)?)?",
                'examples': [r"\delay", r"\delay 100ms", r"\delay 2"]
            },
            "clear": {
                'regex': r"^\\clear",
                'examples': ["\clear", ]
            },
            "assign": {
                'regex': r"^\\assign(\s+(?P<var_name>(@)?[\.\w]+))(:(?P<type>\w+))?\s*=\s*(?P<value>\S.*)",
                'examples': [r"\assign var = asdf", r"\assign var:str = asdf", r"\assign @player.name = $name",
                             r"\assign @player.age:int = 24"]
            },
        }
    },
    "narrative_structure": {
        'regex': r"^#+\s+.*",
        'types': {
            "chapter": {
                'regex': r"^#\s+(?P<chapter_name>.+)",
                'examples': [r"# Tutorial", ]
            },
            "level": {
                'regex': r"^##\s+(?P<level_name>.+)",
                'examples': [r"## Level 1", ]
            },
            "objective": {
                'regex': r"^###\s+(?P<objective_name>.+)",
                'examples': [r"### Level 1", ]
            },
        }
    },
    "output": {
        'regex': r"^(>|!).*",
        'types': {
            "dialog": {
                'regex': r"^>(\s+\[(?P<char_id>\w+)\])?(\s+(?P<text>.*))?",
                'examples': [r">", r"> [diana]", r"> lol", r"> [diana] Hi!", ]
            },
            "console": {
                'regex': r"^!\s+(?P<text>.*)",
                'examples': [r"! Loading...", ]
            },
        }
    },
    "input": {
        'regex': r"^\$.*",
        'types': {
            "input": {
                'regex': r"^\$(\s+\((?P<prompt>.*)\))?((\s+(?P<var_name>\w+))"
                         "(:(?P<type>\w+))?(\s+from\s+\[(?P<choices>.*)\])?)?",
                'examples': [r"$", r"$ (Please enter your name)", r"$ name", r"$ (Please enter your name) name",
                             r"$ (Please enter your name) name:str",
                             r"$ (Please enter your name) name:int from [1|2|3|4]", r"$ name:int from [1|2|3|4]"]
            },
        }
    },
    "action": {
        'regex': r"^\*.*",
        'types': {
            "request_task": {
                'regex': r"^\*\s+@(?P<char_id>\w+)\s+requests\s+%(?P<task_id>\w+)",
                'examples': [r"* @aaa requests %task1"]
            }
        }
    },
    "conditional": {
        'regex': r"^\\(if|else|elif|endif)(\s+(?P<args>.*))?",
        'types': {
            "if": {
                'regex': r"",
                'examples': []
            },
            "elif": {
                'regex': r"",
                'examples': []
            },
            "else": {
                'regex': r"",
                'examples': []
            },
            "endif": {
                'regex': r"",
                'examples': []
            },
        }
    }
}
