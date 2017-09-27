#coding:utf-8
import pygame

pygame.mixer.init()
track = pygame.mixer.music.load("yinfu.wav")
pygame.mixer.music.play()
tmp = raw_input("Playing...Press any key to exit.")

