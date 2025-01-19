from difflib import SequenceMatcher

DASHBOARDS = [
    {
        "name": "CPU Monitoring Dashboard",
        "url": "/dashboards/cpu",
        "description": "Monitor CPU performance and usage metrics in real time.",
        "tags": ["CPU", "Performance", "Monitoring"],
        "preview": "/static/images/cpu_dashboard.jpeg",
    },
    {
        "name": "Memory Usage Dashboard",
        "url": "/dashboards/memory",
        "description": "Track memory usage trends and optimize applications.",
        "tags": ["Memory", "Usage", "Optimization"],
        "preview": "/static/images/memory_dashboard.jpeg",
    },
    {
        "name": "Network Traffic Dashboard",
        "url": "/dashboards/network",
        "description": "Analyze network traffic and detect anomalies.",
        "tags": ["Network", "Traffic", "Monitoring"],
        "preview": "/static/images/network_dashboard.jpeg",
    },
]

def search_dashboards(query):
    query_tokens = query.lower().split()  # Split the query into individual words
    results = []

    for dashboard in DASHBOARDS:
        relevance_score = 0

        # Check for matches in the name
        if any(token in dashboard["name"].lower() for token in query_tokens):
            relevance_score += 3

        # Check for matches in the description
        if any(token in dashboard["description"].lower() for token in query_tokens):
            relevance_score += 2

        # Check for matches in the tags
        if any(token in tag.lower() for token in query_tokens for tag in dashboard["tags"]):
            relevance_score += 1

        # If relevance score > 0, add to results with the score
        if relevance_score > 0:
            results.append({"dashboard": dashboard, "score": relevance_score})

    # Sort results by relevance score in descending order
    results.sort(key=lambda x: x["score"], reverse=True)

    # Return the dashboard details without the score
    return [result["dashboard"] for result in results]