import { React, useState } from "react";
// import { Link, Route, Routes } from 'react-router-dom'
// import Home from "./Home.js"
// import About from "./About.js"
// import Login from "./Login.js"
// import Signup from "./Signup.js"
// import Leaderboard from "./Leaderboard.js"
import * as RxIcons from "react-icons/rx";
import Dropdown from "./Dropdown.js";
import Modal from "./Modal.js";

export default function Navbar() {
  const [dropDown, setDropDown] = useState(false);
  const [modal, setModal] = useState(false)

  const toggleDropDown = () => {
    setDropDown(!dropDown);
  };

  const callModal = () => {
    // console.log(1)
    setModal(!modal)
  }

  return (
    // <div className="app">
    <>
      <header className="navbar">

        <button onClick = {callModal}>CALL MODAL</button>
        {modal ? <Modal closeModal = {() => setModal(false)}/> : null}

        <h1 id="title">Lit🔥 Crypts🧩</h1>
        <button onClick={toggleDropDown} id="dropdown-button">
          {<RxIcons.RxHamburgerMenu />}
        </button>
      </header>
      {dropDown ? <Dropdown /> : null}
    </>
    // </div>
  );
}
