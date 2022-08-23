from flask import Flask, request
from generators.title_to_abstract import title_to_abstract_generator
from generators.topic_to_abstract import topic_to_abstract_generator
app = Flask(__name__)
max_length_char = 360


@app.route('/')
def rewriter():
    data = request.get_json(silent=True)
    if data is None:
        return 'No data received'
    else:
        if data.get('title') is None and data.get('topic') is not None:
            return generate(data, 'topic')
        elif data.get('title') is not None:
            return generate(data, 'title')
        else:
            return 'No data received'


def generate(data, value):
    obj = abstract_generator_obj(value)
    result = obj(
        template_generator('topic', data[value]))
    if len(result['result'][0]) > 10:
        return {"result": result['result']}
    else:
        result_re = obj(
            template_generator(value, data[value]))
        while len(result_re['result'][0]) < 5:
            print("getting results again")
            result_re = obj(
                template_generator(value, data[value]))
        if len(result_re['result'][0]) > 0:
            return {"result": result_re['result']}


def abstract_generator_obj(value):
    if value == 'title':
        return title_to_abstract_generator
    else:
        return topic_to_abstract_generator


def template_generator(type, value):
    if type == 'title':
        return "title:" + value + "\n" + 'abstract:'
    else:
        keyword_str = "\n"
        for k in value:
            keyword_str = keyword_str + k + "\n"
        return "topic:" + keyword_str + "\n" + 'abstract:'


if __name__ == '__main__':
    app.run()
