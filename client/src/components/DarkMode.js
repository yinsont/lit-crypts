import React, { useState, useEffect } from 'react';
import moon from "./Assets/moon.png"
import './Assets/darkMode.css';

function DarkMode() {
const [theme, setTheme] = useState('light');
const toggleTheme = () => {
    if (theme === 'light') {
      setTheme('dark');
    } else {
      setTheme('light');
    }
  };
  useEffect(() => {document.body.className = theme;}, [theme]);
  return (
    <div className={`App ${theme}`}>
      <button onClick={toggleTheme}> <img id = "moon" src ={moon} alt='Dark-Mode Toggle'></img></button>
    </div>
  );
}
export default DarkMode;

