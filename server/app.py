from flask import Flask, request, send_file
from flask import render_template
import os
import transfer
import imageio

app = Flask(__name__)

@app.after_request 
def add_header(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

@app.route("/", methods=["GET", "POST"])
def upload():
	if request.method == 'POST':
		file1 = request.files['file1']
		file2 = request.files['file2']
		iterations = int(request.form['slider'])
		print("---------------------------------------" + str(iterations))
		file1.save('./file1')
		file2.save('./file2')
		
		best, best_loss = transfer.run_style_transfer("file1", "file2", num_iterations=iterations)
		imageio.imwrite('outfile.jpg', best)

		return send_file('outfile.jpg', mimetype='image/jpg')
	else:
		return render_template('index.html')
		
