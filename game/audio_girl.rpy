init python:

    def girl_speak(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            import random
            r = random.randint(0, 2)

            if r == 0:
                renpy.sound.play("audio/girl1.wav", channel="sound")
            elif r == 1:
                renpy.sound.play("audio/girl2.wav", channel="sound")
            else:
                renpy.sound.play("audio/girl3.wav", channel="sound")

        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")