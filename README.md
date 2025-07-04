# python_game

# Creating a Pygame Window and Responding to User Input

We’ll make an empty Pygame window by creating a class to represent the
game. In your text editor, create a new file and save it as alien_invasion.py;
then enter the following:

```python
🔴 alien_invasion.py

import sys 

import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invansion")
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            pygame.display.flip()
    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
```

First, we import the `sys` and `pygame` modules. The `pygame` module contains the functionality we need to make a game. We’ll use tools in the `sys` module to exit the game when the player quits.

Alien Invasion starts as a class called `AlienInvasion`. In the `__init__()` method, the `pygame.init()` function initializes the background settings that Pygame needs to work properly.

we call `pygame.display.set_mode()` to create a display window, on which we’ll draw all the game’s graphical elements. The argument `(1200, 800)` is a tuple that defines the dimensions of the game window, which will be 1200 pixels wide by 800 pixels high. (You can adjust these values depending on your display size.) We assign this display window to the attribute `self.screen`, so it will be available in all methods in the class.

The object we assigned to `self.screen` is called a surface. A surface in Pygame is a part of the screen where a game element can be displayed. Each element in the game, like an alien or a ship, is its own surface. The surface returned by `display.set_mode()` represents the entire game window.

When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.

The game is controlled by the `run_game()` method. This method contains a while loop that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write this event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur. The `for` loop at is an event loop.

To access the events that Pygame detects, we’ll use the `pygame.event.get()` function. This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event will cause this `for` loop to run. Inside the loop, we’ll write a series of `if` statements to detect and respond to specific events.

For example, when the player clicks the game window’s close button, a `pygame.QUIT` event is detected and we call `sys.exit()` to exit the game.

The call to `pygame.display.flip()` tells Pygame to make the most recently drawn screen visible. In this case, it simply draws an empty screen on each pass through the `while` loop, erasing the old screen so only the new screen is visible. When we move the game elements around, `pygame.display.flip()` continually updates the display to show the new positions of game elements and hides the old ones, creating the illusion of smooth movement.

At the end of the file, we create an instance of the game, and then call `run_game()`. We place `run_game()` in an `if` block that only runs if the file is called directly.

When you run this `alien_invasion.py` file, you should see an empty Pygame window.

___



## 🎨 Setting a Custom Background Color in Pygame

Pygame creates a black screen by default, but that’s boring. Let’s set a different background color.

We’ll do this at the end of the `__init__()` method.

### 🧱 Code Example

```python
🔴 alien_invasion.py

def __init__(self):
    # --snip--
    pygame.display.set_caption("Alien Invasion")

    # Set the background color
    self.bg_color = (230, 230, 230)  # 1

def run_game(self):
    # --snip--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Redraw the screen during each pass through the loop
    self.screen.fill(self.bg_color)  # 2

    # Make the most recently drawn screen visible
    pygame.display.flip()
```

### 🌈 RGB Colors in Pygame

Colors in Pygame are specified using **RGB (Red, Green, Blue)** values. Each component ranges from `0` to `255`.

Examples:

- `(255, 0, 0)` → Red
- `(0, 255, 0)` → Green
- `(0, 0, 255)` → Blue

You can mix RGB values to create up to **16 million** different colors.

The color `(230, 230, 230)` mixes equal amounts of red, green, and blue, resulting in a **light gray** background.

We assign this color to `self.bg_color` at **1**.

At **2**, we fill the screen with this background color using the `fill()` method, which acts on a surface and takes only one argument: the color.
