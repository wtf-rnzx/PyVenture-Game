import pygame
import sys
import pickle
from config import * 
from spritess import *
from button import *
import random
import textwrap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Python Maze')
        self.clock = pygame.time.Clock() 
       # self.font = pygame.font.Font('Arial', 32)
        self.running = True
        self.font = pygame.font.Font('font/retrofont.ttf', 30)
        self.intro_background =pygame.image.load('img/tryy.jpg')
        self.go_background = pygame.image.load('img/gameover.png')

        self.username = ""
        self.health = 100

        
        self.levels = [Tile_Map, Tile_Map2, Tile_Map3, Tile_Map4, Tile_Map5]  # Define the different levels
        self.current_level = 0

        self.score = 0

        self.leaderboard = []
        self.load_leaderboard()
       
        self.Character_spritesheet = Sprite_Sheet('img/character1.png')
        self.Terrain_spritesheet = Sprite_Sheet('img/terrain.png')
        self.Enemy_spritesheet = Sprite_Sheet('img/demon.png')
        self.Door_spritesheet = Sprite_Sheet('img/terrain.png')

    def draw_username(self):
        text = self.font.render(f"Player: {self.username}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 90)  # Adjust the position as needed
        self.screen.blit(text, text_rect)

    def draw_health(self):
        text = self.font.render(f"Health: {self.health}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 130)  # Adjust the position as needed
        self.screen.blit(text, text_rect)

    def draw_level_text(self):
        text = self.font.render(f"Level: {self.current_level + 1}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        self.screen.blit(text, text_rect)

    def draw_score_text(self):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 50)
        self.screen.blit(text, text_rect)


    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attack = pygame.sprite.LayeredUpdates()
        self.door = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
 
        self.CreateTileMap()

    def load_level(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attack = pygame.sprite.LayeredUpdates()
        self.door = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()

        if self.current_level == 1:
            self.CreateTileMap2()
        elif self.current_level == 2:
            self.CreateTileMap2()
        elif self.current_level == 3:
            self.CreateTileMap4()
        elif self.current_level == 4:
            self.CreateTileMap5()
        
    def CreateTileMap(self):
        for i, row in enumerate(Tile_Map):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'D':
                    Door(self, j, i)
                

    def CreateTileMap2(self):
        for i, row in enumerate(Tile_Map2):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'D':
                    Door(self, j, i)

    def CreateTileMap3(self):
        for i, row in enumerate(Tile_Map3):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'D':
                    Door(self, j, i)

    def CreateTileMap4(self):
        for i, row in enumerate(Tile_Map4):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'D':
                    Door(self, j, i)

    def CreateTileMap5(self):
        for i, row in enumerate(Tile_Map5):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    Player(self, j, i)
                if column == 'D':
                    Door(self, j, i)

    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.screen.fill(BLACK)
            text = self.font.render('You Win', True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)

            # Adding a return button to go back to the main menu
            return_button = Button(40, 540, 280, 50, WHITE, BLUE, 'Back to Main Menu', 25)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if return_button.is_pressed(mouse_pos, mouse_pressed):
                    self.intro_screen()
                    running = False

                self.screen.blit(return_button.image, return_button.rect)
                pygame.display.update()

            self.username = ""
            self.score = 0
            self.current_level = 0
            self.health = 100
            running = False  # Restart from the first level if all levels are completed
        else:
            self.load_level()
        

    def events(self):
        #game loop event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_level_text()  # Draw the level text on the screen
        self.draw_score_text() 
        self.draw_username()  # Draw the username on the screen
        self.draw_health()
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    def display_scoreboard(self):
        self.screen.fill(BLACK)
        text = self.font.render('Leaderboard', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(text, text_rect)

        y_position = 100
        delete_buttons = []
        for entry in self.leaderboard:
            username_text = self.font.render(f"{entry['username']}", True, WHITE)
            score_text = self.font.render(f"Score: {entry['score']}", True, WHITE)

            self.screen.blit(username_text, (50, y_position))
            self.screen.blit(score_text, (600, y_position))

            delete_button = DeleteButton(800, y_position, 100, 30, RED, BLACK, 'Delete', 20, entry['username'])
            delete_buttons.append(delete_button)

            y_position += 50

        return_button = Button(10, SCREEN_HEIGHT - 80, 270, 50, WHITE, BLACK, 'Return to Main Menu', 20)
        self.screen.blit(return_button.image, return_button.rect)

        for delete_button in delete_buttons:
            self.screen.blit(delete_button.image, delete_button.rect)

        pygame.display.update()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    waiting_for_input = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()

                    if return_button.is_pressed(mouse_pos, mouse_pressed):
                        waiting_for_input = False

                    for delete_button in delete_buttons:
                        if delete_button.is_pressed(mouse_pos, mouse_pressed):
                            self.delete_entry(delete_button.username)
                            self.display_scoreboard()
        
        self.update_leaderboard()
        self.intro_screen()


    def delete_entry(self, username):
        self.leaderboard = [entry for entry in self.leaderboard if entry['username'] != username]
        self.save_leaderboard()

    def load_leaderboard(self):
        try:
            # Try to load leaderboard data from the file
            with open('leaderboard.pkl', 'rb') as file:
                self.leaderboard = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, initialize an empty leaderboard
            self.leaderboard = []

    def save_leaderboard(self):
        with open('leaderboard.pkl', 'wb') as file:
            pickle.dump(self.leaderboard, file)

    def update_leaderboard(self):
        entry = {'username': self.username, 'score': self.score}

        # Check if the username is already in the leaderboard
        existing_entry = next((item for item in self.leaderboard if item['username'] == self.username), None)

        if existing_entry:
            # If the user exists, update the score if the new score is higher
            if self.score > existing_entry['score']:
                existing_entry['score'] = self.score
        else:
            # If the user does not exist, add the entry to the leaderboard
            self.leaderboard.append(entry)

        # Sort the leaderboard by score in descending order
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.save_leaderboard()


    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        restart_button = Button(50, SCREEN_WIDTH / 2, 160, 50, WHITE, BLACK, 'RESTART', 25)
        quit_button = Button(50, 350, 160, 50, WHITE, BLACK, 'QUIT', 25)

        return_button = Button(10, SCREEN_HEIGHT - 80, 270, 50, WHITE, BLACK, 'Return to Main Menu', 20)

        for sprite in self.all_sprites:
            sprite.kill()

        entry = {'username': self.username, 'score': self.score}
        self.leaderboard.append(entry)
    
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):

                self.score = 0  # Reset score
                self.current_level = 0  # Reset current level
                self.health = 100  # Reset health
                self.new()
                self.main()

            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                sys.exit()      

            if return_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro_screen()
                self.running = False


            self.screen.blit(self.go_background,(0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.screen.blit(return_button.image, return_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()   

        self.update_leaderboard()     

    def intro_screen(self):
        intro = True
        username = ""

        title_font = pygame.font.Font('font/retrofont.ttf', 50)
        title = title_font.render('PyVenture', True, RED)
        title_rect = title.get_rect(x = 270, y = 80)
        play_button = Button(400, 350, 100, 50, WHITE, BLACK, 'PLAY', 32)
        leaderboard_button = Button(300, 490, 300, 50, WHITE, BLACK, 'LEADERBOARD', 32)
        quit_button = Button(400, 420, 100, 50, WHITE, BLACK, 'QUIT', 32)

        intro_font = pygame.font.Font('font/retrofont.ttf', 18)
    
        # Text to display on intro screen
        instructions_text = intro_font.render(' Enter Your Username!! :)', True, WHITE)
        instructions_rect = instructions_text.get_rect(x=300, y=245)
        
        

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_SPACE:
                         if username:
                            self.username = username  # Save the entered username
                            intro = False
                    else:
                        username += event.unicode

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.new()
                self.draw_username()  # Draw the username on the screen

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(instructions_text, instructions_rect)
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.screen.blit(leaderboard_button.image, leaderboard_button.rect)
            self.clock.tick(FPS)

            input_box = pygame.Rect(320, 270, 250, 50)
            pygame.draw.rect(self.screen, WHITE, input_box, 4)
            font = pygame.font.Font(None, 32)
            text_surface = font.render(username, True, WHITE)
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            pygame.display.flip()

            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                entry = {'username': self.username, 'score': self.score}
                self.leaderboard.append(entry)
                self.save_leaderboard() 
                sys.exit()
            
            if leaderboard_button.is_pressed(mouse_pos, mouse_pressed):
                self.display_scoreboard()

        self.username = username  # Save the entered username for future use
        pygame.display.update()


    
class Sprite_Sheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def Get_Sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.newscreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.Terrain_spritesheet = Sprite_Sheet('img/terrain.png')

        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1 

        self.image = self.game.Character_spritesheet.Get_Sprite(3, 2, self.width, self.height)

        self.font = pygame.font.Font(None, 24)
        
        self.Character_spritesheet = Sprite_Sheet('img/character1.png')
        self.Terrain_spritesheet = Sprite_Sheet('img/terrain.png')
        self.Enemy_spritesheet = Sprite_Sheet('img/demon.png')
        self.Door_spritesheet = Sprite_Sheet('img/terrain.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.Character_spritesheet.Get_Sprite(3, 2, self.width, self.height),
                           self.game.Character_spritesheet.Get_Sprite(35, 2, self.width, self.height),
                           self.game.Character_spritesheet.Get_Sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.Character_spritesheet.Get_Sprite(3, 34, self.width, self.height),
                         self.game.Character_spritesheet.Get_Sprite(35, 34, self.width, self.height),
                         self.game.Character_spritesheet.Get_Sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.Character_spritesheet.Get_Sprite(3, 98, self.width, self.height),
                           self.game.Character_spritesheet.Get_Sprite(35, 98, self.width, self.height),
                           self.game.Character_spritesheet.Get_Sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.Character_spritesheet.Get_Sprite(3, 66, self.width, self.height),
                            self.game.Character_spritesheet.Get_Sprite(35, 66, self.width, self.height),
                            self.game.Character_spritesheet.Get_Sprite(68, 66, self.width, self.height)]
        
    def update(self):
        self.movement()
        self.Animate()
        self.Collide_Enemy()
        self.Collide_Door()

        self.rect.x += self.x_change
        self.Collide_Blocks('x')
        self.rect.y += self.y_change
        self.Collide_Blocks('y')

        self.x_change = 0
        self.y_change = 0
        self.game.draw_level_text()

        if self.game.health <= 0:
            self.game.playing = False  # Set playing to False to exit the game loop
            self.game.game_over()

        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def Collide_Enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.game.screen.fill(BLACK)
            pygame.display.update()
            self.display_question()
    
            

    def Collide_Blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED

        if direction == "y":
             hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
             if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def Collide_Door(self):
        hits = pygame.sprite.spritecollide(self, self.game.door, False)
        if hits:
            self.game.next_level()  # Load the next level
            self.game.draw_level_text()

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attack = pygame.sprite.LayeredUpdates()
        self.door = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()


    def display_question(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            enemy = hits[0]
            if not enemy.question_asked:
                selected_question = random.choice(questions)
                enemy.question_asked = True
                wrapped_question = textwrap.fill(selected_question['question'], width=40)  # Adjust width as needed

                question_lines = wrapped_question.split('\n')
                max_lines = 5  # Set the maximum number of lines to display

                if len(question_lines) > max_lines:
                    question_lines = question_lines[:max_lines]
                    question_lines.append("...")  # Indicate that the text is truncated

                for i, line in enumerate(question_lines):
                    text_line = self.game.font.render(line, True, WHITE)
                    self.game.screen.blit(text_line, (50, 50 + i * 30))

                choices_text = [self.game.font.render(f"{index + 1}. {choice}", True, WHITE) for index, choice in enumerate(selected_question['choices'])]
                for i, choice_text in enumerate(choices_text):
                    self.game.screen.blit(choice_text, (50, 200 + i * 50))
                pygame.display.update()

                answered = False
                while not answered:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.game.running = False
                            answered = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                player_answer = 1
                                answered = True
                            elif event.key == pygame.K_2:
                                player_answer = 2
                                answered = True
                            elif event.key == pygame.K_3:
                                player_answer = 3
                                answered = True

                    if answered:
                        if selected_question['choices'][player_answer - 1] == selected_question['correct_answer']:
                            self.game.score += 10  # Increase the score by 10 for each correct answer
                            result_text = self.game.font.render("Correct!", True, GREEN)
                            self.game.screen.blit(result_text, (50, 350))
                        else:
                            result_text = self.game.font.render("Wrong!", True, RED)
                            self.game.screen.blit(result_text, (50, 350))
                            self.game.health -= 25

                            if self.game.health < 0:
                                self.game.health = 0
                            
                        pygame.display.update()
                        pygame.time.delay(1000)
                        self.game.screen.fill(BLACK)
                        pygame.display.update()
                        answered = True


        if hits:
            enemy = hits[0]

            num_questions = self.game.current_level  # Number of questions based on the current level

            for _ in range(num_questions):
                selected_question = random.choice(questions)
                enemy.question_asked = True
                wrapped_question = textwrap.fill(selected_question['question'], width=40)  # Adjust width as needed

                question_lines = wrapped_question.split('\n')
                max_lines = 5  # Set the maximum number of lines to display

                if len(question_lines) > max_lines:
                    question_lines = question_lines[:max_lines]
                    question_lines.append("...")  # Indicate that the text is truncated

                for i, line in enumerate(question_lines):
                    text_line = self.game.font.render(line, True, WHITE)
                    self.game.screen.blit(text_line, (50, 50 + i * 30))

                choices_text = [self.game.font.render(f"{index + 1}. {choice}", True, WHITE) for index, choice in enumerate(selected_question['choices'])]
                for i, choice_text in enumerate(choices_text):
                    self.game.screen.blit(choice_text, (50, 150 + i * 50))

                pygame.display.update()

                answered = False
                while not answered:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.game.running = False
                            answered = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                player_answer = 1
                                answered = True
                            elif event.key == pygame.K_2:
                                player_answer = 2
                                answered = True
                            elif event.key == pygame.K_3:
                                player_answer = 3
                                answered = True

                if answered:
                    if selected_question['choices'][player_answer - 1] == selected_question['correct_answer']:
                        self.game.score += 10
                        result_text = self.game.font.render("Correct!", True, GREEN)
                        self.game.screen.blit(result_text, (50, 350))
                    else:
                        result_text = self.game.font.render("Wrong!", True, RED)
                        self.game.screen.blit(result_text, (50, 350))
                        self.game.health -= 25

                    pygame.display.update()
                    pygame.time.delay(1000)
                    self.game.screen.fill(BLACK)
                    pygame.display.update()
                    answered = True
            self.game.draw_score_text()
            
    def Animate(self):  
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.Character_spritesheet.Get_Sprite(3, 2, self.width, self.height)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.Character_spritesheet.Get_Sprite(3, 34, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.Character_spritesheet.Get_Sprite(3, 98, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.Character_spritesheet.Get_Sprite(3, 66, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
g = Game()

g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()

