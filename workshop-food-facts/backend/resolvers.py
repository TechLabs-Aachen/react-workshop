from ariadne import QueryType, ObjectType, make_executable_schema, gql
import openfoodfacts


type_defs = gql("""
    type Nutriments {
        energy_100g: Float
        proteins_100g: Float
        casein_100g: Float
        serum__proteins_100g : Float
        nucleotides_100g: Float
        carbohydrates_100g: Float
        sugars_100g: Float
        sucrose_100g: Float
        glucose_100g: Float
        fructose_100g: Float
        lactose_100g: Float
        maltose_100g: Float
        maltodextrins_100g: Float
        starch_100g: Float
        polyols_100g: Float
        fat_100g: Float
        saturated__fat_100g: Float
        butyric__acid_100g: Float
        caproic__acid_100g: Float
        caprylic__acid_100g: Float
        capric__acid_100g: Float
        lauric__acid_100g: Float
        myristic__acid_100g: Float
        palmitic__acid_100g: Float
        stearic__acid_100g: Float
        arachidic__acid_100g: Float
        behenic__acid_100g: Float
        lignoceric__acid_100g: Float
        cerotic__acid_100g: Float
        montanic__acid_100g: Float
        melissic__acid_100g: Float
        monounsaturated__fat_100g: Float
        polyunsaturated__fat_100g: Float
        omega__3__fat_100g: Float
        alpha__linolenic__acid_100g: Float
        eicosapentaenoic__acid_100g: Float
        docosahexaenoic__acid_100g: Float
        omega__6__fat_100g: Float
        linoleic__acid_100g: Float
        arachidonic__acid_100g: Float
        gamma__linolenic__acid_100g: Float
        dihomo__gamma__linolenic__acid_100g: Float
        omega__9__fat_100g: Float
        oleic__acid_100g: Float
        elaidic__acid_100g: Float
        gondoic__acid_100g: Float
        mead__acid_100g: Float
        erucic__acid_100g: Float
        nervonic__acid_100g: Float
        trans__fat_100g: Float
        cholesterol_100g: Float
        fiber_100g: Float
        sodium_100g: Float
        alcohol_100g: Float
        vitamin__a_100g: Float
        vitamin__d_100g: Float
        vitamin__e_100g: Float
        vitamin__k_100g: Float
        vitamin__c_100g: Float
        vitamin__b1_100g: Float
        vitamin__b2_100g: Float
        vitamin__pp_100g: Float
        vitamin__b6_100g: Float
        vitamin__b9_100g: Float
        vitamin__b12_100g: Float
        biotin_100g: Float
        pantothenic__acid_100g: Float
        silica_100g: Float
        bicarbonate_100g: Float
        potassium_100g: Float
        chloride_100g: Float
        calcium_100g: Float
        phosphorus_100g: Float
        iron_100g: Float
        magnesium_100g: Float
        zinc_100g: Float
        copper_100g: Float
        manganese_100g: Float
        fluoride_100g: Float
        selenium_100g: Float
        chromium_100g: Float
        molybdenum_100g: Float
        iodine_100g: Float
        caffeine_100g: Float
        taurine_100g: Float
    }
    type Product {
        code: String
        generic_name: String
        image_small_url: String 
        image_url: String
        product_name: String
        quantity: String 
        packaging: String
        labels: String
        brands: String
        nutriscore_grade: String
        nutriments: Nutriments
    }
    type SearchProductResult {
        count: Int!
        page: Int!
        page_count: Int!
        page_size: Int!
        products: [Product!]!
        skip:Int!
    }
    enum SearchCriterions {
        brands 
        categories 
        packaging 
        labels 
        origins 
        manufacturing_places 
        emb_codes 
        purchase_places 
        stores 
        countries 
        additives
        allergens
        traces 
        nutrition_grades 
        states 
    }
    enum SearchCriterionsOp {
        contains
        does_not_contain
    }
    
    input SearchParams {
        search: String
        criterions: [SearchCriterions!]
        criterions_op: [SearchCriterionsOp!]
        criterions_val: [String!]
    }
    type Query {
        searchProduct(params: SearchParams): SearchProductResult
    }
""")

query = QueryType()
searchProductResults = ObjectType("SearchProductResult")
product = ObjectType("Product")
nutriments = ObjectType("Nutriments")
searchParameters = ObjectType("SearchParams")
class FoodQueryBuilder:
    def perform_query(searchParams: dict):
        query_dict = {
            "search_terms": searchParams.get("search", None),
            "sort_by": "unique_scans_n",
            "page_size": "20",
        }
        if "criterions" in searchParams and "criterions_op" in searchParams and "criterions_val" in searchParams:
                if (len(searchParams["criterions"]) != len(searchParams["criterions_val"]) or
                    len(searchParams["criterions"]) != len(searchParams["criterions_op"])):
                        return {}
                i = 0
                for crit, op, val in zip(searchParams["criterions"], searchParams["criterions_op"], searchParams["criterions_val"]):
                    query_dict[f"tagtype_{i}"] = crit
                    query_dict[f"tag_contains_{i}"] = op
                    query_dict[f"tag_{i}"] = val

        q = openfoodfacts.products.advanced_search(query_dict)
        return q

