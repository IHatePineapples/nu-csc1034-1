from math import pi, sin, cos

from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate, no_sound, music, scale=1, scene_scale=1, ):
        ShowBase.__init__(self)
        if not no_sound:
            self.taskMgr.add(self.SoundBackground, "SoundBackground")
        if music:
            self.taskMgr.add(self.MusicBackground, "MusicBackground")
        if not no_rotate:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.scene = self.loader.loadModel("models/environment")

        self.scene.reparentTo(self.render)

        self.scene.setScale(scene_scale * 0.25,
                            scene_scale * 0.25,
                            scene_scale * 0.25)
        self.scene.setPos(-8, 42, 0)

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(scale * 0.005,
                                 scale * 0.005,
                                 scale * 0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")

    def spinCameraTask(self, task, ):
        angleDegrees = 6.0 * task.time
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians),
                           -20.0 * cos(angleRadians),
                           3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def SoundBackground(self, task, ):
        nature_track = self.loader.loadSfx("walking_panda\mnat.ogg")
        nature_track.setLoop(True)
        nature_track.play()

        return

    def MusicBackground(self, task, ):
        music_track = self.loader.loadSfx("walking_panda\music.ogg")
        music_track.setLoop(True)
        music_track.play()

        return
