// import { Card } from "semantic-ui-react";
import Card from "./Card";

function Game(){
    let crypted = 'foodisthegreatestthingknowntomankind'
    return(
        <div className="Game">
            <div className = "Game-Display">
                {crypted.split("").map((character) => {
                    return <Card character = {character}/>
                })}
            </div>
            <div className = "Game-Keys">
                <h1>Game Keys</h1>
            </div>
        </div>
    )
}

export default Game