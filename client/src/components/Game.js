import CryptedCard from "./CryptedCard";
import GuessForm from "./GuessForm";
import Encryption from "./Encryption";
import ScoreCard from "./ScoreCard";
import { useState, useEffect } from "react";

function Game() {
  const [quote, setQuote] = useState('');

  function removeSpecialCharacters(str) {
    return str.replace(/[^\w\s]/gi, '');
  }

  useEffect(() => {
    fetch('http://127.0.0.1:5555/puzzles')
      .then(response => response.json())
      .then(data => {
        const puzzles = data;
        if (puzzles && puzzles.length > 0) {
          const randomIndex = Math.floor(Math.random() * puzzles.length);
          const randomPuzzle = puzzles[randomIndex];
          setQuote(randomPuzzle.quote);
        }
      })
      .catch(error => {
        console.error('Error fetching puzzles:', error);
      });
  }, []);

  let sentence = removeSpecialCharacters(quote);
  let key = "THIS IS WORKING";
  let encrypted = Encryption(key, sentence);

  let pairedObject = {};

  const sentenceArray = sentence.split(" ");
  const encryptedArray = encrypted.split(" ");
  for (let i = 0; i < encryptedArray.length; i++) {
    pairedObject[encryptedArray[i].toUpperCase()] = sentenceArray[i].toUpperCase();
  }

  const [score, setScore] = useState(0);

  function renderScore(score) {
    setScore(score);
  }

  const newPuzzleArray = encrypted.split(" ");

  const letter = newPuzzleArray.map((w, index) => {
    return (
      <div className="word" key={index}>
        {w.split("").map((character, i) => (
          <CryptedCard key={i} character={character} value={pairedObject[character]} />
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
        <GuessForm puzzle={newPuzzleArray}></GuessForm>
        <aside className="timerStyle">
          <ScoreCard renderScore={renderScore} />
        </aside>
      </div>
    </div>
  );
}

export default Game;
