console.log("NeckBeard Games Presents")
time.sleep(100/1000)
console.log("CodeWars")
time.sleep(100/1000)
console.log("Copyright 2017")
console.log("Loading...")
time.sleep(2000/1000)
console.clear()

# start(Chapter("Tutorial", {
#     'levels': [
#         Level("Intro")
#     ]
# }))

player = Player()
assistant = NPC("Diana")

start(Chapter("Tutorial")
    'levels': [
        Level("Intro", {
            'events': [
                dialog(assistant,
                    "This is {self.name}, your handler for this mission".format(self=assistant))
                dialog(assistant,
                    "What is your name?")
                name = input()
                player.name = name
                dialog(assistant,
                    "Good to meet you, {player.name}".format(player=player))

                dialog(assistant,
                    "Your first mission should you choose to accept it, is to talk to our asset, and convince him to reveal intel")
                get_this_input('', "Press Enter to accept mission")
                dialog(player, "I accept")
                console.log("Connecting to asset...")

                asset1 = NPC("Ron")
                dialog(asset1,
                    "Hey this is {self.name}. I have some information that is useful to you. But I won’t give it up to anybody.".format(self=asset1))
                dialog(asset1,
                    " If you want it, you have to answer this question, so I know you aren't a total n00b, ok?")
                get_this_input('', "Press Enter to get question")
                dialog(player, "OK")
                objective = Objective("Basic question", {
                    'text': """
                            What is the output of this program?
                            >>> a = 2
                            >>> b = a
                            >>> b = 3
                            >>> print(a)
                            """,
                    'answer': 2
                })
                answer = None
                while answer != 2:
                    give_objective(asset1, objective)
                    answer = get_typed_input(int, "Please enter your answer (hint: it's an int)")
                    if answer == 2:
                        dialog(asset1, "Good job! I knew you were competant")
                        break
                    else:
                        dialog(asset1, "Wow you are a fool, I will never trust you.")
            ]
        })
    ]
}))
