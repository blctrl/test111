
from databroker import Broker
db = Broker.named('temp')
RE.subscribe(db.insert)
