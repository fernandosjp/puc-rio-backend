from os import environ
import coinoxr

class Forex:
    def __init__(self):
        coinoxr.app_id = environ.get("OPEN_FOREX_KEY")
        self.forex = coinoxr

    def get_forex_usd_brl(self, date):
        response = self.forex.Historical().get(date) 
        if response.code != 200:
            raise Exception(f"Failed to get forex data: {response.body}")
        return response.body['rates']['BRL']
