import importlib
import re

from cmd_regex import commands

gt_filename = "codewars.greentext"

comment__cmds = commands["comment"]
exec__cmds = commands["exec"]
narrative_structure__cmds = commands["narrative_structure"]
dialog_output__cmds = commands["dialog_output"]
input__cmds = commands["input"]
action__cmds = commands["action"]

multi_line_1line__comment__regex = comment__cmds['types']["multi_line_1line"]['regex']
multi_line_start__comment__regex = comment__cmds['types']["multi_line_start"]['regex']
multi_line_end__comment__regex = comment__cmds['types']["multi_line_end"]['regex']

be__command__regex = exec__cmds['types']["be"]['regex']
end__command__regex = exec__cmds['types']["end"]['regex']
load__command__regex = exec__cmds['types']["load"]['regex']
delay__command__regex = exec__cmds['types']["delay"]['regex']
clear__command__regex = exec__cmds['types']["clear"]['regex']
assign__command__regex = exec__cmds['types']["assign"]['regex']


def comment_strip(line):
    comment__single_line__regex = comment__cmds['types']["single_line"]['regex']

    line = line.strip()
    match = re.match(comment__single_line__regex, line)
    if match:
        code = match.group('code')
        return code.strip()
    return line


context = {
    'objects': {},
    'characters': {},
    'tasks': {}
}

with open(gt_filename) as gt_file:
    player_id = None

    for line in gt_file:
        # getting rid of multi line comments
        multi_line_1line__matcher = re.compile(multi_line_1line__comment__regex)  # /* comment */
        multi_line_start__matcher = re.compile(multi_line_start__comment__regex)  # /* multi line
        multi_line_end__matcher = re.compile(multi_line_end__comment__regex)  # comment */

        if multi_line_1line__matcher.match(line):
            continue
        if multi_line_start__matcher.match(line):
            line = gt_file.readline()
            while not multi_line_end__matcher.match(line):
                line = gt_file.readline()

        # strip the line and remove inline comments
        code = comment_strip(line)  # code  // comment
        if not code:
            continue  # if code was empty after comment stripping

        if re.match(exec__cmds['regex'], code):  # \exec
            be__match = re.match(be__command__regex, code)
            if be__match:  # \be me=@player
                char_id = be__match.group('char_id')
                player_id = char_id

            end__match = re.match(end__command__regex, code)
            if end__match:  # \end me
                exit()

            load__match = re.match(load__command__regex, code)
            if load__match:  # \load var from filename
                var_name = load__match.group('var_name')
                file_name = load__match.group('var_name')
                value = importlib.import_module(var_name, package=file_name)
                if var_name not in context:
                    context[var_name] = value
                else:
                    context[var_name].update(value)

