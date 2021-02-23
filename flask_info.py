from location import read_file, get_locations, create_map, generate_map
from twit import get_user_info, write_to_file
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    '''
    Home page
    '''

    return render_template("index.html")

@app.route("/input", methods=["POST"])
def get_data_from_user():
    '''
    Gets bearer token and Twitter handle from user
    '''

    handle = request.form.get("handle")
    bearer = request.form.get("bearer")
    return f'{handle} {bearer}'

@app.route("/input/map", methods=["POST"])
def map_generator():
    '''
    Returns map with follower locations to user
    '''
    try:
        try:
            data = get_data_from_user().split()
            handle = data[0]
            bearer = data[1]
            file = write_to_file(get_user_info(handle, bearer))
            follower_map = generate_map('user_info.json')
            return follower_map.get_root().render()
        except IndexError:
            return render_template('error.html')
    except KeyError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)