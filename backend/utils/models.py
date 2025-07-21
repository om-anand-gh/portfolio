from django.conf import settings
from pgvector.django import VectorField as PGVectorField

class DefaultVectorField(PGVectorField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("dimensions", settings.PGVECTOR_FIELD_DIMENSIONS)
        super().__init__(*args, **kwargs)