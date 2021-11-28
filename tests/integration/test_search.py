from app import db
from app.controllers.university import UniversityController
from factories.university import university_factory


def test_university_search(app):
    unis = university_factory.create(5)
    uni_to_find = unis[1]

    with app.app_context():
        commit_universities(unis)

        search_results = UniversityController.search(uni_to_find.name[:4])

    assert len(search_results) > 0
    assert uni_to_find in search_results


def test_university_no_search_results(app):
    unis = university_factory.create(5)

    with app.app_context():
        commit_universities(unis)

        search_results = UniversityController.search('Should not find this uni')

    assert len(search_results) == 0
    assert search_results == []


def commit_universities(unis):
    for uni in unis:
        db.session.add(uni)
    db.session.commit()
