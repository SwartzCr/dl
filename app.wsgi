import sys
import site
sys.path.insert(0, '/var/www/link')
site.addsitedir('/var/www/link/lib/python2.7/site-packages')
from app import app as application
