// import { Card } from "semantic-ui-react";
import Card from "./Card";
import KeyCard from "./KeyCard";
import StopWatch from "./StopWatch/StopWatch.jsx";
import Encryption from "./Encryption";

function Game() {
  let sentence = "food is the greatest thing known to man kind";
  sentence = (Encryption('JOHN', 'TAR IS FOUND HERE'))

  let puzzle = sentence.split(" ");

  let keys = [...new Set(sentence)];
  //   let output = puzzle.join("").split(" ");
//   console.log("result", puzzle);
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
      <div className="Game-Display">
        {/* {puzzle.map((character) => {
          return <Card character={character} />;
        })} */}
        {letter}
      </div>
      <div className="Game-Keys">
        <form className="Game-Form">
          {keys.map((character) => {
            return <KeyCard character={character} />;
          })}
          <button>Submit</button>
          <aside className ="timerStyle">
            <StopWatch />
          </aside>
        </form>
      </div>
    </div>
  );
}

export default Game;
