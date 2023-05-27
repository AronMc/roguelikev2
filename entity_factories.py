from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char ="@",
    color=(255, 255, 255),
    name="LabMouse",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=17, base_defense=1, base_power=2),
    inventory=Inventory(capacity=15),
    level=Level(level_up_base=21,)
)

mouse = Actor(
    char="m",
    color=(63, 127, 63),
    name="Mouse",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=14),
)
rat = Actor(
    char="R",
    color=(0, 127, 0),
    name="Rat",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=14, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=15),
    )

confusion_gas = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Gas",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

napalm_pack = Item(
    char="~",
    color=(255, 0, 0),
    name="Napalm Pack",
    consumable=consumable.NapalmDamageConsumable(damage=18, radius=2),
)

health_stim = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Stim",
    consumable=consumable.HealingConsumable(amount=4)
)
battery_pack = Item(
    char="~",
    color=(255, 255, 0),
    name="Battery Pack",
    consumable=consumable.BatteryDamageConsumable(damage=19, maximum_range=3),
)

chopper = Item(
    char="/", color=(0, 191, 255), name="Chopper", equippable=equippable.Chopper()
)

axe = Item(char="/", color=(0, 191, 255), name="Axe", equippable=equippable.Axe())

cloth_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Cloth Armor",
    equippable=equippable.ClothArmor(),
)

leather_armor = Item(
    char="[", color=(139, 69, 19), name="Leather Armor", equippable=equippable.LeatherArmor()
)