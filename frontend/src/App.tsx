import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
  const fetchData = async () => {
    let retries = 5;
    while (retries) {
      try {
        const response = await fetch("http://localhost:8000/home");
        const data = await response.json();
        setMessage(data.message);
        break;
      } catch (error) {
        console.error("Error fetching:", error);
        retries -= 1;
        await new Promise(resolve => setTimeout(resolve, 2000)); // Esperar 2 segundos antes de reintentar
      }
    }
  };

  fetchData();
}, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;
