import Card from "./Card";
import KeyCard from "./KeyCard";
import Encryption from "./Encryption";
import ScoreCard from "./ScoreCard";
import {useState} from 'react'

function Game() {
  let sentence = "food is the greatest thing known to man kind";
  sentence = (Encryption('JOHN', 'TAR IS FOUND HERE'))

  let puzzle = sentence.split(" ");

  let keys = [...new Set(sentence)];
  const [score, setScore] = useState(0);
 
  function renderScore(score){
    setScore(score)
 }
 

  let letter = puzzle.map((w) => {
    return (
      <div className="word">
        {w.split("").map((character) => (
          <Card character={character} />
        ))}
      </div>
    );
  });

  return (
    <div className="Game">
        <p id = "score">Score: {'\n'}
        {score}</p>
      <div className="Game-Display">
        {letter}
      </div>
      <div className="Game-Keys">
        <form className="Game-Form">
          {keys.map((character) => {
            return <KeyCard character={character} />;
          })}
          <button>Submit</button>
        </form>
        <aside className ="timerStyle">
            <ScoreCard renderScore = {renderScore}/>
        </aside>
      </div>
    </div>
  );
}

export default Game;
