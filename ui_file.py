elif event.type == pygame.KEYDOWN:
if event.key == pygame.K_q:
    if not jump and pygame.sprite.spritecollideany(mn, objects):
        jump = 15
        double_jump = True
    else:
        print(jump)
        print(under)
        if (jump or under) and double_jump:
            jump = 15
            double_jump = False
pygame.event.pump()
keyinput = pygame.key.get_pressed()
if keyinput[pygame.K_SPACE]:
    start = True
smth.update(screen, color)
if not jump and start and not pygame.sprite.spritecollideany(mn, objects):
    mn.down(2)
if jump:
    mn.jump(jump)
    jump -= 1
    if jump == 0:
        under = 44
if under:
    under -= 1
mn.update(screen, color)
clock.tick(20)
pygame.display.flip()
screen.fill((0, 0, 0))