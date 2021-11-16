import os
from flask import session,redirect,url_for
from functools import wraps

from authlib.integrations.flask_client import OAuth

oauth = OAuth()

auth0 = oauth.register(
    'auth0',
    client_id=os.environ.get('AUTH0_CLIENT_ID'),
    client_secret=os.environ.get('AUTH0_CLIENT_SECRET'),
    api_base_url=os.environ.get('AUTH0_DOMAIN'),
    access_token_url='{}/oauth/token'.format(os.environ.get('AUTH0_DOMAIN')),
    authorize_url='{}/authorize'.format(os.environ.get('AUTH0_DOMAIN')),
    client_kwargs={
        'scope': 'openid profile email',
    },
)


def authorization_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect(url_for("auth0_blueprint.login_route"))
    return f(*args, **kwargs)

  return decorated