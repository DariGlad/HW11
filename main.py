from flask import Flask, render_template

app = Flask(__name__)
import utils


@app.route('/')
def page_list():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>/')
def page_candidate(candidate_id):
    candidate = utils.get_candidate_by_id(candidate_id)
    if candidate is None:
        return "Нет такого кандидата"
    return render_template('candidate.html', candidate=candidate)


@app.route('/search/<candidate_name>/')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    numbers_of_candidates = len(candidates)
    return render_template('search.html',
                           candidates=candidates,
                           numbers_of_candidates=numbers_of_candidates
                           )


@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    numbers_of_candidates = len(candidates)
    return render_template('skill.html',
                           candidates=candidates,
                           skill_name=skill_name,
                           numbers_of_candidates=numbers_of_candidates
                           )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
