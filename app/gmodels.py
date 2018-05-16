from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Company(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    symbol = Property()
    list_date = Property()
    market = Property()
    updated = Property()

    concept = RelatedTo('Concept', 'HAS')
    industry = RelatedTo('Industry', 'IN')
    index = RelatedTo('Index', 'COMPONENT_OF')
    customer = RelatedTo('Company', 'SUPPLIES_TO')
    product = RelatedTo('Product', 'PRODUCES')


class Concept(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    rating = Property()
    heat = Property()

    company = RelatedFrom('Company')