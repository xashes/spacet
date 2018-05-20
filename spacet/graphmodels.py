import neomodel as nm

# Relationship Models


class ComponentRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    rating = nm.IntegerProperty()
    relevancy = nm.IntegerProperty()
    weight = nm.FloatProperty()


class ProductRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    rating = nm.IntegerProperty()
    contribution = nm.IntegerProperty()


class StakeRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    shareholding_ratio = nm.FloatProperty()


# Label Models
class Company(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    symbol = nm.StringProperty()
    market = nm.StringProperty()
    list_date = nm.IntegerProperty()
    updated = nm.DateTimeProperty(default_now=True)

    concept = nm.RelationshipTo(
        'Concept',
        'COMPONENT_OF',
        model=ComponentRel)
    industry = nm.RelationshipTo(
        'Industry',
        'COMPONENT_OF',
        model=ComponentRel)
    index = nm.RelationshipTo(
        'Industry',
        'COMPONENT_OF',
        model=ComponentRel)
    customer = nm.RelationshipTo(
        'Company', 'SUPPLIES_TO')
    product = nm.RelationshipTo('Product', 'PRODUCES', model=ProductRel)


class Index(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    symbol = nm.StringProperty()
    market = nm.StringProperty()
    list_date = nm.IntegerProperty()
    updated = nm.DateTimeProperty(default_now=True)


class Fund(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    rating = nm.IntegerProperty()

    company = nm.RelationshipTo('Company', 'STAKES', model=StakeRel)


class Concept(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    rating = nm.IntegerProperty()
    heat = nm.IntegerProperty()


class Industry(Concept):
    pass


class Product(nm.StructuredNode):
    pass


class order(nm.StructuredNode):
    price = nm.FloatProperty()
    quantity = nm.FloatProperty()
    date = nm.DateTimeProperty(default_now=True)

    company = nm.RelationshipTo('Company', 'ORDER')
