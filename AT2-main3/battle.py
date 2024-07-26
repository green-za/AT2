import random
import pygame
from assets import GAME_ASSETS
from healthbar import healthbar

import random
import pygame
from assets import GAME_ASSETS
from healthbar import healthbar

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

class Battle:
   def __init__(self, window, player, enemy):

       self.window = window
       self.player = player
       self.enemy = enemy
       self.width = int(self.window.get_width())
       self.height = int(self.window.get_height())
       self.map_image = pygame.image.load("Turnbased image.jpg").convert_alpha()
       self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), 700))
       self.player_images = {
           'Warrior': pygame.image.load(GAME_ASSETS['warrior']).convert_alpha(),
           'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
           'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
       }



       self.player_death = False
       self.has_chosen_attack = False
       self.player_turn = True
       self.enemy_turn = False
       pygame.font.init()
       self.font = pygame.font.Font(None, 40)
       self.attacks_font = pygame.font.Font(None, 25)
       
   
 
 
 
   def load_player(self, character_type):
       self.player_type = character_type
       self.player_image = self.player_images[character_type]
       self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 1.5), int(self.player_image.get_height() * 1.5)))

   def load_bars(self):
       self.heath_bar_player = healthbar((self.player_image.get_width()), (self.player.getMax_Hit_points()), (self.player.getHit_points()), 200, (int(self.player_image.get_height()) + 350), self.window, (255,0,0), (0,255,0))
       self.heath_bar_enemy = healthbar((self.enemy.combat_image.get_width()), (self.enemy.getMaxHP()), (self.enemy.getHP()), 1000, (int(self.enemy.combat_image.get_height()) +300), self.window, (255,0,0), (0,255,0))
       self.stamina_bar = healthbar((self.player_image.get_width()), (self.player.getMaxStamina()), (self.player.getStamina()), 200, (int(self.player_image.get_height()) + 375), self.window, (BLACK), (0,0,255))
   
   def handle_combat(self):
       enemy_damage = random.randint(15, 40)
       player_defeated = self.player.take_damage(enemy_damage)
       if player_defeated:
           print("you died :(")
           return 'PLAYER DIED'
       return str(f"{self.enemy.name} attacks back! Deals {enemy_damage} damage to the player.")
   

   def pause(self):
       text = self.attacks_font.render("(press enter to continue)", False, (BLACK))
       textLength = int(text.get_width())
       textHeight = int(text.get_height())
       
       self.window.blit(text, [(self.window.get_width() - (textLength + 10)), (self.window.get_height() - (textHeight + 10))])
       pygame.display.flip()
       hit_key = None
       while not hit_key:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:    
                   break
               elif event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       text = self.attacks_font.render("(press enter to continue)", False, (WHITE))
                       self.window.blit(text, [(self.window.get_width() - (textLength + 10)), (self.window.get_height() - (textHeight + 10))])
                       pygame.display.flip()
                       hit_key = 1
                       
       return hit_key
   
   def pause_for_atributes(self):
       line1 = "Select a stat to level up"
       line2 = f"1. increase your health, lvl({self.player.getMax_Hit_points()})"
       line3 = f"2. increase your armour, lvl({self.player.getArmour()})"
       line4 = f"3. increase your strength, lvl({self.player.getStrength()})"

       line1_text = self.attacks_font.render(line1, False, (BLACK))
       line2_text = self.attacks_font.render(line2, False, (BLACK))
       line3_text = self.attacks_font.render(line3, False, (BLACK))
       line4_text = self.attacks_font.render(line4, False, (BLACK))

       self.window.blit(line1_text, (100, 750))
       self.window.blit(line2_text, (100, 775))
       self.window.blit(line3_text, (100, 800))
       self.window.blit(line4_text, (100, 825))

       pygame.display.flip()

       line1_text = self.attacks_font.render(line1, False, (WHITE))
       line2_text = self.attacks_font.render(line2, False, (WHITE))
       line3_text = self.attacks_font.render(line3, False, (WHITE))
       line4_text = self.attacks_font.render(line4, False, (WHITE))

       self.window.blit(line1_text, (100, 750))
       self.window.blit(line2_text, (100, 775))
       self.window.blit(line3_text, (100, 800))
       self.window.blit(line4_text, (100, 825))

       hit_key = None
       while not hit_key:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:    
                   break
               elif event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_1:
                       hit_key = "1"

                   elif event.key == pygame.K_2:
                       hit_key = "2"

                   elif event.key == pygame.K_3:
                       hit_key = "3"
       return hit_key
   
   def playerTurn(self):
       chosen_attack = None
       attacks = self.player.getAttacks()
       line1 = "choose your attack!"
       line2 = attacks[0]
       line3 = attacks[1]
       line4 = attacks[2]
       line5 = attacks[3]
       line6 = attacks[4]
       
       line1_text = self.attacks_font.render(line1, False, (BLACK))
       line2_text = self.attacks_font.render(line2, False, (BLACK))
       line3_text = self.attacks_font.render(line3, False, (BLACK))
       line4_text = self.attacks_font.render(line4, False, (BLACK))
       line5_text = self.attacks_font.render(line5, False, (BLACK))
       line6_text = self.attacks_font.render(line6, False, ())

       self.window.blit(line1_text, (100, 750))
       self.window.blit(line2_text, (100, 775))
       self.window.blit(line3_text, (100, 800))
       self.window.blit(line4_text, (100, 825))
       self.window.blit(line5_text, (100, 850))
       self.window.blit(line6_text, (100, 875))

       pygame.display.flip()

       line1_text = self.attacks_font.render(line1, False, (WHITE))
       line2_text = self.attacks_font.render(line2, False, (WHITE))
       line3_text = self.attacks_font.render(line3, False, (WHITE))
       line4_text = self.attacks_font.render(line4, False, (WHITE))
       line5_text = self.attacks_font.render(line5, False, (WHITE))
       line6_text = self.attacks_font.render(line6, False, (WHITE))

       self.window.blit(line1_text, (100, 750))
       self.window.blit(line2_text, (100, 775))
       self.window.blit(line3_text, (100, 800))
       self.window.blit(line4_text, (100, 825))
       self.window.blit(line5_text, (100, 850))
       self.window.blit(line6_text, (100, 875))

       
       
       
       
       
       
       
       
       
       
       while not chosen_attack:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:    
                   break
               elif event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_1:
                       chosen_attack = 1
                   elif event.key == pygame.K_2:
                       chosen_attack = 2
                   elif event.key == pygame.K_3:
                       chosen_attack = 3
                   elif event.key == pygame.K_4:
                       chosen_attack = 4
                   elif event.key == pygame.K_5:
                       chosen_attack = 5

       return chosen_attack
           


               

   def Turnbased(self):
       if self.player_turn == True:
              attack_choozer = self.playerTurn()
              player_deal_damage = self.player.choose_attack(self.enemy, attack_choozer)
              if player_deal_damage == "Invalid attack":
                   player_message = self.font.render("only input any of the displayed numbers", False, (BLACK))
                   self.window.blit(player_message, (100, 750))
                   pygame.display.flip()
                   self.pause()
                   pass
                  
              elif player_deal_damage == "no stam":
                   player_message = self.font.render("you dont have enough stamina for that", False, (BLACK))
                   self.window.blit(player_message, (100, 750))
                   pygame.display.flip()
                   self.pause()
                   pass

              elif player_deal_damage == "attack complete":
                     self.stamina_bar.update()
                     attack_message = self.player.get_current_attack_message()
                     player_message = self.font.render(attack_message, False, (BLACK))
                     self.window.blit(player_message, (100, 750))
                     self.heath_bar_enemy.update()
                     pygame.display.flip()        
                     self.pause()
                     player_message = self.font.render(attack_message, False, (WHITE))
                     self.window.blit(player_message, (100, 750))
                     pygame.display.flip()
                     enemy_alive = self.enemy.is_alive()
                     if enemy_alive == "dead":
                       self.draw_enemy_dead()
                       xp_gain = self.player.gain_experience(1000)
                       player_xp_gain = self.font.render(xp_gain, False, (BLACK))
                       player_message = self.font.render("enemy killed", False, (BLACK))
                       self.window.blit(player_xp_gain, (100, 790))
                       self.window.blit(player_message, (100, 750))
                       pygame.display.flip()
                       self.pause()
                       player_xp_gain = self.font.render(xp_gain, False, (WHITE))
                       player_message = self.font.render("enemy killed", False, (WHITE))
                       self.window.blit(player_xp_gain, (100, 790))
                       self.window.blit(player_message, (100, 750))
                       pygame.display.flip()
                       if self.player.get_Attribute_points() > 0:
                           Attribute_chooser = self.pause_for_atributes()
                           if Attribute_chooser == "1":
                               old_atribute = self.player.getMax_Hit_points()
                               new_atribute = self.player.set_Max_Hit_pointsplus1()
                               message = self.font.render(f"your health Has been Upgraded from level {old_atribute} to level {new_atribute}", False, (BLACK))
                               self.window.blit(message, (100, 750))
                               pygame.display.flip()
                               self.pause()
                           elif Attribute_chooser == "2":
                               old_atribute = self.player.getArmour()
                               new_atribute = self.player.set_Armourplus1()
                               message = self.font.render(f"your armor Has been Upgraded from level {old_atribute} to level {new_atribute}", False, (BLACK))
                               self.window.blit(message, (100, 750))
                               pygame.display.flip()
                               self.pause()
                           
                           elif Attribute_chooser == "3":
                               old_atribute = self.player.getStrength()
                               new_atribute = self.player.set_Strengthplus1()
                               message = self.font.render(f"your strength Has been Upgraded from level {old_atribute} to level {new_atribute}", False, (BLACK))
                               self.window.blit(message, (100, 750))
                               pygame.display.flip()
                               self.pause()

                           
                       self.player.healthRegenerate()
                       return "Enemy Death"
                     self.player_turn = False
                     self.enemy_turn = True
                  
                      
               
       
    
    
       if self.enemy_turn == True:
           turn_result = self.handle_combat()
           self.heath_bar_player.update()
           self.player.regenerate_stamina()
           if turn_result == "you died":
               return "player death"
           
           else:
               enemy_message = self.font.render(turn_result, False, ())
               self.window.blit(enemy_message, (100, 750))
               pygame.display.flip()
               self.pause()
               self.enemy_turn = False
               self.player_turn = True



   def draw_enemy_dead(self):
       self.window.fill((WHITE)) 
       self.window.blit(self.map_image, (0, 0))
       self.window.blit(self.player_image, (200, 350))
       pygame.draw.rect(self.window, (0,0,0), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700))
       pygame.draw.rect(self.window, (255,255,255), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700), 4)
       self.stamina_bar.draw()
       self.heath_bar_player.draw()
       pygame.display.flip()
       
             

  
   def draw(self):
       self.window.fill((WHITE)) 
       self.window.blit(self.map_image, (0, 0))
       self.window.blit(self.player_image, (200, 350))
       self.enemy.COMBATDRAW(1000, 300)
       pygame.draw.rect(self.window, (0,0,0), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700))
       pygame.draw.rect(self.window, (255,255,255), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700), 4)
       self.stamina_bar.draw()
       self.heath_bar_enemy.draw()
       self.heath_bar_player.draw()
       pygame.display.flip()

   
   
   def getPlayer(self):
       return self.player
   