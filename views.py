def user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if  form.is_valid() :
            f = form.save(commit=False)
            return render_to_response('login.html')
    else:
        form = RegisterForm()
    return render_to_response('contact_form.html', {'form':form})
