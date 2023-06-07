export default function KeyCard( {character} ){
    if (character == ' '){
        return null
    }
    return(
        <div >

            <input className = "KeyCard" placeholder={character.toUpperCase()}></input>

            {/* <h1>{character}</h1> */}
        </div>
    )
}