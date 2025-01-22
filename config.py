import pygame

app = pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Person:
    def __init__(self):
        self.name = None
        self.sex = None
        self.house = None
        self.tolerance = None # Use this to determine the character's demeanor toward the player

class Package:
    def __init__(self, image_path):
        self.recipient = None
        self.value = None
        self.size = None
        self.weight = None
        self.name = None
        self.image_path = image_path  # Store the path to the package image
        self.image = pygame.image.load(image_path)  # Load the image

    def display(self, x, y, screen):
        """
        Display the image at a specific location (x, y) on the screen.
        """
        screen.blit(self.image, (x, y))