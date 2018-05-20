from neomodel import db
import neomodel as nm
from tdata import local
import jaqs.util as jutil
from app.graphmodels import Company, Index, Fund, Concept, Industry, Product


def create_nodes(df):
    nodes = df.loc[:, ['list_date', 'market', 'name', 'symbol']]
    Index.create_or_update(*nodes.to_dict('records'))


def delete_db():
    db.set_connection('bolt://neo4j:ivey198013@192.168.199.140:7687')
    nm.clear_neo4j_database(db)
