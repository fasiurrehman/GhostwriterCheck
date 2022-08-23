
from .model import model


def title_to_abstract_generator(template):
    return model('title', template)
