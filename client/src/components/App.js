import React from "react";
import Navbar from "./Navbar.js";
import Home from "./Home.js";
import { Link, Route, Routes } from "react-router-dom";
import About from "./About.js";
import Login from "./Login.js";
import Signup from "./Signup.js";
import Leaderboard from "./Leaderboard.js";
import Example from "./Example.js";
import Register from "./Register.js";

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
        <Route path="/example" exact="true" element={<Example />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </div>
  );
}

export default App;
