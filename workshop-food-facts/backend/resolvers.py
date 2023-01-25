from ariadne import QueryType, ObjectType, make_executable_schema, gql
import openfoodfacts
from enum import Enum


type_defs = gql("""
    type Product {
        code: String
        generic_name: String
    }
    type SearchProductResult {
        count: Int!
        page: Int!
        page_count: Int!
        page_size: Int!
        products: [Product!]!
        skip:Int!
    }
    type Query {
        searchProduct: SearchProductResult
    }
""")

query = QueryType()
searchProductResults = ObjectType("SearchProductResult")
product = ObjectType("Product")


class FoodQueryBuilder:
    def simple_query():
        q = openfoodfacts.products.advanced_search({
                "search_terms": "nutella",
                "sort_by": "product_name",
                "page_size": "20",
        })
        return q

@product.field("code")
def resolve_product_code(obj, _):
    if "code" in obj and isinstance(obj["code"], str):
        return obj["code"]
    return None

@product.field("generic_name")
def resolve_product_code(obj, _):
    if "generic_name" in obj and isinstance(obj["generic_name"], str):
        return obj["generic_name"]
    return None

@searchProductResults.field("count")
def resolve_sPR_count(obj, _):
    if "count" in obj and isinstance(obj["count"], int):
        return obj["count"]
    return None

@searchProductResults.field("page")
def resolve_sPR_page(obj, _): 
    if "page" in obj and isinstance(obj["page"], int):
        return obj["page"]
    return None

@searchProductResults.field("page_count")
def resolve_sPR_page_count(obj, _): 
    if "page_count" in obj and isinstance(obj["page_count"], int):
        return obj["page_count"]
    return None

@searchProductResults.field("page_size")
def resolve_sPR_page_size(obj, _): 
    if "page_size" in obj and isinstance(obj["page_size"], int):
        return obj["page_size"]
    return None

@searchProductResults.field("skip")
def resolve_sPR_page_skip(obj, _): 
    if "skip" in obj and isinstance(obj["skip"], int):
        return obj["skip"]
    return None


@searchProductResults.field("products")
def resolve_sPR_page_products(obj, _): 
    if "products" in obj and isinstance(obj["products"], list):
        return obj["products"]
    return None



@query.field("searchProduct")
def resolve_searchProduct(_, info):
    query = FoodQueryBuilder.simple_query()
    print(query)
    return query


schema = make_executable_schema(
    type_defs, query, searchProductResults, product)
