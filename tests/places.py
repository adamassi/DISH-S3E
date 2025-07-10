import math

dishwasher_objects = {
    "cups": {
        "tall_cup": {
            "body": "tall_cup",
            "geom": "tall_cup/dish19_fj/",
            "position": [0.53, -0.5, 0.27],
        },
        "tall_cup_1": {
            "body": "tall_cup_1",
            "geom": "tall_cup_1/dish20_fj/",
            "position": [0.43, -0.2, 0.26],
        },
        "tall_cup_2": {
            "body": "tall_cup_2",
            "geom": "tall_cup_2/dish21_fj/",
            "position": [0.43, -0.3, 0.25],
        },
        "tall_cup_3": {
            "body": "tall_cup_3",
            "geom": "tall_cup_3/dish22_fj/",
            "position": [0.63, -0.2, 0.25],
        },
        "tall_cup_4": {
            "body": "tall_cup_4",
            "geom": "tall_cup_4/dish23_fj/",
            "position": [0.43, -0.52, 0.27],
        },
        "tall_cup_5": {
            "body": "tall_cup_5",
            "geom": "tall_cup_5/dish24_fj/",
            "position": [0.63, -0.4, 0.25],
        },
        "tall_cup_6": {
            "body": "tall_cup_6",
            "geom": "tall_cup_6/dish25_fj/",
            "position": [0.63, -0.5, 0.25],
        },
        "tall_cup_7": {
            "body": "tall_cup_7",
            "geom": "tall_cup_7/dish26_fj/",
            "position": [0.63, -0.3, 0.25],
        },
        "tall_cup_8": {
            "body": "tall_cup_8",
            "geom": "tall_cup_8/dish27_fj/",
            "position": [0.45, -0.4, 0.25],
        },
    },
    "wine_glasses": {
        "wine_glass": {
            "body": "wine_glass",
            "geom": "wine_glass/dish15_fj/",
            "position": [0.53, -0.4, 0.25],
        },
        "wine_glass_1": {
            "body": "wine_glass_1",
            "geom": "wine_glass_1/dish16_fj/",
            "position": [0.53, -0.3, 0.25],
        },
        "wine_glass_2": {
            "body": "wine_glass_2",
            "geom": "wine_glass_2/dish17_fj/",
            "position": [0.54, -0.2, 0.25],
        },
    },
    "utensils": {
        "knife": {
            "body": "knife",
            "geom": "knife/dish13_fj/",
            "position": [0.77, -0.2, 0.37],
        },
        "spoon": {
            "body": "spoon",
            "geom": "spoon/dish31_fj/",
            "position": [0.77, -0.23, 0.27],
        },
        "spoon_1": {
            "body": "spoon_1",
            "geom": "spoon_1/dish32_fj/",
            "position": [0.77, -0.25, 0.27],
        },
    }
}






