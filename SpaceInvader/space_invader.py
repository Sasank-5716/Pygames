import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width, player_height = 50, 30
player = pygame.Rect(WIDTH//2 - player_width//2, HEIGHT - player_height - 20, player_width, player_height)
player_speed = 5

# Bullets
bullets = []
bullet_width, bullet_height = 5, 15
bullet_speed = 7

# Enemies
enemies = []
enemy_width, enemy_height = 40, 30
enemy_rows = 5
enemy_cols = 10
enemy_speed = 1
enemy_direction = 1
enemy_move_down = False

for row in range(enemy_rows):
    for col in range(enemy_cols):
        enemy = pygame.Rect(
            100 + col * (enemy_width + 20),
            50 + row * (enemy_height + 20),
            enemy_width,
            enemy_height
        )
        enemies.append(enemy)


# Enemy bullets
enemy_bullets = []
enemy_bullet_speed = 3
enemy_shoot_chance = 0.005

# Game variables
score = 0
lives = 3
font = pygame.font.Font(None, 36)
logo_font = pygame.font.Font(None, 24)

game_over = False

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = pygame.Rect(
                    player.x + player_width//2 - bullet_width//2,
                    player.y,
                    bullet_width,
                    bullet_height
                )
                bullets.append(bullet)
            if event.key == pygame.K_r and game_over:
                # Reset game
                enemies = []
                for row in range(enemy_rows):
                    for col in range(enemy_cols):
                        enemy = pygame.Rect(
                            100 + col * (enemy_width + 20),
                            50 + row * (enemy_height + 20),
                            enemy_width,
                            enemy_height
                        )
                        enemies.append(enemy)
                bullets = []
                enemy_bullets = []
                score = 0
                lives = 3
                game_over = False

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed
        
        # Bullet movement
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
        
        # Enemy movement
        move_down = False
        for enemy in enemies:
            if enemy.right + enemy_speed * enemy_direction > WIDTH or enemy.left + enemy_speed * enemy_direction < 0:
                move_down = True
                break
        
        if move_down:
            enemy_direction *= -1
            for enemy in enemies:
                enemy.y += 20
        else:
            for enemy in enemies:
                enemy.x += enemy_speed * enemy_direction
        
        # Enemy shooting
        for enemy in enemies:
            if random.random() < enemy_shoot_chance:
                enemy_bullet = pygame.Rect(
                    enemy.x + enemy_width//2 - bullet_width//2,
                    enemy.y + enemy_height,
                    bullet_width,
                    bullet_height
                )
                enemy_bullets.append(enemy_bullet)
        
        # Enemy bullet movement
        for bullet in enemy_bullets[:]:
            bullet.y += enemy_bullet_speed
            if bullet.top > HEIGHT:
                enemy_bullets.remove(bullet)

        # Collision detection
        # Bullets hitting enemies
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    score += 10
                    break
        
        # Enemy bullets hitting player
        for bullet in enemy_bullets[:]:
            if bullet.colliderect(player):
                enemy_bullets.remove(bullet)
                lives -= 1
                if lives <= 0:
                    game_over = True
        
        # Enemies reaching bottom
        for enemy in enemies:
            if enemy.bottom >= HEIGHT:
                game_over = True
        
        # Player hitting enemies
        for enemy in enemies:
            if player.colliderect(enemy):
                game_over = True
        
        # Win condition
        if not enemies:
            # Level complete (for simplicity, just reset)
            enemies = []
            for row in range(enemy_rows):
                for col in range(enemy_cols):
                    enemy = pygame.Rect(
                        100 + col * (enemy_width + 20),
                        50 + row * (enemy_height + 20),
                        enemy_width,
                        enemy_height
                    )
                    enemies.append(enemy)

    # Drawing
    screen.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(screen, GREEN, player)
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    # Draw enemy bullets
    for bullet in enemy_bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    
    # Draw score and lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))

    logo_text = logo_font.render("Created By Sasank Lama", True, WHITE)
    screen.blit(logo_text, (10, HEIGHT - 40))
    
    # Game over message
    if game_over:
        game_over_text = font.render("GAME OVER - Press R to restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH//2 - 180, HEIGHT//2))
    
    pygame.display.flip()
    clock.tick(60)