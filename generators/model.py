from templates.Templates import PromptTemplate
from Settings import Settings
import openai

prompt = PromptTemplate()
settings = Settings()

stop_words = ["###", "\n\n", "<br><br>", "The authors: "]

def model(type, template, max_length=200, hmt=1):
    train = ''
    if type == 'title':
        train = prompt.TITLE_TO_ABSTRACST
    if type == 'topic':
        train = prompt.TOPIC_TO_ABSTRACST

    openai.api_key = settings.API_KEY
    response = openai.Completion.create(
        engine="davinci",
        prompt=train + template,
        temperature=0.9,
        max_tokens=max_length,
        top_p=1,
        frequency_penalty=1.0,
        presence_penalty=1.0,
        stop=stop_words,
        best_of=2,
        n=hmt,
    )
    result = []
    for i in range(0, hmt):
        sen = response.choices[i].text
        result.append(sen)

    return {"result": result}
