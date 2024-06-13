from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import resolve

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            ## only functional with one group
            # group = None
            # if request.user.groups.exists():
            #     group = request.user.groups.all()[0].name
            # if group in allowed_roles:
            #     return view_func(request, *args, **kwargs)
            # else:
            #     #current_url = resolve(request.path_info).url_name
            #     previous_url = request.META.get('HTTP_REFERER')
            #     messages.success(request, "Up yours, chump!")
            #     return redirect(previous_url)
            
            ## revised
            group = None
            if request.user.groups.exists():
                groups = request.user.groups.all()
                group_list = []
                counter = 0
                for group in groups:
                    print(group)                    
                    group_list.append(group.name)
                    print(group_list)
                    counter += 1

            for group in group_list:
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
            else:
                #current_url = resolve(request.path_info).url_name
                previous_url = request.META.get('HTTP_REFERER')
                messages.success(request, "Up yours, chump!")
                return redirect(previous_url)

            
        return wrapper_func
    return decorator