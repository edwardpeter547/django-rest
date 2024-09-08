from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name="Product"):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, **kwargs):
    params = {}
    print("this is the kwargs", query, kwargs)
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) > 0:
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters) > 0:
        params["facetFilters"] = index_filters
    index = get_index()
    return index.search(query, params)