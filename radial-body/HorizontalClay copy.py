import pygame as game

from App import *
from VerletPhysics import *


class DemoRope(App):
    #
    world    = World(Vector(640.0, 480.0), Vector(0, 0), 4)
    #
    grabbed  = None
    radius   = 15
    strength = 0.02


    #
    def Initialize(self):
        #
        rope = self.world.AddComposite()
        mat = Material(1.0,1.0,1.0)
        rope.AddParticles(
            self.world.AddParticle(20.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(40.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(60.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(80.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(100.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(120.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(140.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(160.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(180.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(200.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(220.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(240.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(260.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(280.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(300.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(320.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(340.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(360.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(380.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(400.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(420.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(440.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(460.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(480.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(500.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(520.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(540.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(560.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(580.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(600.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(620.0,self.world.hsize.y,Material(1.0,0.0,1.0))
        )
        
        rope.AddConstraints(
            self.world.AddConstraint(rope.particles[0], rope.particles[1], 0.5),
            self.world.AddConstraint(rope.particles[1], rope.particles[2], 0.5),
            self.world.AddConstraint(rope.particles[2], rope.particles[3], 0.5),
            self.world.AddConstraint(rope.particles[3], rope.particles[4], 0.5),
            self.world.AddConstraint(rope.particles[4], rope.particles[5], 0.5),
            self.world.AddConstraint(rope.particles[5], rope.particles[6], 0.5),
            self.world.AddConstraint(rope.particles[6], rope.particles[7], 0.5),
            self.world.AddConstraint(rope.particles[7], rope.particles[8], 0.5),
            self.world.AddConstraint(rope.particles[8], rope.particles[9], 0.5),
            self.world.AddConstraint(rope.particles[9], rope.particles[10], 0.5),
            self.world.AddConstraint(rope.particles[10], rope.particles[11], 0.5),
            self.world.AddConstraint(rope.particles[11], rope.particles[12], 0.5),
            self.world.AddConstraint(rope.particles[12], rope.particles[13], 0.5),
            self.world.AddConstraint(rope.particles[13], rope.particles[14], 0.5),
            self.world.AddConstraint(rope.particles[14], rope.particles[15], 0.5),
            self.world.AddConstraint(rope.particles[15], rope.particles[16], 0.5),
            self.world.AddConstraint(rope.particles[16], rope.particles[17], 0.5),
            self.world.AddConstraint(rope.particles[17], rope.particles[18], 0.5),
            self.world.AddConstraint(rope.particles[18], rope.particles[19], 0.5),
            self.world.AddConstraint(rope.particles[19], rope.particles[20], 0.5),
            self.world.AddConstraint(rope.particles[20], rope.particles[21], 0.5),
            self.world.AddConstraint(rope.particles[21], rope.particles[22], 0.5),
            self.world.AddConstraint(rope.particles[22], rope.particles[23], 0.5),
            self.world.AddConstraint(rope.particles[23], rope.particles[24], 0.5),
            self.world.AddConstraint(rope.particles[24], rope.particles[25], 0.5),
            self.world.AddConstraint(rope.particles[25], rope.particles[26], 0.5),
            self.world.AddConstraint(rope.particles[26], rope.particles[27], 0.5),
            self.world.AddConstraint(rope.particles[27], rope.particles[28], 0.5),
            self.world.AddConstraint(rope.particles[28], rope.particles[29], 0.5),
            self.world.AddConstraint(rope.particles[29], rope.particles[30], 0.5)
        )

        rope.particles[0].material.mass = 0.0
        rope.particles[-1].material.mass = 0.0

        #rope.particles[9].ApplyForce(Vector(400.0, -900.0))


    #
    def Update(self):
        #
        if game.mouse.get_pressed()[0]:
            if self.grabbed == None:
                closest = self.ClosestPoint()
                if closest[1] < self.radius:
                    self.grabbed = closest[0]
                print('here')
            if self.grabbed != None:
                mouse = Vector(game.mouse.get_pos()[0], game.mouse.get_pos()[1])
                force = (mouse - self.grabbed.position) * self.strength
                self.grabbed.ApplyImpulse(force)
                print('here2')        
            self.world.Simulate()
        else:
            if self.grabbed != None:
                self.world.SimulateWorldStop() 
                self.grabbed = None
            print('here3')
    
        #
        if game.key.get_pressed()[game.K_ESCAPE]:
            self.Exit()


    #
    def Render(self):
        #
        self.screen.fill((24, 24, 24))
        for c in self.world.constraints:
            pos1 = (int(c.node1.position.x), int(c.node1.position.y))
            pos2 = (int(c.node2.position.x), int(c.node2.position.y))
            game.draw.line(self.screen, (255, 0, 0), pos1, pos2, 4)
        for p in self.world.particles:
            pos = (int(p.position.x), int(p.position.y))
            game.draw.circle(self.screen, (255, 255, 255), pos, 8, 0)
        game.display.update()


    #
    def ClosestPoint(self):
        mouse    = Vector(game.mouse.get_pos()[0], game.mouse.get_pos()[1])
        closest  = None
        distance = float('inf')
        for particle in self.world.particles:
            d = mouse.distance(particle.position)
            if d < distance:
                closest  = particle
                distance = d
        return (closest, distance)


if __name__ == "__main__":
    print ("Starting...")
    app = DemoRope("Swinging Rope", 640, 480, 30)
    app.Run()
    print ("Ending...")
