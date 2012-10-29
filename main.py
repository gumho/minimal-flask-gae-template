import sys, os

package_dir_path = os.path.join(os.path.dirname(__file__), 'packages')
sys.path.insert(0, package_dir_path)

from myapp import app