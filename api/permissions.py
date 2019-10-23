from rest_framework.permissions import BasePermission

class IsItemOwner(BasePermission):
	message = "Only staff or item creators can access here."

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.added_by == request.user):
			return True
		else:
			return False
