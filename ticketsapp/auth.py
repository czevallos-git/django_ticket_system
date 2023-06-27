from django.shortcuts import render

def register_page(request):
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')
        print(email)
        print(first_name)
        print(last_name)
        print(password1)
        print(password2)

        # new_user = User(email=email, first_name=first_name, last_name=last_name, password_hash=password1)
        # db.session.add(new_user)
        # db.session.commit()
        # return redirect(url_for('views.home_page'))

    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')