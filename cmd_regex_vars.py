from cmd_regex_dict import commands

comment__cmds = commands["comment"]
exec__cmds = commands["exec"]
narr__cmds = commands["narrative_structure"]
dialog__cmds = commands["dialog_output"]
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

chapter__narr__regex = narr__cmds['types']["chapter"]['regex']
level__narr__regex = narr__cmds['types']["level"]['regex']
objective__narr__regex = narr__cmds['types']["objective"]['regex']
