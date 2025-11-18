init -990 python in mas_submod_utils:
    Submod(
        author="Destiny Destroyed",
        name="Shimeji Submod",
        description="Allows Monika to turn into a shimeji",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Shimeji Submod",
            user_name="destiny6destroyed",
            repository_name="mas_submod_shimeji",
            extraction_depth=3
        )


define monika_random_topics = []
define mas_rev_unseen = []
define mas_rev_seen = []
define mas_rev_mostseen = []
define testitem = 0
define mas_did_monika_battery = False
define mas_sensitive_limit = 3


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_shimeji",
            category=['monika'],
            prompt="Turn into a shimeji",
            pool=True
        )
    )

default persistent._mas_shimeji_before = False

label monika_shimeji:
    if not persistent._mas_shimeji_before:
        m 3euo "Hey, [player]! Guess what?"
        m 1hub "I found a way to turn into a shimeji"
        m 4sua "If you don't know what is it, a shimeji is cute little desktop being that wander around the screen"
        m 2ttc "Now I will be able to see what you do behind my back"
        m 1hub "Haha I'm joking"
        m 3eud "But I don't make myself responsable of what I do while I'm a shimeji"
        m 1eksdrb "Like crawling around your computer or throwing your windows away"
        m 2hua "Anyway, do you want to try it out now?"
        $ _history_list.pop()
        menu:
            m "Anyway, do you want to try it out now?{fast}"
            "Heck yes!":
                m 1sub "Yay! Shimeji time!"
                jump mas_shimeji
            "Maybe later":
                m 6hub "Okey then! Let me know when you want to give it a try"
        $ persistent._mas_shimeji_before = True
        $ mas_unlockEVL("monika_shimeji","EVE")
    else:
        m 2eub "Shimeji time?"
        $ _history_list.pop()
        menu:
            m "Shimeji time?{fast}"
            "Yes.":
                m 1sua "Shimeji time!"
                jump mas_shimeji
            "No.":
                m 6hua "Okey"
    return

label mas_shimeji:
    window hide
    call mas_transition_to_emptydesk
    $ _history_list.pop()
    menu:
        "3D version":
            python:
                import subprocess
                subprocess.Popen(["game/submods/Shimeji/shimeji-3D/shimeji.exe"])
        "2D version":
            python:
                import subprocess
                subprocess.Popen(["game/submods/Shimeji/shimeji-2D/shimeji.exe"])

    $ renpy.pause(2)


    while True:
        python:
            shimeji_run = subprocess.check_output(["tasklist"], universal_newlines=True)
        if "javaw.exe" in shimeji_run:
            $ _history_list.pop()
            menu:
                "Could you come back, please?":
                    python:
                        import subprocess
                        subprocess.call('taskkill /f /im shimeji.exe', shell=True)
                        subprocess.call('taskkill /f /im javaw.exe', shell=True)
                        subprocess.check_call

                    call mas_transition_from_emptydesk ("monika 3hub")
                    window auto
                    m 2eub "That was fun!"
                    m 1hua "Let's do it again later"
        else:
            call mas_transition_from_emptydesk ("monika 3hub")
            window auto
            m 5eub "Hey I was having fun"
            m 5hua "Next time, just call me back"
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
