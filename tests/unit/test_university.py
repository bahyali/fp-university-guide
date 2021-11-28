from app.controllers.university import UniversityController
from factories.university import university_factory


def test_index_return_list_of_universities(mocker):
    fake_universities = university_factory.create(3)
    mock_model = mocker.patch(
        'app.controllers.university.University')
    mock_model.query.order_by.return_value.all.return_value = fake_universities

    result = UniversityController.index()

    assert result['universities'] == fake_universities
