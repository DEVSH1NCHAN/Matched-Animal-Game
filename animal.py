import random
import os
import game_config as gc

from pygame import transform, image

animal_count = dict((a,0) for a in gc.assests_files)

def avilable_animals():
    return [a for a,c in animal_count.items() if c<2]

class animal:
    def __init__(self, index):
        self.index=index
        self.row=self.index//gc.tile_in_line
        self.col=self.index%gc.tile_in_line
        self.name=random.choice(avilable_animals())
        animal_count[self.name]+=1

        self.image_path=os.path.join(gc.assets_dir, self.name)
        self.image=image.load(self.image_path)
        self.image=transform.scale(self.image, (gc.image_size-2*gc.margin,gc.image_size-2*gc.margin))
        self.box=self.image.copy()
        self.box.fill((200,200,200))
        self.skip=False