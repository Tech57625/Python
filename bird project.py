import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.25
FLAP_STRENGTH = -7
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY_BLUE = (135, 206, 235)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.width = 30
        self.height = 30
    
    def flap(self):
        self.velocity = FLAP_STRENGTH
    
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Keep bird on screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.velocity = 0
    
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height), 0, 5)
        # Draw eye
        pygame.draw.circle(screen, BLACK, (self.x + 22, self.y + 10), 4)
        # Draw beak
        pygame.draw.polygon(screen, (255, 165, 0), [(self.x + 30, self.y + 15), 
                                                  (self.x + 40, self.y + 15), 
                                                  (self.x + 30, self.y + 20)])
    
    def get_mask(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + PIPE_GAP, 50, HEIGHT - self.height - PIPE_GAP)
        self.passed = False
    
    def update(self):
        self.x -= PIPE_SPEED
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x
    
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_pipe)
        pygame.draw.rect(screen, GREEN, self.bottom_pipe)
        
        # Draw pipe caps
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, self.height - 20, 60, 20))
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, self.height + PIPE_GAP, 60, 20))
    
    def collide(self, bird):
        bird_mask = bird.get_mask()
        return bird_mask.colliderect(self.top_pipe) or bird_mask.colliderect(self.bottom_pipe)

# Game function
def game():
    bird = Bird()
    pipes = []
    score = 0
    last_pipe = pygame.time.get_ticks()
    game_active = True
    
    font = pygame.font.SysFont('comicsans', 30)
    
    while True:
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird.flap()
                if event.key == pygame.K_r and not game_active:
                    # Restart game
                    return game()
        
        # Background
        screen.fill(SKY_BLUE)
        
        if game_active:
            # Update bird
            bird.update()
            
            # Generate pipes
            if current_time - last_pipe > PIPE_FREQUENCY:
                pipes.append(Pipe())
                last_pipe = current_time
            
            # Update and draw pipes
            for pipe in pipes[:]:
                pipe.update()
                pipe.draw()
                
                # Check for collision
                if pipe.collide(bird):
                    game_active = False
                
                # Check if pipe passed bird
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    score += 1
                
                # Remove off-screen pipes
                if pipe.x < -50:
                    pipes.remove(pipe)
            
            # Draw bird
            bird.draw()
            
            # Draw score
            score_text = font.render(f'Score: {score}', True, BLACK)
            screen.blit(score_text, (10, 10))
        
        else:
            # Game over screen
            game_over_text = font.render('Game Over! Press R to restart', True, BLACK)
            screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2 - 15))
            final_score = font.render(f'Final Score: {score}', True, BLACK)
            screen.blit(final_score, (WIDTH//2 - 80, HEIGHT//2 + 20))
        
        pygame.display.update()
        clock.tick(60)

# Start the game
if __name__ == "__main__":
    game()