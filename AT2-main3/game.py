import pygame
from menu import MainMenu
from character_select import CharacterSelect
from map import Map
from assets import load_assets, GAME_ASSETS
from gamedone import GameDone


class Game:
    def __init__(self):
        pygame.init()
        load_assets()  # load the game image assets
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.menu = MainMenu(self.window)  # Create an instance of the MainMenu class
        self.character_select = CharacterSelect(self.window)  # Create an instance of the CharacterSelect class
        self.game_map = Map(self.window)  # Create an instance of the Map class
        self.state = 'menu'  # Set the initial state to 'menu'
        self.current_character = None  # To store the chosen character

    def run(self):
        while True:
            if self.state == 'menu':  # If the state is 'menu'
                result = self.menu.run()  # Run the menu and get the result
                if result == 'Start Game':  # If the result is 'Start Game'
                    self.state = 'character_select'  # Change the state to 'character_select'
                elif result == 'Settings':  # If the result is 'Settings'
                    pass  # Settings handling would go here
                elif result == 'Exit':  # If the result is 'Exit'
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method

            elif self.state == 'character_select':  # If the state is 'character_select'
                selected_character = self.character_select.run()  # Run the character select screen and get the selected character
                if selected_character == 'back':  # If the selected character is 'back'
                    self.state = 'menu'  # Change the state to 'menu'
                elif selected_character:  # If a character is selected
                    self.current_character = selected_character  # Set the current character to the selected character
                    self.game_map.load_player(selected_character)  # Load the selected character into the game map
                    self.state = 'game_map'  # Change the state to 'game_map'

            elif self.state == 'game_map':  # If the state is 'game_map'
                game_state = self.game_map.gameState()

                if game_state == "Combat":
                    result = self.game_map.inCombat()

                    if result == "lose":
                        pygame.quit()
                        return
                    if result == "won combat":
                        game_state = "Regular"
                        
                elif game_state == "Regular":
                    result = self.game_map.handle_events()
                    if result == 'back':  # If the result is 'back'
                        self.state = 'character_select'  # Change the state to 'character_select'
                    elif result == 'quit':  # If the result is 'quit'
                        pygame.quit()  # Quit pygame
                        return  # Exit the run method
                    else:
                        self.game_map.draw()  # Draw the game map
            elif self.state == 'game_over':
                game_done = GameDone(self.window)
                result = game_done.run()
            for event in pygame.event.get():  # Iterate over the events in the event queue
                if event.type == pygame.QUIT:  # If the event type is QUIT
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method
                



if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.run()  # Run the game

