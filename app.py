from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import math

app = Flask(__name__)
CORS(app)

# Load the base OpenStreetMap data
with open('campus_data.json', 'r', encoding='utf-8') as file:
    campus_geojson = json.load(file)

# 1. Standard GeoJSON Endpoint (For Leaflet Rendering)
@app.route('/api/map', methods=['GET'])
def get_map():
    return jsonify(campus_geojson)

# 2. Network Topology & State Endpoint (For algorithmic processing)
@app.route('/api/map/graph', methods=['GET'])
def get_graph_topology():
    """
    Strips heavy geographic coordinates and returns a clean list of nodes.
    Ideal for feeding into a C++ priority queue, Best-Fit Decreasing algorithms,
    or OS node simulation engines.
    """
    nodes = []
    for feature in campus_geojson['features']:
        props = feature.get('properties', {})
        if 'name' in props:
            nodes.append({
                "node_id": props['name'],
                # Simulated dynamic resource states for allocation optimization
                "active_nodes": props.get('active_nodes', 4), 
                "max_capacity": props.get('capacity', 200),
                "triage_priority": props.get('priority', 'normal')
            })
            
    return jsonify({
        "status": "ready_for_allocation",
        "topology": nodes
    })

# 3. Spatial Querying Endpoint (Nearest Node calculation)
@app.route('/api/map/nearest', methods=['GET'])
def get_nearest_node():
    """
    Pass coordinates to find the closest campus building.
    Example usage: /api/map/nearest?lat=15.368&lng=75.121
    """
    lat = float(request.args.get('lat', 15.3689))
    lng = float(request.args.get('lng', 75.1214))
    
    nearest_node = None
    min_dist = float('inf')
    
    for feature in campus_geojson['features']:
        if feature['geometry']['type'] == 'Polygon' and 'name' in feature['properties']:
            # Quick centroid approximation for the building polygon
            poly_lng = feature['geometry']['coordinates'][0][0][0]
            poly_lat = feature['geometry']['coordinates'][0][0][1]
            
            # Pythagorean distance for local campus scale
            dist = math.hypot(lat - poly_lat, lng - poly_lng)
            if dist < min_dist:
                min_dist = dist
                nearest_node = feature['properties']['name']
                
    return jsonify({
        "query_coordinates": {"lat": lat, "lng": lng},
        "nearest_node": nearest_node,
        "distance_metric": min_dist
    })

# 4. Thematic UI Payload Endpoint
@app.route('/api/map/config', methods=['GET'])
def get_ui_config():
    """
    Passes modern FinTech and dark-mode aesthetics to the frontend
    so the UI logic remains decoupled from the web application.
    """
    return jsonify({
        "theme": "dark_mode_glassmorphism",
        "styling": {
            "backdrop_filter": "blur(12px)",
            "accents": {
                "primary": "#10b981",    # Emerald
                "secondary": "#4f46e5",  # Indigo
                "highlight": "#39ff14"   # Neon
            },
            "map_elements": {
                "building_fill": "rgba(79, 70, 229, 0.4)",
                "road_stroke": "#10b981"
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)