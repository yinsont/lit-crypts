import Card from "./Card";
import KeyCard from "./KeyCard";
import Encryption from "./Encryption";
import ScoreCard from "./ScoreCard";
import { useState } from "react";

function Game({inputs}) {
  const [characterKeys, setCharacterKeys] = useState([]);

  let sentence = "we live in a society";
  let key = "THIS IS WORKING";
  let encrypted = Encryption(key, sentence);

  let puzzle = encrypted.split(" ");

  // let objectPairs = []
  let pairedObject = {};

  sentence.split(" ");
  encrypted.split(" ");
  for (let i = 0; i < encrypted.length; i++) {
    pairedObject[encrypted[i].toUpperCase()] = sentence[i];
  }
  // console.log(pairedObject)

  let keys = [...new Set(encrypted)]; //make new array have one of each character
  keys.forEach((key) => (inputs[key] = ""));
  // console.log(inputs);

  const [score, setScore] = useState(0);

  function renderScore(score) {
    setScore(score);
  }

  const changeCharacterKey = (index, value, character) => {
    const updatedKeys = [...characterKeys];
    // console.log(value)
    if (typeof value.nativeEvent.data == "string") {
      updatedKeys[index] = value.nativeEvent.data.toUpperCase();
      // console.log(updatedKeys[index]);
    } else {
      updatedKeys[index] = "";
    }
    // updated  Keys[index] = value.nativeEvent.data.toUpperCase();
    setCharacterKeys(updatedKeys);
    inputs[character] = updatedKeys[index];
    console.log(inputs);
    //! character -> defaultChar
    //! <USER INPUT> -> currentChar

    //! charTable = {defaultChar: currentChar}

    //! charTable["E"]
    // console.log('character', character)
  };

  let inputkeys = keys.map((character, index) => {
    //input field buttons
    // console.log(character, index)

    return (
      <KeyCard
        value={character}
        key={index}
        character={character}
        changeCharacterKey={(value) =>
          changeCharacterKey(index, value, character.toUpperCase())
        }
        characterKey={characterKeys[index] || ""}
      />
    );
  });

  let letter = puzzle.map((w) => {
    // game display characters
    return (
      <div className="word">
        {w.split("").map((character) => (
          <Card character={character} value={pairedObject[character]} />
        ))}
      </div>
    );
  });

  return (
    <div className="Game">
      <p id="score">
        Score: {"\n"}
        {score}
      </p>
      <div className="Game-Display">{letter}</div>
      <div className="Game-Keys">
        <form className="Game-Form">
          {inputkeys}
          <button>Submit</button>
        </form>
        <aside className="timerStyle">
          <ScoreCard renderScore={renderScore} />
        </aside>
      </div>
    </div>
  );
}

export default Game;
