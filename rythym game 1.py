#define the class that keeps the beat
class conductor:
    bpm = 180.0
    def __init__(self, beatTime, songPosition):
        self.beatTime = beatTime
        self.songPosition = songPosition