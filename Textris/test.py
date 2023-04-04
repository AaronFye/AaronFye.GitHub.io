# import pygame
import pygame

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

# create the display surface
display_surface = pygame.display.set_mode((500, 500))

# change the window screen title
pygame.display.set_caption('Our Text')

# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)

# Render the texts that you want to display
text1 = font1.render('GeeksForGeeks', True, (0, 255, 0))
text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))

# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

# setting center for the first text
textRect1.center = (250, 250)

# setting center for the second text
textRect2.center = (250, 300)

while True:

	# add background color using RGB values
	display_surface.fill((255, 0, 0))

	# copying the text surface objects
	# to the display surface objects
	# at the center coordinate.
	display_surface.blit(text1, textRect1)
	display_surface.blit(text2, textRect2)

	# iterate over the list of Event objects
	# that was returned by pygame.event.get()
	# method.
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
		
			# deactivating the pygame library
			pygame.quit()

			# quitting the program.
			quit()

		# update the display
		pygame.display.update()
