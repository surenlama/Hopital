from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

class UserAccessMixins(LoginRequiredMixin, UserPassesTestMixin):
    user_access_type = []

    def test_func(self):
        user = self.request.user
        user_type = user.user_type
        
        if user_type in self.user_access_type:
            return True
        return False
    
    def handle_no_permission(self):
        return redirect('dashboard')