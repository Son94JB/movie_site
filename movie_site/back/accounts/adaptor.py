from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.reg_no = data.get('profile_image')
        user.department = data.get('profile_text')
        user.university = data.get('movies')
        user.save()
        return user