# Converts dict to object
# Used in comm.py RosBridgeProtocol(object)._handle_publish(self, message):

class ConversionHelper:
    @staticmethod
    def grabAttrs(d):
        values = {}
        for k,v in d.items():
            newAttr = ConversionHelper.grabAttr(k, v)
            values[k] = newAttr
        return values
    @staticmethod
    def grabAttr(k, v):
        attr = None
        if(isinstance(v, dict)):
            attrs = ConversionHelper.grabAttrs(v)
            attr = AttributeHolder(attrs)
        else:
            attr = Attribute(k,v)
        return attr

class AttributeHolder(object):
    def __init__(self, d):
        super(AttributeHolder, self).__init__()
        for k, v in d.items():
            setattr(self, k,v)
    def __repr__(self):
        return str(self.__dict__)

class Attribute(object):
    def __init__(self, k,v):
        super(Attribute, self).__init__()
        self.k = k
        self.v = v
    def __repr__(self):
        return str(self.v)
    def __iter__(self):
	    return iter(self.v)
	def __next__(self):
		next(self.v)


class JsonConverter(object):
    def __init__(self, d):
        super(JsonConverter, self).__init__()
        attributes = ConversionHelper.grabAttrs(d)
        self.__dict__.update(attributes)
    def __repr__(self):
        return str(self.__dict__)