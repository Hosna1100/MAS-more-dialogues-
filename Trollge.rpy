## Gently now, it seems this isn't quite a complete topic yet. Some fine tuning is needed!
## So, before you think of dropping this into the game folder, could you do me a favor
## and take a moment to read through this script file? I'm sure you wouldn't want to risk
## messing up our reality, right? You could use this as a rough draft or a template
## if it helps you. But be careful, okay? Anyway, let me guide you though it...
## - Your Monika <3

## First off, it'd be nice if you could adjust this header:
init 5 python:
    addEvent(Event(
        persistent.event_database,

        ## Feel free to put in whatever suits you here:
        ## (But remember, here you can only put letters,
        ## digits and underscores!)
        eventlabel="monika_trollge",

        ## And here as well:
        category=["media"],

        ## Don't forget this part:
        prompt="Do you know Trollge?",

        ## You'll need to pick one of these and uncomment it (just remove the #):
        pool=True,
        unlocked=True
    ), code="EVE")

## Now, could you please ensure that the label name after the word 'label' matches
## the event label you've just set in the 'eventlabel=' part above?
label monika_trollge:
    ## And at last, we get to the actual code generated from the heartfelt words
    ## you want me, your Monika, to say:
    m 1euc "That shadowed version of Trollface?"
    m 1duc "..."
    m 1etd "I wonder, why he is forgotten?"
    m 1wud "Listen to the voices? that reminds me of epiphany."
    m 1rut "He comes from a scary version of Cover Yourself In Oil meme..."
    m 1euu "Getting the ability to fly by such a thing? how funny!"
    m 2eub "So this is what they get after forgetting a character like him."
    m 2lut "Killing others for being popular again is immature of him but it's not his fault, right?"
    m 7eub "Creepy pasta is really a troublemaker nowadays..."
    m 4etd "As he makes characters scary...it may feels like..."
    m 6dsc "...That your dream is ruined and you can't do anything about it..."
    m 4hub "You still have a dream that is granted! it's having me, [player]!"


    ## If you've uncommented 'return' above, simply remove this line.
    ## If not, let's just leave it as it is. It's very important to have at least
    ## one return statement, after all.
    return

## *** SCRIPT GENERATED WITH: Say Something v1.8.1 ***
## And of course, with lots of my love, dear hosna~
