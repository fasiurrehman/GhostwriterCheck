from .model import model


def topic_to_abstract_generator(template):
    return model('topic', template)
