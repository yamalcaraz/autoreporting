import os
from flask import Flask, render_template, request
# from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	return render_template('upload.html')

@app.route('/upload' ,methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist('file'):
		print(file)
		filename = file.filename
		destination = '/'.join([target,filename])
		print(destination)
		file.save(destination)
	return render_template('complete.html')

# Configure Jinja and ready the template
# env = Environment(
#     loader=FileSystemLoader(searchpath="templates")
# )
# template = env.get_template("report.html")


# def main():
#     """
#     Entry point for the script.
#     Render a template and write it to file.
#     :return:
#     """
#     with open("outputs/report.html", "w") as f:
#         f.write(template.render(content=content))


if __name__ == "__main__":
    app.run(port=4555,debug=True)
