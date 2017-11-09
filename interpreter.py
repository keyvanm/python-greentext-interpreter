import importlib
import re
import time

from cmd_regex_vars import *

DEFAULT_DELAY_TIME = 0.5

DEFAULT_DELAY_TIME_UNIT = "s"


def comment_strip(line):
    comment__single_line__regex = comment__cmds['types']["single_line"]['regex']

    line = line.strip()
    match = re.match(comment__single_line__regex, line)
    if match:
        code = match.group('code')
        return code.strip()
    return line


def update(var, val, context):
    if var not in context:
        context[var] = val
    else:
        context[var].update(value)


chapters = []
context = {
    'objects': {},
    'characters': {},
    'tasks': {},
    'chapters': chapters
}

with open("codewars.greentext") as gt_file:
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
                if not file_name:
                    file_name = var_name
                value = getattr(importlib.import_module(var_name, package=file_name), var_name)
                update(var_name, value, context)

            delay__match = re.match(delay__command__regex, code)
            if delay__match:  # \delay 1000ms
                t = delay__match.group('time')
                if not t:
                    t = DEFAULT_DELAY_TIME
                unit = delay__match.group('unit')
                if not unit:
                    unit = DEFAULT_DELAY_TIME_UNIT
                if unit == "s":
                    time_in_s = int(t)
                elif unit == "ms":
                    time_in_s = int(t) / 1000
                else:
                    raise ValueError
                time.sleep(time_in_s)

            clear__match = re.match(clear__command__regex, code)
            if clear__match:  # \clear
                pass

            assign__match = re.match(assign__command__regex, code)
            if assign__match:  # \assign var:int = 10
                var_name = assign__match.group('var_name')
                var_type = assign__match.group('type')
                value = assign__match.group('value')
                available_cast = {'str': str, 'int': int, 'bool': bool, 'list': list, 'set': set, 'float': float}
                if var_type:
                    if not var_type in available_cast:
                        raise ValueError
                    value = available_cast[var_type](value)
                context[var_name] = value

        elif re.match(narr__cmds['regex'], code):
            chapter__match = re.match(chapter__narr__regex, code)
            if chapter__match:
                chapter_name = chapter__match.group('chapter_name')
                chapters.append({
                    'name': chapter_name,
                    'levels': []
                })

            level__match = re.match(level__narr__regex, code)
            if level__match:
                level_name = level__match.group('level_name')
                curr_chapter = chapters[-1]
                curr_chapter['levels'].append({
                    'name': level_name,
                    'objectives': []
                })

            objective__match = re.match(objective__narr__regex, code)
            if objective__match:
                objective_name = objective__match.group('objective_name')
                curr_chapter = chapters[-1]
                curr_level = curr_chapter['levels'][-1]
                curr_level['objectives'].append({
                    'name': objective_name,
                })

        elif re.match(dialog__cmds['regex'], code):
            pass

        elif re.match(input__cmds['regex'], code):
            pass

        elif re.match(action__cmds['regex'], code):
            pass

        else:
            raise SyntaxError
