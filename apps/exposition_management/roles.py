ROLE_MANAGER = 'manager'
ROLE_BIOLOGIST = 'biologist'
ROLE_DESIGNER = 'designer'


def user_roles(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return {
        'is_manager': ROLE_MANAGER in ug,
        'is_biologist': ROLE_BIOLOGIST in ug,
        'is_designer': ROLE_DESIGNER in ug,
    }
