from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        user_role = self.request.user.role
        if user_role == 'admin':
            return '/admin_dashboard/'
        elif user_role == 'sales_manager':
            return '/sales_manager_dashboard/'
        elif user_role == 'hr':
            return '/hr_dashboard/'
        elif user_role == 'labour':
            return '/labour_dashboard/'
        return super().get_success_url()
