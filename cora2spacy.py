#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import glob
import spacy
from spacy.tokens import DocBin, Doc
from spacy.lookups import Lookups
from spacy.vocab import Vocab
import srsly
from lxml import etree
from pathlib import Path, PurePath
import warnings
import random


class cora2spacy:
    def __init__(self):
        self.corpus = []
        self.nlp = spacy.blank("de")

    def populate(self, globFiles: str):
        for path in glob.glob(globFiles):
            self.corpus.append(path)

    def reset(self, glob: str):
        self.corpus = []

    def _spacySentence(self, vocab:Vocab, sentenceTokens: list, category: str, serialization: str) -> Doc:        
        words= []
        pos= []
        lemmata=[]
        for token in sentenceTokens:
            string = token.find(f'.//{serialization}')
            if string is not None:
                tokenString = string.get('tag')
                tag = token.find(f'.//{category}')
                lemma = token.find(f'.//lemma')
                if tag is not None and lemma is not None:
                    words.append(tokenString)
                    pos.append(tag.get('tag'))
                    lemmata.append(lemma.get('tag'))

        return Doc(vocab, words=words, tags=pos, lemmas=lemmata)

    def tagSentences(self, vocab: Vocab, category: str = 'pos', serialization: str = 'norm') -> list:
        # see https://linguistics.rub.de/forschung/arbeitsberichte/19.pdf: 11
        puncDelimiters = ['DE', 'IE', 'EE', 'QE']
        sentenceTokens = []
        spacySentences = []
        for path in self.corpus:
            tree= etree.parse(path)
            print (f'Working on {path}')
            for token in tree.iterfind('//token'):
                punc = token.find('./tok_anno/punc')
                if punc is not None and punc.get('tag') in puncDelimiters:
                    sentenceTokens.append(token)
                    sentence = self._spacySentence(
                        sentenceTokens=sentenceTokens, category=category, serialization=serialization, vocab=vocab)
                    spacySentences.append(sentence)
                    sentenceTokens = []
                else:
                    sentenceTokens.append(token)
        return spacySentences

    def serializeSentences(self, sentences: list, outputPath: Path , format: str = 'spacy'):
        if format=='spacy':
            db = DocBin()       

            for sentence in sentences: 
                db.add(sentence)
            db.to_disk(outputPath)
        elif format=='text':
            lines=[]
            for sentence in sentences:
                tokens= []
                for token in sentence:
                    tokens.append(token.text)
                sentenceString= ' '.join(tokens)    
                lines.append(sentenceString)
            with open(outputPath, 'w') as f:
                f.write('\n'.join(lines))

    def _lookups(self,lang:str='de')->Lookups:
        d={}
        for path in self.corpus:
            tree = etree.parse(path)
            for token in tree.iterfind('//token'):
                try:
                    lemma = token.find('.//lemma').get('tag')
                    string = token.find('.//norm').get('tag')
                    d[string]=lemma
                except:
                    pass                        
        lookups = Lookups()
        lookups.add_table('lemma_lookup', d)
        return lookups

    def vocab(self) -> Vocab:
        print ('Generate vocab')
        v = Vocab(lookups=self._lookups())
        
        return v

if __name__ == "__main__":
    """
        Converts cora data to spacy training data

        Usage:        

        $ python cora2spacy.py --h 
            for parameter list
    """

    parser = argparse.ArgumentParser(
        description='Build ontology from source'
    )
    parser.add_argument(
        "--globFiles",
        type=str,
        default='./data/REM/*.xml',
        help="Glob to cora corpus files")
    parser.add_argument(
        "--sampleSize",
        type=float,
        default=0.8,
        help="Size of train data. 0.8 means 80% of the corpus is used for training, 20% for testing")
        

    args = parser.parse_args()

    converter = cora2spacy()
    converter.populate(globFiles=args.globFiles)
    vocab= converter.vocab()
    sentences = converter.tagSentences(vocab=vocab)
    random.shuffle(sentences)
    cut_off = int(args.sampleSize*len(sentences))
    trainData = sentences[:cut_off]
    devData = sentences[cut_off:]
    converter.serializeSentences(sentences=trainData,
                                 outputPath=Path('./corpus/train.spacy'), format='spacy')
    converter.serializeSentences(sentences=devData,
                                 outputPath=Path('./corpus/dev.spacy'), format='spacy')
    converter.serializeSentences(sentences=trainData,
                                 outputPath=Path('./test/train.txt'), format='text')                             
    converter.serializeSentences(sentences=devData,
                                 outputPath=Path('./test/dev.txt'), format='text')
