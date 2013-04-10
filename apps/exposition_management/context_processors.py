ROLE_MANAGER = 'manager'
ROLE_BIOLOGIST = 'biologist'
ROLE_DESIGNER = 'designer'


def user_roles(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return {
        'is_manager': ROLE_MANAGER in user_groups,
        'is_biologist': ROLE_BIOLOGIST in user_groups,
        'is_designer': ROLE_DESIGNER in user_groups,
    }
