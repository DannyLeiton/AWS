import yaml

def lambda_handler(event, context):
    print yaml.load("""
        name: Vorlin Laruknuzum
        sex: Male
        class: Priest
        title: Acolyte
        hp: [32, 71]
        sp: [1, 13]
        gold: 423
        inventory:
        - a Holy Book of Prayers (Words of Wisdom)
        - an Azure Potion of Cure Light Wounds
        - a Silver Wand of Wonder
    """)
    print yaml.dump({'name': 'Vorlin Laruknuzum', 'gold': 423, 'title': 'Acolyte', 'hp': [32, 71],
    'sp': [1, 13], 'sex': 'Male', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)',
    'an Azure Potion of Cure Light Wounds', 'a Siver Wand of Wonder'], 'class': 'Priest'})
