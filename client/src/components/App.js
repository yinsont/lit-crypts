import React from "react";
import Game from "./Game.js";
import Navbar from "./Navbar.js";
import Leaderboard from "./Leaderboard.js";

function App() {
 return (
    <div>
      <Navbar/>
      <Game/>
      <Leaderboard />
    </div>
  );
}

export default App;
