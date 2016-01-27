from system.core.router import routes


# Users routes
routes['default_controller'] = 'Users'
routes['POST']['/Users/login'] = 'Users#login'
routes['POST']['/Users/register'] = 'Users#register'


routes['POST']['/Posts/post'] = "Posts#post"






routes['/home'] = "Homes#home"


