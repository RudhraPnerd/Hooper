import assets as ast
import pygame

SHOP_ITEMS = [
    {"name": "Realistic Hoop", "cost": 50, "unlock": "realistic_hoop"},
    {"name": "Gold Hoop", "cost": 150, "unlock": "gold_hoop"},
]

def draw_game_over(screen, font):
    screen.fill((69, 71, 70))

    game_over_text = font.render('GAME OVER', True, (227, 48, 48))
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(game_over_text, text_rect)
    screen.blit(ast.replay, ast.replay_img_rect)
    screen.blit(ast.home, ast.home_img_rect)
    ast.power_img_rect = ast.power.get_rect(center=(screen.get_width() // 2, 300))
    screen.blit(ast.power, ast.power_img_rect)

def draw_home(screen, font):
    screen.fill((252, 186, 3))

    title = font.render('Hooper', True, (0, 0, 0))
    title_rect = title.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(title, title_rect)
    screen.blit(ast.play, ast.play_img_rect)
    screen.blit(ast.power, ast.power_img_rect)

def draw_shop(screen, font, title_font):
    screen.fill((252, 186, 3))

    shop_title = title_font.render('Shop', True, (0, 0, 0))
    shop_title_rect = shop_title.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(shop_title, shop_title_rect)
    screen.blit(ast.back, ast.back_img_rect)

    item_width = 150
    item_height = 120
    buy_height = 40
    gap = 30
    start_x = 50
    start_y = 200

    item_rects = []
    buy_rects = []

    for i, item in enumerate(SHOP_ITEMS):
        x = start_x + i * (item_width + gap)
        y = start_y

        item_rect = pygame.Rect(x, y, item_width, item_height)
        buy_rect = pygame.Rect(x, y + item_height + 10, item_width, buy_height)

        item_rects.append(item_rect)
        buy_rects.append(buy_rect)

        pygame.draw.rect(screen, (255, 0, 0), item_rect, border_radius=10)
        pygame.draw.rect(screen, (0, 200, 0), buy_rect, border_radius=10)

        name_text = font.render(item["name"], True, (0, 0, 0))
        name_rect = name_text.get_rect(center=(item_rect.centerx, item_rect.top + 30))
        screen.blit(name_text, name_rect)

        cost_text = font.render(f'{item["cost"]}', True, (0, 0, 0))
        cost_rect = cost_text.get_rect(center=(item_rect.centerx, item_rect.bottom - 20))
        screen.blit(cost_text, cost_rect)

        buy_text = font.render('Buy', True, (0, 0, 0))
        buy_text_rect = buy_text.get_rect(center=buy_rect.center)
        screen.blit(buy_text, buy_text_rect)

    return item_rects, buy_rects

def draw_broke(screen, font):
    screen.fill((252, 186, 3))

    message = font.render('Not enough money!', True, (0, 0, 0))
    message_rect = message.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(message, message_rect)
    screen.blit(ast.back, ast.back_img_rect)