dishwasher_objects_has_space_down_rack = {
    "cups": {
        "tall_cup": {
            "body": "tall_cup",
            "geom": "tall_cup/dish19_fj/",
            "position": [0.53, -0.5, 0.29],
            "rotation": None,
        },
        "tall_cup_1": {
            "body": "tall_cup_1",
            "geom": "tall_cup_1/dish20_fj/",
            "position": [0.43, -0.2, 0.29],
            "rotation": None,
        },
        "tall_cup_2": {
            "body": "tall_cup_2",
            "geom": "tall_cup_2/dish21_fj/",
            "position": [0.43, -0.3, 0.29],
            "rotation": None,
        },
        "tall_cup_3": {
            "body": "tall_cup_3",
            "geom": "tall_cup_3/dish22_fj/",
            "position": [0.63, -0.2, 0.29],
            "rotation": None,
        },
        "tall_cup_4": {
            "body": "tall_cup_4",
            "geom": "tall_cup_4/dish23_fj/",
            "position": [0.43, -0.5, 0.29],
            "rotation": None,
        },
        "tall_cup_5": {
            "body": "tall_cup_5",
            "geom": "tall_cup_5/dish24_fj/",
            "position": [0.63, -0.4, 0.29],
            "rotation": None,
        },
        "tall_cup_6": {
            "body": "tall_cup_6",
            "geom": "tall_cup_6/dish25_fj/",
            "position": [0.63, -0.5, 0.29],
            "rotation": None,
        },
        "tall_cup_7": {
            "body": "tall_cup_7",
            "geom": "tall_cup_7/dish26_fj/",
            "position": [0.63, -0.3, 0.29],
            "rotation": None,
        },
        "tall_cup_8": {
            "body": "tall_cup_8",
            "geom": "tall_cup_8/dish27_fj/",
            "position": [0.43, -0.4, 0.29],
            "rotation": None,
        },
    },
    "wine_glasses": {
        "wine_glass": {
            "body": "wine_glass",
            "geom": "wine_glass/dish15_fj/",
            "position": [0.53, -0.4, 0.29],
            "rotation": None,
        },
        "wine_glass_1": {
            "body": "wine_glass_1",
            "geom": "wine_glass_1/dish16_fj/",
            "position": [0.53, -0.3, 0.29],
            "rotation": None,
        },
        "wine_glass_2": {
            "body": "wine_glass_2",
            "geom": "wine_glass_2/dish17_fj/",
            "position": [0.54, -0.2, 0.29],
            "rotation": None,
        },
    },
    "utensils": {
        "knife": {
            "body": "knife",
            "geom": "knife/dish13_fj/",
            "position": [0.77, -0.175, 0.35],
            "rotation": [0, 0, - math.pi / 2],
        },
        "spoon": {
            "body": "spoon",
            "geom": "spoon/dish31_fj/",
            "position": [0.77, -0.23, 0.27],
            "rotation": [0, 0, math.pi / 2],
        },
        "spoon_1": {
            "body": "spoon_1",
            "geom": "spoon_1/dish32_fj/",
            "position": [0.77, -0.25, 0.27],
            "rotation": [0, 0, math.pi / 2],
        },
        # "knife_1": {
        #     "body": "knife_1",
        #     "geom": "knife_1/dish14_fj/",
        #     "position": [0.77, -0.23, 0.5],
        #     "rotation": [0, 0, math.pi / 2],
        # },
        # "wood_spoon": {
        #     "body": "wood_spoon",
        #     "geom": "wood_spoon/dish7_fj/",
        #     "position": [0.77, -0.27, 0.5],
        #     "rotation": [0, 0, - math.pi / 2],
        # },
        # "wood_spoon_1": {
        #     "body": "wood_spoon_1",
        #     "geom": "wood_spoon_1/dish8_fj/",
        #     "position": [0.77, -0.29, 0.5],
        #     "rotation": [0, 0, - math.pi / 2],
        # },
        # "wood_spoon_2": {
        #     "body": "wood_spoon_2",
        #     "geom": "wood_spoon_2/dish9_fj/",
        #     "position": [0.77, -0.31, 0.5],
        #     "rotation": [0, 0, - math.pi / 2],
        # },
        # "wood_spoon_3": {
        #     "body": "wood_spoon_3",
        #     "geom": "wood_spoon_3/dish10_fj/",
        #     "position": [0.77, -0.33, 0.5],
        #     "rotation": [0, 0, math.pi / 2],
        # },
        # "wooden_fork": {
        #     "body": "wooden_fork",
        #     "geom": "wooden_fork/dish11_fj/",
        #     "position": None,
        #     "rotation": [0, 0, math.pi / 2],
        # },
        # "wooden_fork_1": {
        #     "body": "wooden_fork_1",
        #     "geom": "wooden_fork_1/dish12_fj/",
        #     "position": None,
        #     "rotation": [0, 0, math.pi / 2],
        # },
        # "fork": {
        #     "body": "fork",
        #     "geom": "fork/dish33_fj/",
        #     "position": None,
        #     "rotation": [0, 0, math.pi / 2],
        # }
    }
}