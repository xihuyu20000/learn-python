from typing import Dict


# 作者，机构，关键词

# = namedtuple('BiblioModel', ['doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'])

class BiblioModel:
    def __init__(self, doctype='', authors='', orgs='', title='', source='', pubyear='', kws='', abs=''):
        self.doctype = doctype
        self.authors = authors
        self.orgs = orgs
        self.title = title
        self.source = source
        self.pubyear = pubyear
        self.kws = kws
        self.abs = abs

    def __eq__(self, other):
        return (self.authors == other.authors
                and self.orgs == other.orgs
                and self.title == other.title
                and self.kws == other.kws)

    def to_dict(self):
        return {'doctype': self.doctype, 'authors': self.authors, 'orgs': self.orgs, 'title': self.title,
                'source': self.source, 'pubyear': self.pubyear, 'kws': self.kws, 'abs': self.abs}

    @staticmethod
    def from_cnki_gbt7714_2015(raw: Dict):
        # 'doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'
        doctype = raw['doctype']
        authors = ','.join([a.strip() for a in raw['authors'].strip().split(',') if a.strip()])
        orgs = ''
        title = raw['title']
        source = raw['source']
        pubyear = ''
        kws = ''
        abs = ''

        return BiblioModel(doctype=doctype, authors=authors, orgs=orgs, title=title, source=source, pubyear=pubyear,
                           kws=kws, abs=abs)

    @staticmethod
    def from_cnki_refworks(raw: Dict):
        # 'doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'
        doctype = raw['RT']
        authors = ','.join([a.strip() for a in raw['A1'].strip().split(';') if a.strip()])
        orgs = ','.join([a.strip() for a in raw['AD'].strip().split(';') if a.strip()])
        title = raw['T1']
        source = raw['JF']
        pubyear = ''
        kws = ','.join([a.strip() for a in raw['K1'].strip().split(',') if a.strip()])
        abs = raw['AB']

        if len(raw['YR']) > 0:
            pubyear = raw['YR']
        elif len(raw['FD']) > 0:
            pubyear = raw['FD'][:4]

        return BiblioModel(doctype=doctype, authors=authors, orgs=orgs, title=title, source=source, pubyear=pubyear,
                           kws=kws, abs=abs)
