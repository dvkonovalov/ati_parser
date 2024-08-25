headers_array = {
  "exclude_geo_dicts": True,
  "page": 1,
  "items_per_page": 100,
  "filter": {
    "from": {
      "id": "30",
      "type": 2,
      "radius": 180,
      "exact_only": True
    },
    "to": {
      "id": "30",
      "type": 2,
      "radius": 850,
      "exact_only": True
    },
    "dates": {
      "date_option": "today-plus"
    },
    "weight": {
      "max": 2
    },
    "length": {
      "max": 4.3
    },
    "width": {
      "max": 2.2
    },
    "volume": {
      "max": 20
    },
    "truck_type": "70368744191195",
    "loading_type": "65540",
    "height": {
      "max": 2.2
    },
    "with_dimensions": False,
    "extra_params": 2057,
    "rate": {
      "currency_type_id": 8,
      "type": 0,
      "value": 25
    },
    "change_date": 0,
    "sorting_type": 5,
    "with_auction": False,
    "firm": {
      "firm_rating": 0
    }
  }
}

url_request = "https://loads.ati.su/webapi/public/v1.0/loads/search"