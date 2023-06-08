export default function CryptedCard({character}){
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