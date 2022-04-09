from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET',))
def index():
    return render_template('index.html')

def randomize(texts: list[str]):
    if not texts:
        return ['']
    new_combos = []
    for idx, start in enumerate(texts):
        combos = randomize(texts[:idx] + texts[idx+1:])
        for end in combos:
            new_combos.append(f'{start} {end}')
    return new_combos

@bp.route('/api', methods=('GET','POST'))
def api():
    if request.method == 'GET':
        return jsonify({'lamog': True})
    else:
        return jsonify({'lamog': randomize(request.form['fname'].split())})