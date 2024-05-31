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
        eventlabel="monika_modding",

        ## And here as well:
        category=["mod"],

        ## Don't forget this part:
        prompt="What is Ren'py?",

        ## You'll need to pick one of these and uncomment it (just remove the #):
        pool=True,
        unlocked=True
    ), code="EVE")

## Now, could you please ensure that the label name after the word 'label' matches
## the event label you've just set in the 'eventlabel=' part above?
label monika_modding:
    ## And at last, we get to the actual code generated from the heartfelt words
    ## you want me, your Monsa, to say:
    m 4eub "Ren'py is a programming language for creating visual novels and it mades with Python."
    m 4eub "And this game mades with both python and Ren'py but the modding for DDLC need more files in general."
    m 2eub "For creating something in Ren'py itself, we need four files that are:"
    m 2eub "options.rpy{w=0.5} gui.rpy{w=0.5} screens.rpy and script.rpy"
    m 4eud "In mod template, we need more files than those four!"
    show monika 5lud at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5lud "like definitions{w=0.5} script_ch1{w=0.1} and so on...."
    show monika 3eud at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3eud "Although, modding DDLC is the easiest one I've ever seen."
    m 1rud "You have to add sprites for the mod to be interesting."
    m 1wud "The After Story that I'm in is the first and for most DDLC mod!"
    m 1euu "The dialogs and images codes are the easiest to start with but other part like choices are a bit difficult to learn."
    m 1rup "Other Monikas in the mods always forget that there's a mod for them that is an After Story..."
    m 1ett "Did modders forgot about Monika After Story?"
    m 4hub "Anyways, thanks for listening~"
    show monika 5sublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5sublb "And who knows? Maybe you create a mod that is focused on me..."
    show monika 1hubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hubsb "Ehehe~"

    return 

## *** SCRIPT GENERATED WITH: Say Something v1.8.1 ***
## And of course, with lots of my love, dear hosna~
