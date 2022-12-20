from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'soup_lukovyi': {
        'хлеб, ломтик': 1,
        'лук, кг': 1,
        'бульон, литр': 1,
        'сыр, грамм': 100,
    },
}
DEFUALT_SERVINGS_COUNT = 1


def dish_view(request, dish):
    servings = int(request.GET.get('servings', DEFUALT_SERVINGS_COUNT))
    recipe = {}    
    if dish in DATA.keys():
        recipe = DATA[dish]
    for ingredient in recipe:
        recipe[ingredient] = recipe[ingredient] * servings
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
