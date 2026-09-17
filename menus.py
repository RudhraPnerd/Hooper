import assets as ast

def draw_game_over(screen, font):
    screen.fill((69, 71, 70))

    game_over_text = font.render('GAME OVER', True, (227, 48, 48))
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, 100))

    screen.blit(game_over_text, text_rect)
    screen.blit(ast.replay, ast.replay_img_rect)