base_url = 'https://stellarburgers.nomoreparties.site'


class Endpoint:
    login_endpoint = '/login'
    recovery_password_endpoint = '/forgot-password'
    reset_password_endpoint = '/reset-password'
    profile_endpoint = '/account/profile'
    order_history_endpoint = '/account/order-history'
    order_feed_endpoint = '/feed'

    create_user_endpoint = '/api/auth/register'
    delete_user_endpoint = '/api/auth/user'
