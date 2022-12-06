from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html', {'name': 'safa'})

def count(reqest):
    fulltext = reqest.GET['fulltext']
    word_list = fulltext.split()
    word_list_len = len(word_list) - 1
    
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(reqest, 'count.html', {'fulltext': fulltext, 'count': word_list_len, 'worddictionary': sorted_words})