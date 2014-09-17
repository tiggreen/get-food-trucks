from flask import Flask, url_for, render_template, request
app = Flask(__name__)

# Setting up the index route.
@app.route('/')
def get_index():
    return render_template('index.html')

# Allowing people to see the SF map with trucks on it. 
@app.route('/map', methods=['GET'])
def get_map():
    return render_template('map.html')


@app.route('/gettrucks/<loc>', methods=['GET'])
def get_trucks_api(loc):
	if loc != None:
		return render_template('map.html', find=loc)
	else:
		return "Location can't be empty."

@app.route('/gettrucks', methods=['POST'])
def get_trucks():
	loc = request.form['loc']
	if loc != None:
		return render_template('map.html', find=loc)
	else:
		return "Location can't be empty."

if __name__ == '__main__':
    app.run()
