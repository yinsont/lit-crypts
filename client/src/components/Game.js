import CryptedCard from "./CryptedCard";
import GuessForm from "./GuessForm";
import Encryption from "./Encryption";
import ScoreCard from "./ScoreCard";
import { useState } from "react";
import Quote from "./Quote"

function Game({ inputs }) {

  const [answerSubmition, setAnswerSubmition] = useState({})
  function  handleAnswerSubmition(value){
    setAnswerSubmition(value)
    console.log(value)
  }

  function removeSpecialCharacters(str) {
    return str.replace(/[^\w\s]/gi, '');
  }
  let sentence = "HOLY! MOTHERF***ing S**t #tightaf";

  sentence = removeSpecialCharacters(sentence)
  let key = "THIS IS WORKING";
  let encrypted = Encryption(key, sentence);

  let puzzle = encrypted.split(" ");

  // let objectPairs = []
  let pairedObject = {};

  sentence.split(" ");
  encrypted.split(" ");
  for (let i = 0; i < encrypted.length; i++) {
    pairedObject[encrypted[i].toUpperCase()] = sentence[i].toUpperCase();
  }
  // console.log(pairedObject)
  // console.log(inputs);

  const [score, setScore] = useState(0);

  function renderScore(score) {
    setScore(score);
  }
  //
  // puzzle = puzzle.split('')
  let new_puzzle = puzzle.join("");
  new_puzzle = new_puzzle.split("");
  // console.log(new_puzzle) //! ['F', 'B', 'P', 'V', 'M', 'H']


  let letter = puzzle.map((w) => {
    // game display characters
    return (
      <div className="word">
        {w.split("").map((character) => (
          <CryptedCard character={character} value={pairedObject[character]} />
        ))}
      </div>
    );
  });


  return (
    <div className="Game">
      <Quote />
      <p id="score">
        Score: {"\n"}
        {score}
      </p>
      <div className="Game-Display">{letter}</div>
      <div className="Game-Keys">
        <GuessForm puzzle = {encrypted.split(' ')} handleAnswerSubmition = {handleAnswerSubmition}></GuessForm>
        <aside className="timerStyle">
          <ScoreCard renderScore={renderScore} />
        </aside>
      </div>
    </div>
  );
}

export default Game;
