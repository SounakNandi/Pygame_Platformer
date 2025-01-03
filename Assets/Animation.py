import pygame

class Animation:
    def __init__(self):
        self.current_time = pygame.time.get_ticks()
        self.time_difference = 0
        self.sprite_sheet = None
        self.frame_interval = 0
        self.frame_counter = 0
        self.total_frames = 0

        self.width = 0
        self.height = 0

    def __call__(self, sprite_sheet, frame_interval, total_frames, width, height, LOOP = True):
        self.sprite_sheet = sprite_sheet
        self.frame_interval = frame_interval
        self.total_frames = total_frames
        self.width = width
        self.height = height
        if LOOP:
            self.frame_counter = self.frame_counter if self.frame_counter < self.total_frames else 0
        else:
            self.frame_counter = self.frame_counter if self.frame_counter < self.total_frames - 1  else self.total_frames - 1
        return self.update(LOOP)

    def update(self, loop):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.time_difference >= self.frame_interval:
            if loop:
                self.frame_counter = (self.frame_counter + 1) % self.total_frames
            else:
                self.frame_counter = self.frame_counter + 1 if self.frame_counter < self.total_frames - 2  else self.total_frames - 1
            self.time_difference = self.current_time
        return self.sprite_sheet.subsurface(self.width * self.frame_counter, 0, self.width, self.height)
    
    def reset(self):
        self.frame_counter = 0



