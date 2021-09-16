#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy

nlp = spacy.load('./models/model-best')
doc = nlp('sô solte ime ouch di burc wesen vile tiure ne hæte si mit den viure unde mit den mangen niet bestân')

for w in doc:
    print(f'{w.text} – {w.tag_}')
