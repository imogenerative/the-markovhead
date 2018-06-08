import markovify
import markov_novel

with open('corpus.txt') as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)
for i in range(2):
	novel = markov_novel.Novel(text_model, chapter_count=15)
	part = 'the-markovhead-part-%s' % (i + 1)
	novel.write(novel_title=part, filetype='md')

novel = markov_novel.Novel(text_model, chapter_count=8)
part = 'the-markovhead-part-%s' % (3)
novel.write(novel_title=part, filetype='md')

novel = markov_novel.Novel(text_model, chapter_count=20)
part = 'the-markovhead-shrugged-part-%s' % (4)
novel.write(novel_title=part, filetype='md')
