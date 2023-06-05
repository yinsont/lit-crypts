import React from "react";
import { Link, Route, Routes } from 'react-router-dom'
import Home from "./Home.js"
import About from "./About.js"
import Login from "./Login.js"
import Signup from "./Signup.js"
import Leaderboard from "./Leaderboard.js"

export default function Navbar() {
 return (
    <div className="app">
      <nav className="navbar">
        <Link className='link' to='/' exact="true">Home</Link>
        <br/>
        <Link className='link' to='/about' exact="true">About</Link>
        <br/>
        <Link className='link' to='/signup' exact="true">Sign-up</Link>
        <br/>
        <Link className='link' to='/login' exact="true">Login</Link>
        <br/>
        <Link className='link' to='/leaderboard' exact="true">Leaderboard</Link>
      </nav>
      <h1 id = "title">Lit🔥 Crypts🧩</h1>
      <Routes>
        <Route path='/' exact="true" element={<Home />} />
        <Route path='/about' exact="true" element={<About />} />
        <Route path='/signup' exact="true" element={<Signup />} />
        <Route path='/login' exact="true" element={<Login />} />
        <Route path='/leaderboard' exact="true" element={<Leaderboard />} />
      </Routes>
    </div>
  );
}

