import React from "react";
import { Link, Route, Routes } from 'react-router-dom'
import Home from "./Home.js"
import About from "./About.js"
import Login from "./Login.js"
import Signup from "./Signup.js"

export default function Navbar() {
 return (
    <div className="app">
      <nav className="navbar">
        <Link className='link' to='/' exact="true">Home</Link>
        <br/>
        <Link className='link' to='/about' exact="true">About</Link>
        <br/>
        <Link className='link' to='/signup' exact="true">Signup</Link>
        <br/>
        <Link className='link' to='/login' exact="true">Login</Link>
        <br/>
      </nav>
      <Routes>
        <Route path='/' exact="true" element={<Home />} />
        <Route path='/about' exact="true" element={<About />} />
        <Route path='/signup' exact="true" element={<Signup />} />
        <Route path='/login' exact="true" element={<Login />} />
      </Routes>
    </div>
  );
}

