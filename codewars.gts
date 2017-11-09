/*
@people
#objects
%tasks

! console
> output
$ input
// comment
\ exec?
/*


\load objects from objects
\load characters
\load tasks

\be me = @player  // start game
! NeckBeard Games Presents
\delay 100ms
! CodeWARS
\delay 100ms
! Copyright 2017
! loading...
\delay 2000ms
$ (Press n to continue)
\clear  // clears the screen

/* start tutorial chapter */
# Tutorial  // start chapter
## Intro  // start level
### Accept mission  // start objective
> [diana] This is Diana, your handler for this mission.
> What is your name?
$ name
\assign @player.name = name
> [diana] Good to meet you, {@player.name}
> Your first mission should you choose to accept it, is to talk to our asset, and convince him to reveal intel.
$ (Press Enter to accept mission)
> [player] I accept.
! Connecting to asset...
> [asset1] Hey this is {@asset1.name}. I have some information that is useful to you. But I won’t give it up to anybody.
> [asset1] If you want it, you have to answer this question, so I know you aren't a total n00b, ok?
$ (Press Enter to get question)
> [player] OK.
* @asset1 requests %question1
$ (Please enter your answer) $answer:int from [2|3]
\end me
