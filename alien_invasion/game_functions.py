import sys
import pygame

def check_events():
    """Respond to keypresses and mouse clicks."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new one."""
    # Redraw the screen for each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()