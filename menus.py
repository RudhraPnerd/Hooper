import assets as ast

def draw_game_over(screen, font):
    screen.fill(69, 71, 70)

    game_over_text = font.render('GAME OVER', True, (227, 48, 48))

    screen.blit(game_over_text, (20, 60))
    screen.blit(ast.check_circle, ast.check_circle_img_rect)