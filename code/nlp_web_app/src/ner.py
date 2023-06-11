import spacy
import pandas as pd
from loguru import logger


def build_entity(text):
    nlp = spacy.load('en_core_web_md')
    doc = nlp(text)
    logger.info(f'nlp object created! {text[:10]}...')
    ent_list = []

    for ent in doc.ents:

        ent_dict = {
            'text': ent.text,
            'label':ent.label_,
            'description': spacy.explain(ent.label_)
                   }

        ent_list.append(ent_dict)
    if ent_list == False:
        logger.info('list is empty')

    df = pd.DataFrame(ent_list)
    logger.info(f'Dataframe created successfully!, {df.shape}')
    return df

