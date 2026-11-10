from ursina import *

# Creates a window
app = Ursina()

# naming window
window.title = "Legend of Arhke: Noct to the Past"

# The ground
ground = Entity(
    model="plane",
    scale=20,
    color=color.green

)

# temp player
class Player(Entity):
    def __init__(self) -> None:
        super().__init__(
            model='cube',
            color=color.azure

        )

# run game until exited
app.run()
