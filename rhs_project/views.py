from django.shortcuts import render, redirect

def admin_redirect(request):
    return redirect('admin:index')