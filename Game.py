import pygame
from config import Person
from config import Package

person1 = Person()
package1 = Package()

pygame.init()

# Create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Package Display Game")

# Define button properties
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60
BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2  # Center the button horizontally
BUTTON_Y = SCREEN_HEIGHT - BUTTON_HEIGHT - 50  # Place button near the bottom

# Define button colors
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 255, 255)
TEXT_COLOR = (255, 255, 255)

# Function to draw a button
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # End the game loop
    return True  # Continue the game loop

# Function to update the screen
def update_screen(package, button_hovered):
    # Fill the screen with a white color to clear the previous frame
    screen.fill((255, 255, 255))

    # Draw the button
    button_color = BUTTON_HOVER_COLOR if button_hovered else BUTTON_COLOR
    draw_button(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, button_color, "Show Package")

    # If the button is clicked, display the package image
    if package["shown"]:
        package["obj"].display(100, 100, screen)

    # Update the display
    pygame.display.update()

# Main game loop
def main():
    running = True

    # Create person and package objects
    person1 = Person()
    package_image_path = "package.png"  # Make sure this path is correct
    package = Package(image_path=package_image_path)

    # Track whether the package image should be shown
    package_data = {"obj": package, "shown": False}

    # Game loop
    while running:
        # Handle events
        running = handle_events()

        # Get the mouse position and check if it is over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_hovered = (BUTTON_X <= mouse_x <= BUTTON_X + BUTTON_WIDTH) and (BUTTON_Y <= mouse_y <= BUTTON_Y + BUTTON_HEIGHT)

        # Check if the button is clicked
        if pygame.mouse.get_pressed()[0] and button_hovered:
            package_data["shown"] = True  # Show the package when the button is clicked

        # Update the screen with the package image if the button was clicked
        update_screen(package_data, button_hovered)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()