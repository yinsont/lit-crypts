import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./components/App";
  
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <React.StrictMode>
      <BrowserRouter>
        <App></App>
      </BrowserRouter>
    </React.StrictMode>
  );
