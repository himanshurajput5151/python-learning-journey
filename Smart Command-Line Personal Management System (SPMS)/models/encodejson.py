from decimal import Decimal

from datetime import date, time
import simplejson as json



class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (time, date)):
            return  obj.isoformat()
        if isinstance(obj, Decimal):
            return  str(obj)
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)