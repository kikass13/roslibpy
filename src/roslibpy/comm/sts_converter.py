# Converts dict to object
# Used in comm.py RosBridgeProtocol(object)._handle_publish(self, message):

class ConversionHelper:
    @staticmethod
    def grabAttrs(container):
        values = None
        if(isinstance(container, dict)):
            values = {}
            for k,v in container.items():
                newAttr = ConversionHelper.grabAttr(k, v)
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
                tmp.append(ConversionHelper.grabAttr(None,value))
            attr = tmp
        else:
            attr = v
        return attr

class AttributeHolder(object):
    def __init__(self, d):
        super(AttributeHolder, self).__init__()
        for k, v in d.items():
            setattr(self, k,v)
    def __repr__(self):
        return str(self.__dict__)

class JsonConverter(object):
    def __init__(self, d):
        super(JsonConverter, self).__init__()
        attributes = ConversionHelper.grabAttrs(d)
        self.__dict__.update(attributes)
    def __repr__(self):
        return str(self.__dict__)