import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

def get_statistical_data(prompt):
    """
    Fetch statistical data relevant to the prompt.
    This is a simplified example - in a real application, you'd have more sophisticated methods.
    """
    # Extract key terms from the prompt for data searching
    key_terms = extract_key_terms(prompt)
    
    # Try to get data from various sources
    data = None
    
    # Example 1: Try World Bank API for economic data
    if any(term in key_terms for term in ['gdp', 'economy', 'population', 'poverty']):
        data = get_world_bank_data(key_terms)
    
    # Example 2: Try web scraping for general statistics
    if not data:
        data = scrape_statistics(key_terms)
    
    # Example 3: Use a predefined dataset for common topics
    if not data:
        data = get_predefined_statistics(prompt)
    
    # Format the data into a paragraph
    if data:
        return format_statistical_paragraph(data, prompt)
    else:
        return "I couldn't find specific statistical data for this topic. This might be a niche subject with limited publicly available statistics."

def extract_key_terms(prompt):
    """
    Extract key terms from the prompt for data searching.
    This is a simplified version - you could use NLP techniques for better extraction.
    """
    # Simple keyword extraction
    common_words = ['the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'about', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'and', 'or', 'but', 'if', 'as', 'of', 'from', 'by', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then', 'once']
    
    words = re.findall(r'\b\w+\b', prompt.lower())
    key_terms = [word for word in words if word not in common_words and len(word) > 2]
    
    return key_terms[:5]  # Return top 5 key terms

def get_world_bank_data(key_terms):
    """
    Fetch data from World Bank API.
    """
    # This is a simplified example - you'd need to map key terms to World Bank indicators
    # Example URL structure: http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date=2010:2020
    
    # For demonstration, we'll return mock data
    return {
        'source': 'World Bank',
        'data': [
            {'year': 2020, 'value': 12345, 'indicator': 'GDP (current US$)'},
            {'year': 2021, 'value': 12890, 'indicator': 'GDP (current US$)'}
        ]
    }

def scrape_statistics(key_terms):
    """
    Scrape statistical data from websites.
    This is a simplified example - in practice, you'd need more robust scraping.
    """
    # For demonstration, we'll return mock data
    return {
        'source': 'Wikipedia',
        'data': [
            {'fact': 'Approximately 65% of the global population uses the internet.'},
            {'fact': 'The average life expectancy worldwide is 73 years.'}
        ]
    }

def get_predefined_statistics(prompt):
    """
    Get statistics from predefined datasets for common topics.
    """
    # In a real application, you'd have a database or dataset for common topics
    predefined_stats = {
        'climate change': [
            {'fact': 'Global average temperature has increased by about 1°C since the pre-industrial era.'},
            {'fact': 'CO2 concentrations in the atmosphere have risen by 50% since 1750.'}
        ],
        'renewable energy': [
            {'fact': 'Renewable energy accounted for 29% of global electricity generation in 2020.'},
            {'fact': 'Solar power capacity grew by 22% globally in 2021.'}
        ]
    }
    
    for topic, stats in predefined_stats.items():
        if topic in prompt.lower():
            return {'source': 'Predefined Dataset', 'data': stats}
    
    return None

def format_statistical_paragraph(data, prompt):
    """
    Format the statistical data into a coherent paragraph.
    """
    if data['source'] == 'World Bank':
        # Format World Bank data
        values = [f"{item['value']} ({item['indicator']})" for item in data['data']]
        return f"According to data from the World Bank, key statistics include: {', '.join(values)}."
    
    elif data['source'] == 'Wikipedia' or data['source'] == 'Predefined Dataset':
        # Format fact-based data
        facts = [item['fact'] for item in data['data']]
        return f"Statistical data shows that {'; '.join(facts)}."
    
    else:
        return "Statistical data is available but could not be formatted properly."