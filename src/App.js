import "./App.css";
import CoronavirusData from "./components/coronavirus_data.js";

function App() {
    return (
        <div className="App">
            <CoronavirusData
                host="coronavirus-monitor.p.rapidapi.com"
                api_key="rvy6OR8SFOjlCcMXB7uGNKXGaPC5OW06"
                country="India"
            />
        </div>
    );
}

export default App;
