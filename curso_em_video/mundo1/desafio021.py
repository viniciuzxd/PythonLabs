import pygame

pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
input('Tocando música, aperte ENTER para parar...')
pygame.mixer.music.stop()