from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list" :[
    {"restaurant_name":"restaurant_A" , "food_type":"food_A"},
    {"restaurant_name":"restaurant_B" , "food_type":"food_B"},
    {"restaurant_name":"restaurant_C" , "food_type":"food_C"},

    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":
    {"restaurant_name":"restaurant_R" , "food_type":"food_R"},

    }
    return render(request, 'detail.html', context)
