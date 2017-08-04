from django.shortcuts import render


def mce(request):
    return render(request, 'tt_demo/mce.html')


def mce2(request):
    dict = request.POST
    mce1 = dict.get('mce1')

    return render(request, 'tt_demo/mce2.html', {'mce1': mce1})
