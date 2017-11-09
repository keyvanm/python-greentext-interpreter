commands = {
    "comments": {
        "regex": None,
        "types": {
            "single_line": {
                "regex": r"(?P<script>.*)(?P<comment>\/\/.*)",
                "examples": ["blah blah // start game", ]
            },
            "multi_line_1line": {
                "regex": r"^\/\*.*\*\/",
                "examples": ["/* start tutorial chapter */", ]
            },
            "multi_line_start": {
                "regex": r"^\/\*.*",
                "examples": ["/* start tutorial chapter", ]
            },
            "multi_line_end": {
                "regex": r".*\*/$",
                "examples": ["start tutorial chapter */", ]
            },
        }
    },
    "commands": {
        "regex": r"(?P<command>^\\\w+)\s(?P<args>.*)",
        "types": {
            "be": {
                "regex": r"^\\be\s(?P<me>me)\s\=\s@(?P<char_name>\w+)",
                "examples": ["\be me = @player", ]
            },
            "end": {
                "regex": r"^\\end\s(?P<me>me)",
                "examples": ["\end me", ]
            },
            "load": {
                "regex": r"^\\load\s(?P<var>\w+)\sfrom\s(?P<file_name>[\w\.]+)",
                "examples": ["\load objects from objects.json", ]
            },
            "delay": {
                "regex": r"^\\delay\s(?P<time>\d+)(?P<unit>\w+)",
                "examples": ["\delay 100ms", ]
            },
            "clear": {
                "regex": r"^\\clear",
                "examples": ["\clear", ]
            },
        }
    },
    "narrative_structure": {
        "regex": None,
        "types": {
            "chapter": {
                "regex": r"^#\s(?P<chapter_name>\w+)",
                "examples": ["# Tutorial", ]
            },
            "level": {
                "regex": r"^##\s(?P<level_name>\w+)",
                "examples": ["## Level 1", ]
            },
            "objective": {
                "regex": r"^###\s(?P<objective_name>\w+)",
                "examples": ["### Level 1", ]
            },
        }
    },
    "output": {
        "regex": r"^>",
        "types": {
            "named_dialog": {
                "regex": r"^>\s\[(?P<char_name>\w+)\]\s(?P<text>.*)",
                "examples": ["> [diana] Hi!", ]
            },
            "unnamed_dialog": {
                "regex": r"^>\s(?P<text>.*)",
                "examples": ["> What's up?", ]
            },
            "console_output": {
                "regex": r"^!\s(?P<text>.*)",
                "examples": ["! Loading...", ]
            },
        }
    },
    "input": {
        "regex": r"^\$",
        "types": {
            "raw_input": {
                "regex": r"^\$(\s\((?P<prompt>.*)\))?(\s(?P<var>\w+))?(:(?P<type>\w+))?",
                "examples": ["$", "$ name", "$ (Please enter your name)", "$ (Please enter your name) name", ]
            },
            "mc_input": {
                "regex": r"",
                "examples": ["", ]
            },
        }
    }
}
