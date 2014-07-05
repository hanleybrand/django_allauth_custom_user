from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):

#    @trace(max_level=10, calls_only=False, ignore=('debugtools', 'blessings', 'ipdb', 'IPython',),
#           ignore_builtins=False, ignore_stdlib=True)
    def save_user(self, request, user, form, commit=False):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        # user_field(user, 'date_of_birth', date_of_birth)
        # when field date_of_birth  (datetime.date(1975, 11, 11),)
        # is evaluated by  user_field, utils.py:80
        #     v = v[0:User._meta.get_field(field).max_length]
        # (or even just v[0] is evaluated on it's own)
        # {TypeError}'datetime.date' object has no attribute '__getitem__'
        # is thrown
        from allauth.account.utils import user_username, user_email, user_field
        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        date_of_birth = data.get('date_of_birth')
        gender = data.get('gender')
        user_email(user, email)
        user_username(user, username)
        user_field(user, 'first_name', first_name or '')
        user_field(user, 'last_name', last_name or '')
        user_field(user, 'gender', gender or '')
        user_field(user, 'date_of_birth', date_of_birth)
        if 'password1' in data:
            user.set_password(user,  data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        print user
        return user
