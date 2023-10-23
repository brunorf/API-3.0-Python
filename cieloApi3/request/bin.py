from .base import Base

class Bin(Base):

    def __init__(self, merchant, environment):

        super(Bin, self).__init__(merchant)

        self.environment = environment

    def execute(self, card):

        uri = '%s1/cardBin/%s' % (self.environment.api_query, card)
        
        response = self.send_request("GET", uri)

        return response
