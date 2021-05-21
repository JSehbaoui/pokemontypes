import pygame
import math

#angle in degrees
class Polygon:
    def __init__(self, angle, size, color, pos) -> None:
        self.angle = angle
        self.size = size
        self.color = color

        kante = size*0.35

        point1 = pos
        point2 = (math.sin(math.radians(angle))*size + point1[0],                             math.cos(math.radians(angle))*size + point1[1])
        point3 = (math.sin(math.radians(angle+90))*size + point1[0],                          math.cos(math.radians(angle+90))*size + point1[1])
        point4 = (math.sin(math.radians(angle+90))*kante+point2[0],               math.cos(math.radians(angle+90))*kante+point2[1])
        point5 = (math.sin(math.radians(angle))*kante+point3[0],                  math.cos(math.radians(angle))*kante+point3[1])
        point6 = (math.sin(math.radians(angle+180))*(size-kante)+point4[0],       math.cos(math.radians(angle+180))*(size-kante)+point4[1])

        self.points = [point1, point2, point4, point6, point5, point3]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
