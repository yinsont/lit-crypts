export default function KeyCard( {character} ){
    if (character == ' '){
        return null
    }
    return(
        <div >
            <input className = "KeyCard" placeholder={character.toUpperCase()}></input>
        </div>
    )
}