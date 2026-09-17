import assets as ast

def draw_game_over(screen, font):
    screen.fill((69, 71, 70))

    game_over_text = font.render('GAME OVER', True, (227, 48, 48))
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(game_over_text, text_rect)
    screen.blit(ast.replay, ast.replay_img_rect)
    screen.blit(ast.home, ast.home_img_rect)

def draw_home(screen, font):
    screen.fill((252, 186, 3))

    title = font.render('Hooper', True, (0, 0, 0))
    title_rect = title.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(title, title_rect)
    screen.blit(ast.play, ast.play_img_rect)