import re

from cmd_regex import commands

gt_filename = "codewars.greentext"

comment_cmds = commands["comments"]


def comment_strip(line):
    comment__single_line__regex = comment_cmds['types']["single_line"]['regex']

    line = line.strip()
    match = re.match(comment__single_line__regex, line)
    if match:
        code = match.group('code')
        return code.strip()
    return line


with open(gt_filename) as gt_file:
    for line in gt_file:
        # getting rid of multi line comments
        comment__multi_line_1line__regex = comment_cmds['types']["multi_line_1line"]['regex']
        multi_line_1line = re.compile(comment__multi_line_1line__regex)

        comment__multi_line_start__regex = comment_cmds['types']["multi_line_start"]['regex']
        multi_line_start = re.compile(comment__multi_line_1line__regex)

        comment__multi_line_end__regex = comment_cmds['types']["multi_line_end"]['regex']
        multi_line_end = re.compile(comment__multi_line_1line__regex)

        if multi_line_1line.match(line):
            continue
        if multi_line_start.match(line):
            line = gt_file.readline()
            while not multi_line_end.match(line):
                line = gt_file.readline()

        # strip the line and remove inline comments
        line = comment_strip(line)
        if not line:
            continue  # if line was empty after comment stripping
