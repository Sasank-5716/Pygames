import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]

# Game variables
card_width, card_height = 100, 100
margin = 20
rows, cols = 4, 4
cards = []
revealed = []
selected = []
matched = []
font = pygame.font.Font(None, 36)
score = 0

# Create cards
for color in COLORS * 2:  # Each color appears twice
    cards.append(color)
random.shuffle(cards)

# Initialize revealed and matched lists
revealed = [False] * len(cards)
matched = [False] * len(cards)


#Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
            # Check which card was clicked
            for i in range(len(cards)):
                row = i // cols
                col = i % cols
                card_x = col * (card_width + margin) + margin
                card_y = row * (card_height + margin) + margin
        
                if (card_x <= mouse_x <= card_x + card_width and 
                    card_y <= mouse_y <= card_y + card_height and 
                    not revealed[i] and len(selected) < 2 and not matched[i]):
                    revealed[i] = True
                    selected.append(i)
            
                    # Check for match
                    if len(selected) == 2:
                        if cards[selected[0]] == cards[selected[1]]:
                            matched[selected[0]] = True
                            matched[selected[1]] = True
                            score += 10
                        else:
                            # Wait a bit before hiding
                            pygame.time.delay(500)
                            for idx in selected:
                                revealed[idx] = False
                        selected = []

    # Check win condition
    if all(matched):
        win_text = font.render("You Win! Final Score: " + str(score), True, BLACK)
        screen.blit(win_text, (WIDTH//2 - 150, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(2000)
        # Reset game
        random.shuffle(cards)
        revealed = [False] * len(cards)
        matched = [False] * len(cards)
        selected = []
        score = 0
    
    # Drawing
    screen.fill(WHITE)
    
    # Draw cards
    for i in range(len(cards)):
        row = i // cols
        col = i % cols
        card_x = col * (card_width + margin) + margin
        card_y = row * (card_height + margin) + margin
    
        if revealed[i] or matched[i]:
            pygame.draw.rect(screen, cards[i], (card_x, card_y, card_width, card_height))
        else:
            pygame.draw.rect(screen, GRAY, (card_x, card_y, card_width, card_height))
    
        pygame.draw.rect(screen, BLACK, (card_x, card_y, card_width, card_height), 2)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)