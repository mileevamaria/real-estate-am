from dataclasses import dataclass


@dataclass
class ListAmQueryRange:
    from_query_name = None
    from_value = 0
    to_query_name = None
    to_value = 0
    

class PriceTotal(ListAmQueryRange):
    from_query_name = 'price1'
    to_query_name = 'price2'
    

class PricePerSqm(ListAmQueryRange):
    from_query_name = 'sq_price1'
    to_query_name = 'sq_price2'


class SquareMeters(ListAmQueryRange):
    from_query_name = '_a3_1'
    to_query_name = '_a3_2'


class Floor(ListAmQueryRange):
    from_query_name = '_a11_1'
    to_query_name = '_a11_2'
