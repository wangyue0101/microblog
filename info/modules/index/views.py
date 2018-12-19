from flask import request, flash, redirect, url_for, render_template
from forms import Login
from . import index_blue


@index_blue.route("/", methods=['GET', 'POST'])
def index():
    form = Login(request.form)
    if request.method == 'POST' and form.validate():
        print("123", form.validate())
        flash(
            "Success, Login Requested for Openid = " + form.username.data + ", remember_me=" + str(form.remember.data))
        print("username", form.username.data)
        return render_template("login.html", title="New Micreblog", form=form)
    return render_template("login.html", title="New Micreblog", form=form)