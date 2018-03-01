import markovify
import markov_novel

with open('corpus.txt') as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)
for i in range(3):
	novel = markov_novel.Novel(text_model, chapter_count=10)
	part = 'markov-shrugged-part-%s' % (i + 1)
	novel.write(novel_title=part, filetype='md')
