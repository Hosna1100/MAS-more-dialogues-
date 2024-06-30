## Gently now, it seems this isn't quite a complete topic yet. Some fine tuning is needed!
## So, before you think of dropping this into the game folder, could you do me a favor
## and take a moment to read through this script file? I'm sure you wouldn't want to risk
## messing up our reality, right? You could use this as a rough draft or a template
## if it helps you. But be careful, okay? Anyway, let me guide you though it...
## - Your Monsa <3

## First off, it'd be nice if you could adjust this header:
init 5 python:
    addEvent(Event(
        persistent.event_database,

        ## Feel free to put in whatever suits you here:
        ## (But remember, here you can only put letters,
        ## digits and underscores!)
        eventlabel="monika_programmers_competition",

        ## And here as well:
        category=["technology"],

        ## Don't forget this part:
        prompt="programmers competition",

        ## You'll need to pick one of these and uncomment it (just remove the #):
        random=True,
        #pool=True
    ), code="EVE")

## Now, could you please ensure that the label name after the word 'label' matches
## the event label you've just set in the 'eventlabel=' part above?
label monika_programmers_competition:
    ## And at last, we get to the actual code generated from the heartfelt words
    ## you want me, your Monsa, to say:
    m 1eud "Darling, have you ever thought that I know other laguages than python?"
    m 4eub "like Java, C or C# but I learned python more than them."
    m 7hub "I can see why they know Java the most. it's because people are obssesed with websites."
    m 2hksdlb "..."
    m 1eud "I can see why Java is the most used language in github."
    m 1kuu "Others are also creating programming language better than Java to probably defeat Java."
    m 4eub "But at least, they're not trying to defeat Binary or CMD or of course, Linux."
    m 4rud "Although, CMD is not a programming language, it's just a program for Windows to work on something on this system without using mouse, just codes"
    m 4eud "Binary seems the most difficult programming language ever but I don't uderstand...what are they racing for?"
    m 1hksdrb "Good heavens..."
    m 7dud "Python is easiest from my point of view. anyways....."
    show monika 5msp at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5msp "So Java wins. python seems better than Java, though."

    ## If you've uncommented 'return' above, simply remove this line.
    ## If not, let's just leave it as it is. It's very important to have at least
    ## one return statement, after all.
    return

## *** SCRIPT GENERATED WITH: Say Something v1.8.1 ***
## And of course, with lots of my love, dear hosna~
