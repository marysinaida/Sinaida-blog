from myblog import create_app
from myblog.models import *

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)