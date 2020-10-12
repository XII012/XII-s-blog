from django.shortcuts import render

# Create your views here.


def post_list(request):
    # 用render方法调用blog/post_list.html模板进行渲染
    return render(request, 'blog/post_list.html', {})
