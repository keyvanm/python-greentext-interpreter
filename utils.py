import re

from cmd_regex_vars import comment__cmds


def peek_line(lines, curr_line_no):
    return lines[curr_line_no + 1]


def comment_strip(line):
    comment__single_line__regex = comment__cmds['types']["single_line"]['regex']

    match = re.match(comment__single_line__regex, line)
    if match:
        code = match.group('code')
        return code.strip()
    return line