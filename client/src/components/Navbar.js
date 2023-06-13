import { React, useState } from "react";
import * as RxIcons from "react-icons/rx";
import Dropdown from "./Dropdown.js";
import DarkMode from "./DarkMode.js"
export default function Navbar() {
  const [dropDown, setDropDown] = useState(false);

  const toggleDropDown = () => {
    setDropDown(!dropDown);
  };

  return (
    <>
      <header className="navbar">

        <h1 id="title">Lit🔥 Crypts🧩</h1>
        <DarkMode />
        <button className = "Dropdown-Button" onClick={toggleDropDown} id="dropdown-button">
          {<RxIcons.RxHamburgerMenu />}
        </button>
        
      </header>
      {dropDown ? <Dropdown /> : null}
    </>
  );
}
