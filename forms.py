from wtforms import Form, StringField, SubmitField, BooleanField, HiddenField, PasswordField
from wtforms.validators import DataRequired, length


class Login(Form):
    username = StringField("username", validators=[DataRequired("提示信息"), length(3, 4, message="输入错误")])
    password = PasswordField("password", validators=[DataRequired("请输入密码"), length(6, 12)])
    remember = BooleanField("remember_me", default=False)
    hidden = HiddenField()
    submit = SubmitField("Sign In")