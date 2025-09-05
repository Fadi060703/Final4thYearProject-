# permissions.py
from rest_framework.permissions import BasePermission

class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        method_roles = getattr(view, 'method_roles', {}).get(request.method)
        if method_roles is None:
            method_roles = getattr(view, 'required_roles', [])
        if method_roles and hasattr(request.user, 'role') and request.user.role:
            user_role = request.user.role.name.lower()
            return any(role.lower() == user_role for role in method_roles)
        
        return False  
    
    
'''
    method_roles = {
        'GET': ['accountant', 'manager', 'viewer'],  # Multiple roles can view
        'POST': ['accountant']  # Only accountant can create
    }
    
    permission_classes = [HasRolePermission]
'''