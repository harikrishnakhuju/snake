from settings import *
from os import walk

class Snake:
    def __init__(self):
        # Setup
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_ROW - col,START_COL) for col in range(START_LENGHT)]
        self.direction = pygame.Vector2(1,0)

        self.has_eaten = False
    
        # Graphics
        self.surfs = self.import_surfs()
        self.draw_data = []
        self.head_surf = self.surfs['head_right']
        self.tail_surf = self.surfs['tail_left']
    

    def import_surfs(self):
        surf_dict = {}
        for folder_path, _, image_names in walk(r'assets\graphics\snake'):
            for image_name in image_names:
                full_path = join(folder_path, image_name)
                surface = pygame.image.load(full_path).convert_alpha()
                surf_dict[image_name.split('.')[0]] = surface
        return surf_dict
    


    def update(self):
        if not self.has_eaten:
            body_copy = self.body [:-1]
            # 1. get the head and move the head by the direction
            new_head = body_copy[0] + self.direction
            # 2. insert the new head at index 0
            body_copy.insert(0,new_head)
            self.body = body_copy[:]
        else:
            body_copy = self.body [:]
            new_head = body_copy[0] + self.direction
            body_copy.insert(0,new_head)
            self.body = body_copy[:]
            self.has_eaten = False

        self.update_head()
        self.update_tail()
        self.update_body()


    def reset(self):
        self.body = [pygame.Vector2(START_ROW - col,START_COL) for col in range(START_LENGHT)]
        self.direction = pygame.Vector2(1,0)
        self.update_head()
        self.update_tail()
        self.update_body()

    def update_head(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.Vector2(-1,0): self.head_surf = self.surfs['head_right']
        elif head_relation == pygame.Vector2(1,0): self.head_surf = self.surfs['head_left']
        elif head_relation == pygame.Vector2(0,-1): self.head_surf = self.surfs['head_down']
        elif head_relation == pygame.Vector2(0,1): self.head_surf = self.surfs['head_up']
    
    def update_body(self):
        self.draw_data=[]
        for index, part in enumerate(self.body):
            # position
            x = part.x * CELL_SIZE
            y = part.y * CELL_SIZE
            rect = pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)

            if index == 0:
                self.draw_data.append((self.head_surf, rect))
            elif index == len(self.body) -1:
                self.draw_data.append((self.tail_surf, rect))
            else:
                last_part = self.body[index + 1] - part
                next_part = self.body[index - 1] - part
                if last_part.x == next_part.x:
                    self.draw_data.append((self.surfs['body_horizontal'], rect))
                elif last_part.y == next_part.y:
                    self.draw_data.append((self.surfs['body_vertical'], rect))
                else:
                    if last_part.x == -1 and next_part.y == -1 or last_part.y == -1 and next_part.x == -1:
                        self.draw_data.append((self.surfs['body_tl'],rect))
                    elif last_part.x == -1 and next_part.y == 1 or last_part.y == 1 and next_part.x == -1:
                        self.draw_data.append((self.surfs['body_bl'],rect))
                    elif last_part.x == 1 and next_part.y == 1 or last_part.y == 1 and next_part.x == 1:
                        self.draw_data.append((self.surfs['body_br'],rect))
                    elif last_part.x == 1 and next_part.y == -1 or last_part.y == -1 and next_part.x == 1:
                        self.draw_data.append((self.surfs['body_tr'],rect))
                    

    def update_tail(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.Vector2(-1,0): self.tail_surf = self.surfs['tail_right']
        elif tail_relation == pygame.Vector2(1,0): self.tail_surf = self.surfs['tail_left']
        elif tail_relation == pygame.Vector2(0,-1): self.tail_surf = self.surfs['tail_down']
        elif tail_relation == pygame.Vector2(0,1): self.tail_surf = self.surfs['tail_up']

    def draw(self):
        for surf, rect in self.draw_data:
            self.display_surface.blit(surf,rect)