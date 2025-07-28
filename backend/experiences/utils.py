from utils.embedding import generate_embeddings
from utils.text import extract_lines

from .models import Project, Experience

# ass Experience(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     keywords = models.ManyToManyField(Keyword)
#     ordering = models.PositiveIntegerField(default=0)
#     content = models.TextField()
#     embedding = DefaultVectorField(null=True, default=None)


def generate_project_experience(project: Project):
    # Cleare exisiting experiences for this Project
    Experience.objects.filter(project=project).delete()

    lines = extract_lines(project.content)
    embeddings = generate_embeddings(lines)

    embeddings_to_create = [
        Experience(project=project, ordering=i, content=line, embedding=embedding)
        for i, (line, embedding) in enumerate(zip(lines, embeddings))
    ]

    Experience.objects.bulk_create(embeddings_to_create, ignore_conflicts=True)
