import spacy  # importing spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# It is interesting that there is more similarity between the monkey and the banana than the apple, so the fact that monkeys eat bananas is recognised
# It is also interesting that there is very little similarity between the cat and the fruits, so it must recognise that cats are carnivores

new_tokens = nlp("universe earth moon star")

for token1 in new_tokens:
    for token2 in new_tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# universe and the earth has the greatest similarity of 59%, earth and star have he lowest at 13%
# It is interesting that the moon, star and universe all have fairly low siilarities

# When running the example file with en_core_web_sm instead of en_core_web_md, a warning is displayed before the results that says:

# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
# which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, 
# or use one of the larger models instead if available

# When looking at the results there is also a difference in the similarity results thn usinf the md model
