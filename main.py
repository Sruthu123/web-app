from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []

@app.route('/')
def home():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todo_list.append(todo)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_todo():
    todo = request.form.get('todo')
    if todo in todo_list:
        todo_list.remove(todo)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
