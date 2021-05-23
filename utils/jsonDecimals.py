
import json
from decimal import Decimal as D

# d1 = D(11) / D(10) # 1.1
# d2 = D(22) / D(10) # 2.2
# f1 = 1.1
# f2 = 2.2

# See http://docs.python.org/2/library/json.html
# Extending JSONEncoder:
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, D):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

# print(json.dumps({'a': f1+f2}))
# # {"a": 3.3000000000000003} # This is not what we want, should be 3.3 exactly

# #print json.dumps({'a': d1+d2})
# # Fails for json encoding of decimal

# print(DecimalEncoder().encode({'a': d1+d2}))
# # {"a": 3.3}