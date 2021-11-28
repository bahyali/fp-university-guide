from app.models.university import University, UniversitySchema


class UniversityController:
    @staticmethod
    def index():
        return {
            'universities': University.query.order_by(University.name.asc()).all(),
        }

    @staticmethod
    def search_api(query):
        raw = UniversityController.search(query)

        schema = UniversitySchema(many=True, only=['name', 'logo'])
        return schema.jsonify(raw)

    @staticmethod
    def search(query):
        return University.query.where(University.name.ilike('%s%%' % query)).all()
