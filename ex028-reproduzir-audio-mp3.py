from pygame import init, mixer, event
init()
mixer.music.load('ex028-firme.mp3')
mixer.music.play()
input()
event.wait()
