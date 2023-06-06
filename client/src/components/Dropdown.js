import { React, useState } from "react";
import { Link, Route, Routes } from "react-router-dom";
import About from "./About.js";
import Login from "./Login.js";
import Signup from "./Signup.js";
import Leaderboard from "./Leaderboard.js";

export default function Dropdown() {
  return (
      <nav className = "Dropdown-Menu">
            <Link className="link" to="/about" exact="true">
            About
            </Link>
            <Link className="link" to="/signup" exact="true">
            Sign-up
            </Link>
            <Link className="link" to="/login" exact="true">
            Login
            </Link>
            <Link className="link" to="/leaderboard" exact="true">
            Leaderboard
            </Link>

      </nav>
      );
    }
    
    {/* <Routes>
      <Route path="/about" exact="true" element={<About />} />
      <Route path="/signup" exact="true" element={<Signup />} />
      <Route path="/login" exact="true" element={<Login />} />
      <Route path="/leaderboard" exact="true" element={<Leaderboard />} />
    </Routes> */}
    // https://codepen.io/kevinpowell/pen/bawGKx/ff0263bcbff4729a696dc19c8870518e
    // https://www.youtube.com/watch?v=Nloq6uzF8RQ