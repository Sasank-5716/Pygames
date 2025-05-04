import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird
bird_radius = 20
bird = pygame.Rect(WIDTH//4, HEIGHT//2, bird_radius*2, bird_radius*2)
bird_speed = 0
gravity = 0.5
flap_strength = -8

# Pipes
pipes = []
pipe_width = 60
pipe_gap = 150
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks()
scroll_speed = 3

# Game variables
score = 0
high_score = 0
font = pygame.font.Font(None, 36)
game_active = False

# Game loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_speed = flap_strength
                else:
                    # Reset game
                    bird.y = HEIGHT//2
                    bird_speed = 0
                    pipes = []
                    score = 0
                    game_active = True
    
    # Game logic
    if game_active:
        # Bird movement
        bird_speed += gravity
        bird.y += bird_speed
        
        # Generate pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(100, HEIGHT - pipe_gap - 100)
            top_pipe = pygame.Rect(WIDTH, 0, pipe_width, pipe_height)
            bottom_pipe = pygame.Rect(WIDTH, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
            pipes.append((top_pipe, bottom_pipe))
            last_pipe = time_now
        
        # Move pipes
        for pipe_pair in pipes[:]:
            pipe_pair[0].x -= scroll_speed
            pipe_pair[1].x -= scroll_speed
            
            # Remove pipes that are off screen
            if pipe_pair[0].right < 0:
                pipes.remove(pipe_pair)
                score += 0.5  # 0.5 for each pipe (1 for each pair)
        
        # Collision detection
        # With ground and ceiling
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_active = False
        
        # With pipes
        for pipe_pair in pipes:
            if bird.colliderect(pipe_pair[0]) or bird.colliderect(pipe_pair[1]):
                game_active = False
        
        # Update high score
        if score > high_score:
            high_score = score
    def draw_logo(screen):
        logo_font = pygame.font.Font(None, 24)  
        logo_text = logo_font.render('Created By Sasank Lama', True, (50, 50, 50)) 
        logo_pos = (screen.get_width() - logo_text.get_width() - 10, screen.get_height() - logo_text.get_height() - 10)
        screen.blit(logo_text, logo_pos)

    # Drawing
    screen.fill(SKY_BLUE)

    # Draw pipes
    for pipe_pair in pipes:
        pygame.draw.rect(screen, GREEN, pipe_pair[0])
        pygame.draw.rect(screen, GREEN, pipe_pair[1])
    
    # Draw bird
    pygame.draw.ellipse(screen, RED, bird)
    pygame.draw.ellipse(screen, BLACK, bird, 2)
    
     # Draw score
    score_text = font.render(f"Score: {int(score)}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Draw high score
    high_score_text = font.render(f"High: {int(high_score)}", True, WHITE)
    screen.blit(high_score_text, (10, 50))
    
    # Game over message
    if not game_active and score > 0:
        game_over_text = font.render("Press SPACE to restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
    
    draw_logo(screen)

    pygame.display.flip()
    clock.tick(60)