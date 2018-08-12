from django.http import HttpResponse
from django.shortcuts import render
import operator
# view for wordcounter

def homepage(request):
    return render(request, 'home.html')

def count(request):
    init_word= request.GET['inputtext']
    simple_word = {}
    smpl_list = ['a', 'and', 'are', 'be', 'by', 'but', 'from','he',
                 'here', 'it' 'just', 'i', 'she', 'to', 'then',
                 'there', 'we', 'you',]
    unique_word = {}

    word_list = init_word.split()

    for word in word_list:
        if word in smpl_list:
            if word in simple_word:
                simple_word[word] += 1
            else:
                simple_word[word] = 1
        else:
            if word in unique_word:
                unique_word[word] +=1
            else:
                unique_word[word] = 1

    sort_simple_word = sorted(simple_word.items(), key=operator.itemgetter(1), reverse=True)
    sort_unique_word = sorted(unique_word.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,
                  'count.html',
                  {'total':len(word_list), 'sorted_simple':sort_simple_word, 'sorted_unique':sort_unique_word},
                  )

def about(request):
    return HttpResponse('<h1>This is tutorial website about counting word in a text</h1>')