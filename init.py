from flask import Flask, url_for, render_template, request
app = Flask(__name__)
# url_for('static', filename='style.css')

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/map')
def get_map():
    return render_template('map.html')

#@app.route('/post/<int:post_id>')
@app.route('/gettrucks/<loc>', methods=['GET'])
def get_trucks_api(loc):
	if loc != None:
		return generate_trucks_json(loc)
	else:
		return "Location can't be empty."

@app.route('/gettrucks', methods=['POST'])
def get_trucks():
	loc = request.form['loc']
	if loc != None:
		#return find_the_trucks(loc)

		return render_template('map.html', find=loc)
	else:
		return "Location can't be empty."

@app.route('/gettrucks-nearby', methods=['POST'])
def get_trucks_nearby():
	return render_template('map.html', find_nearby=1)

def find_the_trucks(loc):
	return "The input location is: " + loc

def generate_trucks_json(loc):
	return loc
	# return "OK, I'll generate a json for you: " + loc

if __name__ == '__main__':
    app.run(debug=True)
