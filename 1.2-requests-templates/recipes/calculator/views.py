from django.shortcuts import render


def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * servings,
            'молоко, л': 0.1 * servings,
            'соль, ч.л.': 0.5 * servings,
        },
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        },
    }
    return render(request, 'calculator/index.html', context)


def buter_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * servings,
            'колбаса, ломтик': 1 * servings,
            'сыр, ломтик': 1 * servings,
            'помидор, ломтик': 1 * servings,
        },
    }
    return render(request, 'calculator/index.html', context)


def soup_lukovyi_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * servings,
            'лук, кг': 1 * servings,
            'бульон, литр': 1 * servings,
            'сыр, грамм': 100 * servings,
        },
    }
    return render(request, 'calculator/index.html', context)
