# services/search_service.py

def search_dashboards(query):
    """
    Search for dashboards based on the query.

    Args:
        query (str): The search query.

    Returns:
        list: A list of matching dashboards.
    """
    # Mock data: Replace with actual database or configuration lookup
    dashboards = [
        {"name": "CPU Usage Dashboard", "url": "/dashboards/cpu"},
        {"name": "Memory Metrics Dashboard", "url": "/dashboards/memory"},
        {"name": "Network Traffic Dashboard", "url": "/dashboards/network"},
        {"name": "VM Performance Dashboard", "url": "/dashboards/vm-performance"}
    ]

    # Filter dashboards based on the query
    if not query:
        return []
    query = query.lower()
    return [d for d in dashboards if query in d['name'].lower()]