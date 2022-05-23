import json

DATA_PATH = "data/candidates.json."


def load_candidates_from_json(path=DATA_PATH):
    """возвращает список всех кандидатов"""

    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_all_candidates():
    """возвращает список всех кандидатов"""
    candidates = load_candidates_from_json()
    return candidates


def get_candidate_by_id(candidate_id):
    """возвращает одного кандидата по его id"""

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""

    candidates = load_candidates_from_json()
    candidates_found = []
    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower().split():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""

    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        skills = candidate.get("skills")
        list_of_skills = skills.lower().split(", ")
        if skill_name in list_of_skills:
            candidates_found.append(candidate)

    return candidates_found
