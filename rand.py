import markovify
import markov_novel

with open('corpus.txt') as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
novel = markov_novel.Novel(text_model, chapter_count=1)
novel.write(novel_title='markov-shrugged', filetype='md')
