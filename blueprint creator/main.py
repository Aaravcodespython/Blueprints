from characters import NPC1, NPC2, Pet

wizard = NPC1(name="Jalam", role="Wizard", level=15)

warrior = NPC2(name="Walou", role="Warrior", level=18)

mewmew = Pet(name="MeowMeow", role="mewmew", level=12)

entities = [wizard,warrior,mewmew]

for entity in entities:
    entity.speak()

for entity in entities:
    entity.level_up()
    entity.speak()