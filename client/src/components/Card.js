// import { Card } from "semantic-ui-react";

export default function CryptedCard({character}){
    console.log(character)
    if (character == ' '){
        return <div className="Empty-Card"></div>
    } else {
        return(
            <div className="card">
                <h1>{character.toUpperCase()}</h1>
            </div>
    
        )
    }
}