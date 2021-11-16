from flask import Blueprint,redirect,url_for,request,abort,send_from_directory,session
from src.utils.auth0 import auth0
from os import environ
from six.moves.urllib.parse import urlencode

auth0_blueprint = Blueprint('auth0_blueprint', __name__)



@auth0_blueprint.route('/auth0/callback')
def auth0_callback_route():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return  redirect(url_for('admin_blueprint.admin_panel_route'))


@auth0_blueprint.route('/auth0/logout')
def auth0_logout_route():
        # Clear session stored data
    home_url = url_for('home_blueprint.home_route')
    print(home_url)
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home_blueprint.home_route'), 'client_id': environ.get('AUTH0_CLIENT_ID')}
    return redirect(environ.get('AUTH0_DOMAIN') + '/v2/logout?' + urlencode(params))

@auth0_blueprint.route('/auth0/login')
def login_route():
    return auth0.authorize_redirect(redirect_uri=environ.get("AUTH0_CALLBACK"))
