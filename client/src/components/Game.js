import CryptedCard from "./CryptedCard";
import GuessForm from "./GuessForm";
import Encryption from "./Encryption";
import ScoreCard from "./ScoreCard";
import { useState, useEffect } from "react";
import StartModal from "./StartModal";

function Game() {
  const [quote, setQuote] = useState('');
  const [attempts, setAttempts] = useState([])
  
  const [key, setKey] = useState('')
  
  const [modal, setModal] = useState(false)

  useEffect(() => {
    setModal(true)
  }, [])

  useEffect(() => {
    fetch('https://random-word-api.herokuapp.com/word')
      .then(response => response.json())
      .then(data => setKey(data[0]))
  }, [])

  function handleAttempts(value) {
    // console.log(value);
    setAttempts([...attempts, value]);
    // console.log(attempts)
  
    if (value.select in combinedObject) {
      let detect = value.select;
      combinedObject[detect].input = value.input;
      console.log(combinedObject)
    }
  }

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
  // let key = "THIS IS WORKING";
  let encrypted = Encryption(key, sentence);
    console.log(sentence)
  // console.log(encrypted)

  let sentenceArray = sentence.toUpperCase().split("");
  let encryptedArray = encrypted.toUpperCase().split("");
  
  let combinedObject = {};
  
  // Assuming both arrays have the same length
  for (let i = 0; i < sentenceArray.length; i++) {
    const key = sentenceArray[i];
    const value = encryptedArray[i];
  
    // Assigning the value as an object with an empty string
    combinedObject[value.toUpperCase()] = { encrypted: value, original: sentenceArray[i], input: "" };
  }
  console.log(combinedObject)
  
  const [score, setScore] = useState(0);

  function renderScore(score) {
    setScore(score);
  }

  const newPuzzleArray = encrypted.split(" ");

  const letter = newPuzzleArray.map((w, index) => {
    return (
      <div className="word" key={index}>
        {w.split("").map((character) => (
          <CryptedCard character={character} value={combinedObject[character]} attempts = {attempts}/>
        ))}
      </div>
    );
  });

  return (
    <div>
      {modal ? <StartModal closeModal = {() => setModal(false)}/> : null}
      <div className="Game">
        <p id="score">
          Score: {"\n"}
          {score}
        </p>
        <div className="Game-Display">{letter}</div>
        <div className="Game-Keys">
          <GuessForm puzzle={newPuzzleArray} handleAttempts ={handleAttempts}></GuessForm>
          <aside className="timerStyle">
            <ScoreCard renderScore={renderScore} />
          </aside>
        </div>
      </div>
    </div>
  );
}


export default Game;