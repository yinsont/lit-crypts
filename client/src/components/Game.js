import { React, useState } from "react";
import Card from "./Card";
import KeyCard from "./KeyCard";
import StopWatch from "./StopWatch/StopWatch.jsx";
import Encryption from "./Encryption";

function Game() {
  const [characterKeys, setCharacterKeys] = useState([]);

  let sentence = "we live in a society";
  let key = "THIS IS WORKING"
  let encrypted = Encryption(key, sentence);
  
  let puzzle = encrypted.split(" ");
  
  // let objectPairs = []
  let pairedObject = {};

  sentence.split(' ')
  encrypted.split(' ')
  for (let i = 0; i < sentence.length; i++){
    pairedObject[sentence[i].toUpperCase()] = encrypted[i]
  }
  console.log(pairedObject)

  let keys = [...new Set(encrypted)]; //make new array have one of each character
  
  let letter = puzzle.map((w) => {
    return (
      <div className="word">
        {w.split("").map((character) => (
          <Card character={character}/>
        ))}
      </div>
    );
  });
  const changeCharacterKey = (index, value) => {
    const updatedKeys = [...characterKeys];
    // console.log(value)
    if (typeof value.nativeEvent.data == "string") {
      updatedKeys[index] = value.nativeEvent.data.toUpperCase();
      console.log(updatedKeys[index]);
    } else {
      updatedKeys[index] = "";
    }
    // updatedKeys[index] = value.nativeEvent.data.toUpperCase();
    setCharacterKeys(updatedKeys);
  };

  let inputkeys = keys.map((character, index) => {
    // console.log(character, index)
    return (
      <KeyCard
        value = {character}
        key={index}
        character={character}
        changeCharacterKey={(value) => changeCharacterKey(index, value)}
        characterKey={characterKeys[index] || ""}
      />
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
          {inputkeys}
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
