import os
import pygame as pg
def globalise(foldr_path, method, condition=lambda file:True, *, not_image_ok=False):
    for file in os.listdir(foldr_path):
        file: str 
        if not condition(file): continue
        try: method(file)
        except Exception as e:
            if not not_image_ok: raise e


def main():
    pg.init()
    pg.display.set_mode((800, 500))
    pg.display.set_caption("Image editing")
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        pg.display.update()
        clock.tick(60)
