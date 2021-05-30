from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import numpy as np
"""
2020年10月29日
"""

class WordNet():
    # WordNet

    def remove_punctuation(self, data):
        symbols = "!\"#$%&()*+-.,/:;'<=>?@[\]^_`{|}~\n"
        for i in symbols:
            data = np.char.replace(data, i, '')
        return data

    def penn_to_wn(self, tag):
        """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
        if tag.startswith('N'):
            return 'n'

        if tag.startswith('V'):
            return 'v'

        if tag.startswith('J'):
            return 'a'

        if tag.startswith('R'):
            return 'r'

        return None

    def tagged_to_synset(self, word, tag):

        wn_tag = WordNet.penn_to_wn(self, tag)
        if wn_tag is None:
            return None

        try:
            return wn.synsets(word, wn_tag)[0]
        except:
            return None

    def single_direction_similarity(self, sentence1, sentence2):
        """ compute the sentence similarity using Wordnet """

        # Tokenize and tag
        sentence1 = pos_tag(word_tokenize(sentence1))
        sentence2 = pos_tag(word_tokenize(sentence2))

        # Get the synsets for the tagged words
        synsets1 = [WordNet.tagged_to_synset(self, *tagged_word) for tagged_word in sentence1]
        synsets2 = [WordNet.tagged_to_synset(self, *tagged_word) for tagged_word in sentence2]

        # Filter out the Nones
        synsets1 = [ss for ss in synsets1 if ss]
        synsets2 = [ss for ss in synsets2 if ss]

        score, count = 0.0, 0

        # For each word in the first sentence
        for synset in synsets1:
            # Get the similarity value of the most similar word in the other sentence
            best_score = 0.0
            for ss in synsets2:
                score_temp = synset.path_similarity(ss)
                if score_temp is not None and score_temp > best_score:
                    best_score = score_temp
                    # best_score = max([synset.path_similarity(ss) for ss in synsets2])
            # Check that the similarity could have been computed
            if best_score != 0.0:
                score += best_score
                count += 1

        # Average the values
        if count > 0:
            score /= count
        return score

    def similarity(self, sentence1, sentence2):
        """ compute the symmetric sentence similarity using Wordnet"""
        return (WordNet.single_direction_similarity(self, sentence1, sentence2) + WordNet.single_direction_similarity(
            self, sentence2, sentence1)) / 2

    def array(self, array, num):
        b = array[:, num]
        str = ' '
        strb = []
        for i in range(len(b)):
            strb.append(str(b[i]))
        str1 = str.join(strb)
        return str1

    def test(self, s1, s2):
        # s1 = "noah's ark activity center (jewel case ages 3-8)"
        # s2 = "the beginners bible: noah's ark activity center: activity center"
        # s1 = "disney's 1st & 2nd grade bundle (pixar 1st grade secret keys and aladdin reading quest)"
        # s2 = "wg017449 watchguard firebox x5500e utm software suite - subscription license ( 1 year ) +"
        s01 = str(WordNet.remove_punctuation(self, s1))
        s02 = str(WordNet.remove_punctuation(self, s2))
        print("Similarity", WordNet.similarity(self, s01, s02))
        return WordNet.similarity(self, s01, s02)


if __name__ == '__main__':
    WordNet().test()
