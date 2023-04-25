# CS2520 Assignment6 - Refactoring graphics_v4.py: George Matta, Mark Haddad, Ayanna Sanges-Chu
This project explores refactoring the graphics_v4.py file from https://github.com/johoule/stuff. We've structured the program from being one file
into different classes that are structured in functions. The project is also strucured modularly, as each of the classes execute different aspects of
building the environment, in which each of the classes utilize the other classes amongst each other.

# Installation and Running
- Go to desired directory for storing the project (e.g. Desktop: `cd Desktop`)

- Clone the repo: `git clone https://github.com/iHeroGH/Assignment6.git`

- Install pygame: `pip3 install pygame`

- Run: `cd MajorLeagueSoccerAnim`, `python3 graphics_v4.py`

# Project Details
### artist.py
Defines a class Artist that draws each of the individual parts to the environment, all in separate functions. The Artist class utilizes
the colors listed in the Color class. Functions include move_clouds(), draw_grass(), draw_goal(), etc.

### color.py
Defines all of the colors used in the project in a separate Color class.

### config.py
This file defines a class Config, which utlizes the Color class. The class consists of functions that define boolean statements on different aspects of the environment.
These aspects include the color of the sky, cloud color, field color etc, as the colors are manipulated into day or night "mode" based on day or lights_on is True.

### pygame_handler.py
Handles all the non-visual Pygame operations (like events) of the project.
The handler is the main delegator for the operation, checking configuration 
settings, calling draw methods, and initializing/maintaining the Pygame surfaces. 
In this class, Config and Artist objects are defined as attributes when the Handler is initialized, and are utilized in the other functions.
The main game loop is also held in this class.

### graphics_v4.py
This is the main executable file that has been minimized to just creating Config, Artist, and PygameHandler object to run the project. The Handler passes in
the Artist and Config, and runs the game_loop function which utilizes these classes.

# Credits
Project created by George Matta, Mark Haddad, and Ayanna Sanges-Chu for CS2520 Assignment 6.
