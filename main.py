def 一音進める():
    global 音程, 現在の音
    音程 = 音楽[現在の音][0]
    if 音程 == 0:
        music.rest(音楽[現在の音][1])
    else:
        music.play_tone(音程, 音楽[現在の音][1])
    現在の音 += 1
    if len(音楽) == 現在の音:
        現在の音 = 0
def 音を再生():
    music.play_tone(87, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(130, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(87, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(130, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(87, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(130, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(87, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.HALF))
現在の音 = 0
音程 = 0
音楽: List[List[number]] = []
basic.pause(1000)
音楽 = [[87, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [130, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [87, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [130, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [87, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [130, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [87, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [311, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [311, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [233, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [494, music.beat(BeatFraction.HALF)],
    [466, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.WHOLE)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [311, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [311, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [262, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [330, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [233, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [494, music.beat(BeatFraction.HALF)],
    [466, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.DOUBLE)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [698, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [698, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.HALF)],
    [440, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [523, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.HALF)],
    [294, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.HALF)],
    [349, music.beat(BeatFraction.QUARTER)],
    [0, music.beat(BeatFraction.QUARTER)],
    [330, music.beat(BeatFraction.HALF)],
    [0, music.beat(BeatFraction.DOUBLE)]]

def on_forever():
    if input.light_level() > 30:
        一音進める()
basic.forever(on_forever)
