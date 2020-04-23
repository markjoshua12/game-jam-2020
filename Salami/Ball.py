
import arcade
from Mob import Mob

class Ball(Mob):

    def update(self):
        
        # collision_list = arcade.check_for_collision_with_list(self, self.level.entities)

        # for entity in collision_list:
        #     if entity == self:
        #         continue

        #     if self.change_x != 0:
        #         self.change_x += entity.change_x
        #         self.change_x *= -0.9
        #     if self.change_y != 0:
        #         self.change_y += entity.change_y
        #         self.change_y *= -0.9

        if self.change_x > 12:
            self.change_x = 12
        elif self.change_x < -12:
            self.change_x = -12
        if self.change_y > 12:
            self.change_y = 12
        elif self.change_y < -12:
            self.change_y = -12

        super().update()
        # print(f"{self.change_x} {self.change_y}")

    def move(self, dx: float, dy: float):
        
        if dy != 0:
            self.center_y += dy

            collision_list_y = arcade.check_for_collision_with_list(self, self.level.engine.tiles)

            for entity in collision_list_y:
                if self.intersects(entity):
                    if self.change_y > 0:
                        self.center_y = entity.center_y - self.width
                    elif self.change_y < 0:
                        self.center_y = entity.center_y + entity.width
                    self.change_y *= -0.8
        if dx != 0:

            self.center_x += dx
            collision_list_x = arcade.check_for_collision_with_list(self, self.level.engine.tiles)

            for entity in collision_list_x:

                if self.intersects(entity):
                    if self.change_x > 0:
                        self.center_x = entity.center_x - self.width
                    elif self.change_x < 0:
                        self.center_x = entity.center_x + entity.width
                    self.change_x *= -0.6