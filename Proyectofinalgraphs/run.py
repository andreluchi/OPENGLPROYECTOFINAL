import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 1920
height = 1280

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

#carga de objeto y textura
face = Model('pikapika.obj', 'pikapika.bmp')
face.position.z = -1.5
face.position.y = -0.3

rend.scene.append( face )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Movimiento camara

    #izquierda derecha atras adelante
    if keys[K_a]:
        rend.camPosition.x += 1 * deltaTime
        rend.pointLight.x += 10* deltaTime
    if keys[K_d]:
        rend.camPosition.x -= 1 * deltaTime
        rend.pointLight.x -= 10* deltaTime
    if keys[K_w]:
        rend.camPosition.z += 1 * deltaTime
        rend.pointLight.z += 3* deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 1 * deltaTime
        rend.pointLight.z -= 3* deltaTime

    #arriba abajo camara
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
        rend.pointLight.y -= 3 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime
        rend.pointLight.y += 3 * deltaTime

    # Rotacion de camara

    #axis y
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime

        
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime

    # axis x
    if keys[K_c]:
        rend.camRotation.x += 30 * deltaTime
        
    if keys[K_b]:
        rend.camRotation.x -= 30 * deltaTime  
    # axis z
    if keys[K_v]:
        rend.camRotation.z += 30 * deltaTime
        
    if keys[K_n]:
        rend.camRotation.z -= 30 * deltaTime

    if keys[K_r]:
            rend.camPosition.x = 0 * deltaTime
            rend.pointLight.x = 0* deltaTime
            rend.camPosition.y = 0 * deltaTime
            rend.pointLight.y = 0* deltaTime
            rend.camPosition.z = 0 * deltaTime
            rend.pointLight.z = 0* deltaTime
            rend.camRotation.x = 0 * deltaTime
            rend.camRotation.y = 0 * deltaTime
            rend.camRotation.z = 0 * deltaTime

    if keys[K_p]:
            rend.camPosition.x = 0 * deltaTime
            rend.pointLight.x = 0* deltaTime
            rend.camPosition.y = 0 * deltaTime
            rend.pointLight.y = 0* deltaTime
            rend.camPosition.z = 0 * deltaTime
            rend.pointLight.z = 0* deltaTime
            rend.camRotation.x = 0 * deltaTime
            rend.camRotation.y = 0 * deltaTime
            rend.camRotation.z = 0 * deltaTime
            rend.setShaders(shaders.vertex_shader, shaders.start_shader)

    # cambio de shaders
    if keys[K_6]:
            rend.setShaders(shaders.vertex_shader, shaders.Blackwhite_shader)
    if keys[K_5]:
            rend.setShaders(shaders.vertex_shader, shaders.termico_shader)
    if keys[K_4]:
        rend.setShaders(shaders.vertex_shader, shaders.radioactivo_shader)
    if keys[K_3]:
        rend.setShaders(shaders.vertex_shader, shaders.ocean_shader)
    if keys[K_2]:
            rend.setShaders(shaders.vertex_shader, shaders.whiteout_shader)
    if keys[K_1]:
            rend.setShaders(shaders.vertex_shader, shaders.start_shader)


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()