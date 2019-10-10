# Converts dict to object
# Used in comm.py RosBridgeProtocol(object)._handle_publish(self, message):

class ConversionHelper:
    @staticmethod
    def grabAttrs(container):
	    values = None
	    if(isinstance(container, dict)):
	    	values = {}
	    	for k,v in container.items():
				newAttr = CrawlerHelper.grabAttr(k, v)
				values[k] = newAttr
		return values

    @staticmethod
    def grabAttr(k, v):
        attr = None
        if(isinstance(v, dict)):
            attrs = ConversionHelper.grabAttrs(v)
            attr = AttributeHolder(attrs)
        elif(isinstance(v, list)):
            tmp = []
            for value in v:
                tmp.append(CrawlerHelper.grabAttr(None,value))
            attr = AttributeList(k,tmp)
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

class AttributeList(list):
    def __init__(self, k,v):
        super(AttributeList, self).__init__(v)

class Attribute(object):
    def __init__(self, k,v):
        super(Attribute, self).__init__()
        self.k = k
        self.v = v
    def __repr__(self):
        return str(self.v)

class JsonConverter(object):
    def __init__(self, d):
        super(JsonConverter, self).__init__()
        attributes = ConversionHelper.grabAttrs(d)
        self.__dict__.update(attributes)
    def __repr__(self):
        return str(self.__dict__)