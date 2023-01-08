class Settings:
    """save every CLASS of setting in the game"""

    def __init__(self):
        """initialize the settings"""
        # set screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 155, 255)

        # set ship
        self.ship_speed = 3
        self.ship_limit = 3

        # settings of bullets
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 40, 10)
        self.bullet_allowed = 100

        # settings of aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        self.ship_speed = 3
        self.bullet_speed = 5
        self.alien_speed = 2

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)