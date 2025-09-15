from utils.llm import generate_embeddings
from utils.keywords import extract_keywords_for_lines, clean_experience_paragraph
from utils.text import extract_lines

from .models import Project, Experience, Keyword


def generate_project_experience(project: Project):
    # Cleare existing experiences for this Project
    Experience.objects.filter(project=project).delete()

    lines = extract_lines(project.cleaned_content)
    embeddings = generate_embeddings(lines)

    embeddings_to_create = [
        Experience(project=project, ordering=i, content=line, embedding=embedding)
        for i, (line, embedding) in enumerate(zip(lines, embeddings))
    ]

    Experience.objects.bulk_create(embeddings_to_create, ignore_conflicts=True)

    keyword_lists = extract_keywords_for_lines(lines)

    all_keywords = set(kw for kw_list in keyword_lists for kw in kw_list)
    keyword_objs_to_create = [Keyword(name=name) for name in all_keywords]
    Keyword.objects.bulk_create(keyword_objs_to_create, ignore_conflicts=True)
    keyword_objs = {k.name: k for k in Keyword.objects.filter(name__in=all_keywords)}

    # Fetch saved experiences in order to assign keywords
    saved_experiences = list(
        Experience.objects.filter(project=project).order_by("ordering")
    )

    # Assign keywords to each experience
    for exp, kw_list in zip(saved_experiences, keyword_lists):
        kws = [keyword_objs[kw] for kw in kw_list]
        exp.keywords.set(kws)
    
