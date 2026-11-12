Campus & Interactive Map Project (map_project)

An interactive mapping and navigation web application designed to help users explore locations, search for points of interest, and find optimal routes seamlessly.

🚀 Features

Interactive Map View: Smooth zooming, panning, and custom map markers for key locations.

Location Search & Filtering: Quickly locate buildings, landmarks, or departments by name or category.

Pathfinding & Navigation: Calculate and display directions/routes between selected start and destination points.

Responsive Design: Accessible across both desktop and mobile browsers.

🛠️ Tech Stack

(Update this section based on the specific files in your repository)

Frontend: HTML5, CSS3, JavaScript / React.js

Mapping Library: Leaflet.js / Mapbox GL JS / Google Maps API

Backend / Data: Node.js / Python / GeoJSON

📁 Project Structure

map_project/
├── public/              # Static assets, icons, and map tiles
├── src/                 # Main application source code
│   ├── components/      # UI components (Map, SearchBar, Sidebar, etc.)
│   ├── data/            # GeoJSON coordinates and location metadata
│   └── utils/           # Routing and helper functions
├── package.json         # Project dependencies and scripts
└── README.md            # Project documentation


⚙️ Installation & Local Setup

Follow these steps to clone and run the project locally on your machine:

1. Clone the Repository

git clone https://github.com/joshuadasari11/map_project.git
cd map_project


2. Install Dependencies

(Choose the command that matches your project's setup)

For Node.js / React projects:

npm install


For Python projects:

pip install -r requirements.txt


3. Configure Environment Variables (If Applicable)

If the project uses an external Map API key, create a .env file in the root directory and add your key:

VITE_MAP_API_KEY=your_api_key_here


4. Run the Application

For Node.js / React projects:

npm run dev
# or
npm start


For Python projects:

python app.py


For Static HTML/JS projects:
Simply open index.html in your web browser or use the VS Code Live Server extension.

📸 Screenshots

Note: Add screenshots of your running map application inside a screenshots/ folder and update the links below.

![Map Overview](screenshots/map_overview.png)
![Route Navigation](screenshots/route_navigation.png)


🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

📄 License

This project is open-source and available under the MIT License.
