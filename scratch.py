import random
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.uix.widget import Widget
from kivy.vector import Vector

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def ball_bounce(self):
        x,y = self.pos
        if y+ self.size[0]>self.height:
            self.velocity[1]=-self.velocity[1]
        if y<0:
            self.velocity[1] = -self.velocity[1]

        if x+ self.size[0]>self.width:
            self.velocity[0]=-self.velocity[0]
        if x  < 0:
            self.velocity[0] = -self.velocity[0]

class Hero(Widget):
    score = NumericProperty(0)
    hscore = NumericProperty(0)


class PongGame(Widget):
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = ObjectProperty(None)
    hero = ObjectProperty(None)
    start_enabled_start = BooleanProperty(False)

    px = random.random()
    py = random.random()
    state_game_over = False



    def serve_ball(self, velx,vely):

        self.ball1.center = self.center_x,self.center_y
        self.ball1.velocity = (-velx,vely)
        self.ball2.center = self.center
        self.ball2.velocity = (velx/2,vely*1.5)
        self.ball3.center = self.center_x,self.center_y
        self.ball3.velocity = (velx,vely)





    def ball_bounce(self):
        x,y = self.ball1.pos
        if y+ self.ball1.size[0]>self.height:
            self.ball1.velocity[1]=-self.ball1.velocity[1]
        if y<0:
            self.ball1.velocity[1] = -self.ball1.velocity[1]

        if x+ self.ball1.size[0]>self.width:
            self.ball1.velocity[0]=-self.ball1.velocity[0]
        if x  < 0:
            self.ball1.velocity[0] = -self.ball1.velocity[0]
        x2,y2 = self.ball2.pos
        if y2+ self.ball2.size[0]>self.height:
            self.ball2.velocity[1]=-self.ball2.velocity[1]
        if y2<0:
            self.ball2.velocity[1] = -self.ball2.velocity[1]

        if x2+ self.ball2.size[0]>self.width:
            self.ball2.velocity[0]=-self.ball2.velocity[0]
        if x2  < 0:
            self.ball2.velocity[0] = -self.ball2.velocity[0]
        x3,y3 = self.ball3.pos
        if y3+ self.ball3.size[0]>self.height:
            self.ball3.velocity[1]=-self.ball3.velocity[1]
        if y3<0:
            self.ball3.velocity[1] = -self.ball3.velocity[1]

        if x3+ self.ball3.size[0]>self.width:
            self.ball3.velocity[0]=-self.ball3.velocity[0]
        if x3 < 0:
            self.ball3.velocity[0] = -self.ball3.velocity[0]


    def game_over(self):
        p1,p2=self.hero.pos
        x,y = self.ball1.pos
        x2,y2 = self.ball2.pos
        x3,y3 = self.ball3.pos

        if (p1-x)**2+(p2-y)**2<=2500 or (p1-x2)**2+(p2-y2)**2<=2500  or (p1-x3)**2+(p2-y3)**2<=2500:
            print("game over")
            self.state_game_over = True
            self.start_enabled_start = False
            if self.hero.score> self.hero.hscore:
                self.hero.hscore= self.hero.score
            self.hero.score=0

    def game_reset(self):
        #print(self.state_game_over, self.start_enabled_start)

        #if self.start_enabled_start == True:
        self.state_game_over = False
        self.serve_ball(1,1)
        self.hero.center_x = 25

        self.hero.center_y = 25

    def update(self, dt):
        #if not self.state_game_over:
        if self.start_enabled_start:

            self.ball1.move()
            self.ball2.move()
            self.ball3.move()
            self.ball_bounce()
            self.hero.score+=1
            self.game_over()
            if self.state_game_over== True:
                print(self.start_enabled_start,self.state_game_over)

                self.game_reset()

    def on_touch_move(self, touch):
        if self.start_enabled_start:

            self.hero.center_x = touch.x
            self.hero.center_y = touch.y

    def on_button_click_s(self, clickfunm):
        self.start_enabled_start = True
        print("clicked"+str(self.start_enabled_start))









class PongApp(App):


    def build(self):
        game = PongGame()

        print("111")
        game.serve_ball(1,1)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()