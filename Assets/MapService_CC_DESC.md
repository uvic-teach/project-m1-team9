## Component and Connector (C&C) Diagram: [MapService_CC]

### Description:
The 

### Components:
- EDMapData: A python application that parses the bc.gov public database of ED locations for displaying on MapService.
- EDMapView: A python component in the Django-based webapp responsible for compiling contextual data (such as the interactive map) to build HTML for the webpage.
- EDMapURLHandler: Another python component in the Django webapp responsible for mapping URL requests to the map service to the interactive map HTML and Javascript.
- Leaflet Map Library: An open-source Javascript Library capable of rendering interactive mobile-friendly maps with contextual data such as coordinates, field containers, and groupings.
- BC.gov: A CSV of the official government of British Columbia's public database of ED locations.

### Connectors:
- HTTP Connector: Facilitates connection between the User Application and the Map Service.
- Parsing Connector: Links the EDMapData parsing script to a given CSV of ED locations.
- JavaScript Library Connector: Connects the Leaflet Map Library to the EDMapView HTML response renderer.

### Ports & Interfaces:
- EDMapService HTTP Port: Exposes an HTTP endpoint for the User Application to embed the service's interactive map, and to provide user location data.
- Map Rendering Javascript: Leaflet Javascript interface for the EDMapView to render and display ED location data on a map.
- Coordinate Parsing Interface: Python integrated interfaces to extract the ED coordinates from the external CSV source.

### Relationships:
1. EDMapData <-> BC.gov : The coordinate parsing interface extracts the ED location data into workable data format for the webpage.
2. EDMapView <-> Leaflet Library : The JavaScript Library connector enables EDMapView to utilize the Leaflet library for map rendering.
3. EDMapView <-> MrED User Application: The EDMapService HTTP Port is visited by the user application for embedded map viewing in the user interface.
4. EDMapURLHandler <-> MrEd User Application : The EDMapService HTTP Port is given contextual data of the user's location for appropriate map rendering.

### Dependencies:
1. The Django based web app EDMapService depends on the EDMapData to retrieve and provide ED coordinates data.
2. The EDMapView component relies on the JavaScript Library Connector to interact with the Leaflet library for map rendering.

### Configuration:
- The EDMapService microservice is configured with appropriate routing and settings to handle incoming HTTP requests and serve rendered map responses.
- The EDMapData module is configured to retrieve data from BC.gov's public spreadsheet of ED coordinates.

### Constraints:
- The service relies on the availability and accessibility of BC.gov's public spreadsheet whenever the CSV file needs to be updated.
- The EDMapService is limited to the constraints and capabilities of the Django web framework.
- The EDMapView component is constrained by the capabilities of the Leaflet Map Library's map rendering limitations.
