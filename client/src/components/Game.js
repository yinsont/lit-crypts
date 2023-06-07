import {React, useState} from 'react'
import Card from "./Card";
import KeyCard from "./KeyCard";
import StopWatch from "./StopWatch/StopWatch.jsx";
import Encryption from "./Encryption";

function Game() {

    const [characterKey, setCharacterKey] = useState('')
    
    const changeCharacterKey = (e) => setCharacterKey(e.target.value.toUpperCase())

  let sentence = "food is the greatest thing known to man kind";
  sentence = Encryption("JOHN", "TAR IS FOUND HERE");

  let puzzle = sentence.split(" ");

  let keys = [...new Set(sentence)]; //make new array have one of each character

  let letter = puzzle.map((w) => {
    return (
      <div className="word">
        {w.split("").map((character) => (
          <Card character={character} />
        ))}
      </div>
    );
  });

  const handleClick = (e) => {
    e.preventDefault();
    console.log("hi");
  };

  return (
    <div className="Game">
      <div className="Game-Display">
        {/* {puzzle.map((character) => {
          return <Card character={character} />;
        })} */}
        {letter}
      </div>
      <div className="Game-Keys">
        <form className="Game-Form">
          {keys.map((character) => {
            return <KeyCard character={character} changeCharacterKey = {changeCharacterKey} characterKey={characterKey}/>;
          })}
          <button onClick={handleClick}>Submit</button>
          <aside className="timerStyle">
            <StopWatch />
          </aside>
        </form>
      </div>
    </div>
  );
}

export default Game;
