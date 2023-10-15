import pygame
from sprites import *
from config import *
import sys
class Game :
    def __init__(self) :
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Arial', 32)
        self.running = True
        
        self.character_spritesheet= Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet= Spritesheet('img/enemy.png')
        self.attack_spritesheet= Spritesheet('img/attack.png')
    def createTilemap(self) :
        for i, row in enumerate(tilemap) :
             for j, column in enumerate(row) :
                 Ground(self, j, i)
                 if column == 'B' :
                     Block(self,j,i)
                 if column== 'E' :
                     Enemy(self, j,i)
                 if column ==  'P' :
                     #Player(self, j, i)
                     self.player= Player(self, j,i)
    
    def new(self) :
        
        # a new game starts
        self.playing= True  
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks= pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()
        
        
    def events(self ) :
        # game loop event
        for event in pygame.event.get() :
            if event.type== pygame.QUIT :
                self.playing = False
                self.running= False
        
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    if self.player.facing == 'up' :
                        Attack(self, self.player.rect.x, self.player.rect.y- TILESIZE)
                    if self.player.facing == 'down' :
                        Attack(self, self.player.rect.x, self.player.rect.y+ TILESIZE)
                    if self.player.facing == 'left' :
                        Attack(self, self.player.rect.x- TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right' :
                        Attack(self, self.player.rect.x+ TILESIZE, self.player.rect.y)         
        
    def update(self) :
        # game loop update 
        self.all_sprites.update()
        
        
    def draw(self) :
        # GAME LOOP DRAW
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        
    def main(self) :
        # game loop
        while self.playing :
            self.events()
            self.update()
            self.draw()
        self.running = False
        
    def game_over(self) :
        pass
        
    def intro_screen (self) :
        pass
g= Game()
g.intro_screen()
g.new()
while g.running :
    g.main()
    g.game_over()
pygame.quit()
sys.exit()  
    