import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        self.snake_pos = [200, 200]
        self.snake_body = [[200, 200], [220, 200], [240, 200]]
        self.food_pos = [random.randrange(20, WIDTH - 20) // 10 * 10, random.randrange(20, HEIGHT - 20) // 10 * 10]
        self.food_spawn = True
        self.snake_direction = 'RIGHT'
        self.score = 0

    def draw_everything(self):
        win.fill(BLACK)
        for pos in self.snake_body:
            pygame.draw.rect(win, WHITE, (pos[0], pos[1], 10, 10))
        pygame.draw.rect(win, RED, (self.food_pos[0], self.food_pos[1], 10, 10))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, WHITE)
        win.blit(text, (WIDTH - 150, 20))

    def update_snake_position(self):
        if self.snake_direction == 'RIGHT':
            new_head_pos = [self.snake_body[-1][0] + 10, self.snake_body[-1][1]]
        elif self.snake_direction == 'LEFT':
            new_head_pos = [self.snake_body[-1][0] - 10, self.snake_body[-1][1]]
        elif self.snake_direction == 'UP':
            new_head_pos = [self.snake_body[-1][0], self.snake_body[-1][1] - 10]
        elif self.snake_direction == 'DOWN':
            new_head_pos = [self.snake_body[-1][0], self.snake_body[-1][1] + 10]

        if (new_head_pos[0] < 0 or new_head_pos[0] > WIDTH - 10 or
                new_head_pos[1] < 0 or new_head_pos[1] > HEIGHT - 10):
            pygame.quit()
            sys.exit()

        self.snake_body.append(new_head_pos)
        if self.food_pos == new_head_pos:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop(0)

    def update_food_position(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(20, WIDTH - 20) // 10 * 10,
                             random.randrange(20, HEIGHT - 20) // 10 * 10]
            self.food_spawn = True

    def check_collision(self):
        for pos in self.snake_body[:-1]:
            if self.snake_body[-1] == pos:
                pygame.quit()
                sys.exit()

game = SnakeGame()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake_direction != 'DOWN':
                game.snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and game.snake_direction != 'UP':
                game.snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and game.snake_direction != 'RIGHT':
                game.snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and game.snake_direction != 'LEFT':
                game.snake_direction = 'RIGHT'

    game.update_snake_position()
    game.check_collision()
    game.draw_everything()
    game.draw_score()

    if not game.food_spawn:
        game.update_food_position()

    pygame.display.update()
    clock.tick(10)