import React from "react";
import Navbar from "./Navbar.js";
import Home from "./Home.js";
import { Route, Routes } from "react-router-dom";
import About from "./About.js";
import Login from "./Login.js";
import Signup from "./Signup.js";
import Leaderboard from "./Leaderboard.js";

function App() {
  
  return (
    <div>
      <Navbar />

      <Routes>
        <Route path="/" exact="true" element={<Home />} />
        <Route path="/about" exact="true" element={<About />} />
        <Route path="/signup" exact="true" element={<Signup />} />
        <Route path="/login" exact="true" element={<Login />} />
        <Route path="/leaderboard" exact="true" element={<Leaderboard />} />
      </Routes>
    </div>
  );
}

export default App;
