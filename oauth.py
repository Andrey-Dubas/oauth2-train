from app import app
import os

if __name__ == '__main__':
    print(os.environ.get('PORT'))
    app.run(threaded=True, port=os.environ.get('PORT') or 5000)