@nutriments.field("energy_100g")
@nutriments.field("proteins_100g")
@nutriments.field("casein_100g")
@nutriments.field("serum__proteins_100g")
@nutriments.field("nucleotides_100g")
@nutriments.field("carbohydrates_100g")
@nutriments.field("sugars_100g")
@nutriments.field("sucrose_100g")
@nutriments.field("glucose_100g")
@nutriments.field("fructose_100g")
@nutriments.field("lactose_100g")
@nutriments.field("maltose_100g")
@nutriments.field("maltodextrins_100g")
@nutriments.field("starch_100g")
@nutriments.field("polyols_100g")
@nutriments.field("fat_100g")
@nutriments.field("saturated__fat_100g")
@nutriments.field("butyric__acid_100g")
@nutriments.field("caproic__acid_100g")
@nutriments.field("caprylic__acid_100g")
@nutriments.field("capric__acid_100g")
@nutriments.field("lauric__acid_100g")
@nutriments.field("myristic__acid_100g")
@nutriments.field("palmitic__acid_100g")
@nutriments.field("stearic__acid_100g")
@nutriments.field("arachidic__acid_100g")
@nutriments.field("behenic__acid_100g")
@nutriments.field("lignoceric__acid_100g")
@nutriments.field("cerotic__acid_100g")
@nutriments.field("montanic__acid_100g")
@nutriments.field("melissic__acid_100g")
@nutriments.field("monounsaturated__fat_100g")
@nutriments.field("polyunsaturated__fat_100g")
@nutriments.field("omega__3__fat_100g")
@nutriments.field("alpha__linolenic__acid_100g")
@nutriments.field("eicosapentaenoic__acid_100g")
@nutriments.field("docosahexaenoic__acid_100g")
@nutriments.field("omega__6__fat_100g")
@nutriments.field("linoleic__acid_100g")
@nutriments.field("arachidonic__acid_100g")
@nutriments.field("gamma__linolenic__acid_100g")
@nutriments.field("dihomo__gamma__linolenic__acid_100g")
@nutriments.field("omega__9__fat_100g")
@nutriments.field("oleic__acid_100g")
@nutriments.field("elaidic__acid_100g")
@nutriments.field("gondoic__acid_100g")
@nutriments.field("mead__acid_100g")
@nutriments.field("erucic__acid_100g")
@nutriments.field("nervonic__acid_100g")
@nutriments.field("trans__fat_100g")
@nutriments.field("cholesterol_100g")
@nutriments.field("fiber_100g")
@nutriments.field("sodium_100g")
@nutriments.field("alcohol_100g")
@nutriments.field("vitamin__a_100g")
@nutriments.field("vitamin__d_100g")
@nutriments.field("vitamin__e_100g")
@nutriments.field("vitamin__k_100g")
@nutriments.field("vitamin__c_100g")
@nutriments.field("vitamin__b1_100g")
@nutriments.field("vitamin__b2_100g")
@nutriments.field("vitamin__pp_100g")
@nutriments.field("vitamin__b6_100g")
@nutriments.field("vitamin__b9_100g")
@nutriments.field("vitamin__b12_100g")
@nutriments.field("biotin_100g")
@nutriments.field("pantothenic__acid_100g")
@nutriments.field("silica_100g")
@nutriments.field("bicarbonate_100g")
@nutriments.field("potassium_100g")
@nutriments.field("chloride_100g")
@nutriments.field("calcium_100g")
@nutriments.field("phosphorus_100g")
@nutriments.field("iron_100g")
@nutriments.field("magnesium_100g")
@nutriments.field("zinc_100g")
@nutriments.field("copper_100g")
@nutriments.field("manganese_100g")
@nutriments.field("fluoride_100g")
@nutriments.field("selenium_100g")
@nutriments.field("chromium_100g")
@nutriments.field("molybdenum_100g")
@nutriments.field("iodine_100g")
@nutriments.field("caffeine_100g")
@nutriments.field("taurine_100g")
def resolve_nutriments_fields(obj, info):
    field_name = info.field_name.replace("__","_")
    if field_name in obj and isinstance(obj[field_name], str):
        return obj[field_name]
    return None

@product.field("code")
@product.field("generic_name")
@product.field("image_small_url")
@product.field("image_url")
@product.field("product_name")
@product.field("quantity")
@product.field("packaging")
@product.field("labels")
@product.field("brands")
@product.field("nutriscore_grade")
def resolve_product_fields(obj, info):
    if info.field_name in obj and isinstance(obj[info.field_name], str):
        return obj[info.field_name]
    return None

@product.field("nutriments")
def resolve_products_nutriments(obj, info):
    if info.field_name in obj and isinstance(obj[info.field_name], dict):
        return obj[info.field_name]
    return None

@searchProductResults.field("count")
@searchProductResults.field("page")
@searchProductResults.field("page_count")
@searchProductResults.field("skip")
@searchProductResults.field("page_size")
def resolve_sPR_count(obj, info):
    if info.field_name in obj and isinstance(obj[info.field_name], int):
        return obj[info.field_name]
    return None

@searchProductResults.field("products")
def resolve_sPR_page_products(obj, _): 
    if "products" in obj and isinstance(obj["products"], list):
        return obj["products"]
    return None



@query.field("searchProduct")
def resolve_searchProduct(_, info, params=None):
    query = FoodQueryBuilder.perform_query(params)
    return query


schema = make_executable_schema(
    type_defs, query, searchProductResults, product)
