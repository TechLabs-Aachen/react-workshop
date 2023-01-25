import openfoodfacts
# https://openfoodfacts.github.io/api-documentation/#jump-6Understandingresponses-Product

def search_product():
    search_result = openfoodfacts.products.advanced_search({
        "search_terms": "nutella",
        "sort_by": "unique_scans_n",
        "page_size": "20"
    })
    pick = search_result

    print(pick["products"][0].keys())
    lookups = ["code", "image_small_url", "image_url", "generic_name",
               "product_name", "quantity", "packaging", "labels",
               "brands", "nutriscore_data", "nutriscore_grade", "environment_impact_level", 
               "environment_impact_level_tags", "carbon_footprint_percent_of_known_ingredients", 
               "nutriments"
               ]

    for lookup in lookups:
        try:
            print(lookup, pick["products"][0][lookup])
        except Exception as err:
            print(f"Error bruh{err}")
    import json
    #print(json.dumps(pick["products"][0], indent=2, sort_keys=True))

search_product()
