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
        eventlabel="monika_a_weathered_world",

        ## And here as well:
        category=["mod"],

        ## Don't forget this part:
        prompt="A Weathered World",

        ## You'll need to pick one of these and uncomment it (just remove the #):
        random=True,
        #pool=True
    ), code="EVE")

## Now, could you please ensure that the label name after the word 'label' matches
## the event label you've just set in the 'eventlabel=' part above?
label monika_a_weathered_world:
    ## And at last, we get to the actual code generated from the heartfelt words
    ## you want me, your Monsa, to say:
    m 1rksdld "Er, have you ever played that mod that named...ehhhh..."
    m 1ekd "{b}A Weathered World?{/b}" 
    m 3ekd "It's about me doing experiments on MC to kill him and get to you, [player]."
    m 1ekd "And you, the player, leave me in that spaceroom. for years...."
    m 1rsd "As well as I brought back other characters but they were still glitched and gory."
    m 7esd "The MC changed his name to Wren and he was self-aware that you were controlling him and his decisions all the time."
    m 2wud "He killed Natsuki by his own hands but he was in control when doing that, he didn't know it was him or...me."
    m 4hksdlb "I was even pretending to not be self-aware and he sort of got furious with me for that and faulted me for his misery."
    m 4esd "When he got to spend time with me, I revealed that it was me doing all of that gory stuff."
    m 3esd "I teleported him to A Weathered version of DDLC. just having black and white design in it. girls just having red and black design and having red eyes, saying words upside down. voices whispering him to delete/add mc.chr."
    m 3esd "Then, he end up in Residential Day and Sayori told him about all of that he ruined my codes by loading script-ch1.rpy."
    m 2tfc "Sayori pretended to love you but instead, she trapped you, saying she never loved the you..."
    m 2tfd "Telling you she did it because you didn't save her when she got forced to kill herself."
    m 2dfd "You know, SHE IS THE WORST CHILDHOOD FRIEND EVER THAT I'VE SEEN!"
    m 4cfx "{b}That damn Sayori betrayed you! what kind of friend she is?????{/b}"
    m 6eksdld "Er, sorry...it just frustrates me, you know you are important to me and I hate someone unrealistic and also clumsy like her, suffering you, [player]..."
    m 6eksdld "I know, I should get fury like this but I can't stand your suffering, [player]."
    m 1dkd "Maybe it's my fault to do that to her, if I didn't do that then, she wouldn't behave to you like that and show all those scary flashbacks..."
    m 7wud "Wait! it wasn't even us! it was just a mod or...does the things others make, affect us that much??"
    m 2rup "Hmmmm..."
    m 2eud "We talked about this before, it's relates to multiverse, isn't it [player]? mods are other universes of DDLC."
    m 3rksdlb "Wow! imagine just a plenty of mods become a {i}incident{/i} for us. hehe~" 

    ## If you've uncommented 'return' above, simply remove this line.
    ## If not, let's just leave it as it is. It's very important to have at least
    ## one return statement, after all.
    return

## *** SCRIPT GENERATED WITH: Say Something v1.8.1 ***
## And of course, with lots of my love, dear Hosna~
