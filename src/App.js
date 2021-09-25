import "./App.css";
import CoronavirusData from "./components/coronavirus_data.js";
import TopBar from "./components/topbar.js";

function App() {
    return (
        <div className="App">
            <TopBar />
            <CoronavirusData
                host="coronavirus-monitor.p.rapidapi.com"
                api_key={process.env.REACT_APP_API_KEY}
                country="India"
            />
        </div>
    );
}

export default App;
